#!/usr/bin/env python3
"""Exact identities and physical smokes for the approved four-LG-mode theorem C8.

Written proofs carry the universal quantifiers. Floating propagation comparisons
are empirical. No search, optimization, network access, or extra dependencies.
"""
from __future__ import annotations

import json
import math
import os
import platform
from pathlib import Path
import sys

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("OMP_NUM_THREADS", "1")
sys.dont_write_bytecode = True

import numpy as np
import scipy
from scipy.integrate import quad
from scipy.special import jv
import sympy as sp

from verify import apply_choi, degree

ROOT = Path(__file__).resolve().parents[1]


def symbolic_j(k: sp.Matrix, f: sp.Matrix) -> sp.Matrix:
    return sum((f[b] * sp.conjugate(f[c]) * k[2*b:2*b+2, 2*c:2*c+2]
                for b in range(2) for c in range(2)), sp.zeros(2))


def trace_matrix(k: sp.Matrix) -> sp.Matrix:
    return sp.Matrix(2, 2, lambda b, c: sp.trace(k[2*c:2*c+2, 2*b:2*b+2]))


def covariance_cases() -> dict:
    r = sp.Rational
    omega = sp.Matrix([1, 0, 0, 1])
    swap = sp.Matrix([[1, 0, 0, 0], [0, 0, 1, 0],
                      [0, 1, 0, 0], [0, 0, 0, 1]])
    a = sp.Matrix([[1, sp.I/4], [-sp.I/4, r(3, 2)]])
    transform = sp.kronecker_product(a.T, sp.diag(1, sp.I))
    b0 = sp.eye(4)/4 + omega*omega.T/2
    bplus0 = sp.diag(r(1, 16), 0, 0, 0)
    bsum = transform*b0*transform.H
    bplus = transform*bplus0*transform.H
    c0 = sp.eye(4)/3 + swap/3
    csum = transform*c0*transform.H
    cp = sp.Matrix([[r(3, 5), (1+2*sp.I)/10],
                    [(1-2*sp.I)/10, r(2, 5)]])
    replacement = sp.kronecker_product((a*a).T, cp)
    dark_t = sp.Matrix([[1, sp.I], [-sp.I, 1]])
    rank_one = sp.kronecker_product(dark_t.T, sp.diag(r(3, 4), r(1, 4)))
    pure = omega*omega.T
    return {
        "C6_opposite_azimuth_split": (sp.diag(r(3,4),0,r(3,8),0),
                                       sp.diag(0,r(1,4),0,r(1,8)), r(1,4)),
        "replacement_complex_trace": (replacement/3, 2*replacement/3, r(6,25)),
        "depolarizing_nontrivial_split": (bplus, bsum-bplus, r(1,4)),
        "transpose_endpoint": (csum/3, 2*csum/3, r(1,9)),
        "rank_one_attained_dark_direction": (rank_one/3, 2*rank_one/3, r(1,4)),
        "unpolarized_endpoint": (sp.eye(4)/6, sp.eye(4)/3, sp.Integer(0)),
        "pure_endpoint": (pure/3, 2*pure/3, sp.Integer(1)),
    }


def exact_controls(cases: dict) -> dict:
    m = sp.symbols("m", integer=True, positive=True)
    t, rr, rho = sp.symbols("t rr rho", real=True, positive=True)
    mm = m+1
    q = 1+sp.I*t
    ratio = (mm*(1+t*t)-rr*rr)/(sp.sqrt(mm)*q*q)
    # Check the paraxial radial PDE without numerical propagation.
    # Log-derivatives of q0; radial Laplacian includes -m^2/r^2.
    lr = m/rr-rr/q
    lrr = -m/rr**2-1/q
    lt = -mm*sp.I/q+sp.I*rr**2/(2*q*q)
    assert sp.simplify(lt-sp.I*(lrr+lr**2+lr/rr-m*m/rr**2)/2) == 0
    ratio_pde = sp.diff(ratio,t)-sp.I*(sp.diff(ratio,rr,2)
                 +(2*lr+1/rr)*sp.diff(ratio,rr))/2
    assert sp.simplify(ratio_pde) == 0
    assert sp.simplify(ratio.subs(t,0)-(mm-rr*rr)/sp.sqrt(mm)) == 0
    radial_cross = (mm*sp.factorial(m)-sp.factorial(m+1))/(sp.sqrt(mm)*sp.factorial(m))
    radial_norm = (mm**2*sp.factorial(m)-2*mm*sp.factorial(m+1)
                   +sp.factorial(m+2))/(mm*sp.factorial(m))
    assert sp.simplify(radial_cross) == 0 and sp.simplify(radial_norm) == 1
    # Explicit parametrization of the attained upper half-plane.
    w = sp.simplify(ratio.subs(rr**2,(1+t*t)*(mm+sp.sqrt(mm)*rho)))
    u = rho*(t*t-1)/(1+t*t)
    v = 2*rho*t/(1+t*t)
    assert sp.simplify(w-u-sp.I*v) == 0
    assert sp.simplify(u*u+v*v-rho*rho) == 0
    assert sp.simplify(t*v-(rho+u)) == 0
    # Example proving forward projective density cannot be assumed:
    # Im(w)<0 forces tau>0, and radius>0 forces tau<sqrt(m+1).
    missing_radius_gap = sp.simplify(2*sp.sqrt(mm)-sp.sqrt(mm))
    assert missing_radius_gap.is_positive

    x, y = sp.symbols("x y", real=True)
    f = sp.Matrix([1,x+sp.I*y])
    records = {}
    for name, (plus, minus, p2) in cases.items():
        assert plus == plus.H and minus == minus.H
        assert plus.is_positive_semidefinite and minus.is_positive_semidefinite
        k = plus+minus
        j = symbolic_j(k,f)
        residual = sp.expand((1-p2)*sp.trace(j)**2-4*j.det())
        assert residual == 0, (name,residual)
        # Include the projective direction absent at any finite illuminated radius.
        j_inf = symbolic_j(k,sp.Matrix([0,1]))
        assert sp.simplify((1-p2)*sp.trace(j_inf)**2-4*j_inf.det()) == 0
        tr = trace_matrix(k)
        assert tr.is_positive_semidefinite and tr.rank() > 0
        records[name] = {"polynomial_residual":"0", "degree_squared":str(p2),
                         "trace_rank":tr.rank(),
                         "plus_rank":plus.rank(), "minus_rank":minus.rank()}
    # Attained dark direction: m=3, t=1, R^2=12 gives w=i.
    dark_ratio = sp.simplify(ratio.subs({m:3,t:1,rr:sp.sqrt(12)}))
    assert dark_ratio == sp.I
    gp, gm, _ = cases["rank_one_attained_dark_direction"]
    dark_j = symbolic_j(gp+gm,sp.Matrix([1,sp.I]))
    assert dark_j == sp.zeros(2)
    # Noninvariant, strictly positive sum; two physically attained directions.
    bad = sp.diag(3,1,1,3)
    bad_j = symbolic_j(bad,f)
    bad_poly = sp.expand(sp.Rational(3,4)*sp.trace(bad_j)**2-4*bad_j.det())
    assert bad_poly == -16*(x*x+y*y)
    bad_degrees = []
    for w0 in (sp.Integer(0),sp.I):
        mat = symbolic_j(bad,sp.Matrix([1,w0]))
        bad_degrees.append(sp.simplify(1-4*mat.det()/sp.trace(mat)**2))
    assert bad_degrees == [sp.Rational(1,4),0]
    # A nontrivial split need not obey the sum's degree in either sector.
    plus, minus, _ = cases["depolarizing_nontrivial_split"]
    sector_values = []
    for w0 in (sp.Integer(0),sp.I):
        mat = symbolic_j(minus,sp.Matrix([1,w0]))
        sector_values.append(sp.simplify(1-4*mat.det()/sp.trace(mat)**2))
    assert sector_values[0] != sector_values[1]
    assert trace_matrix(sp.zeros(4)) == sp.zeros(2)
    return {"status":"PASS","arbitrary_integer_m_PDE_residuals":["0","0"],
            "radial_cross_inner_product":"0","radial_n1_norm":"1",
            "upper_half_plane_inverse_identities":"PASS",
            "forward_CP1_density":"FALSE; -2i*sqrt(m+1) lies outside the response closure",
            "families":records,"attained_dark_direction":{
                "m":3,"z_over_k_a_squared":1,"R_squared":12,"ratio":"i",
                "coherency_matrix":str(dark_j),"degree":"undefined; not assigned zero"},
            "negative_control_polynomial":str(bad_poly),
            "negative_control_degree_squared":[str(v0) for v0 in bad_degrees],
            "individual_minus_sector_degree_squared":[str(v0) for v0 in sector_values],
            "zero_source":"trace matrix zero; excluded from nonzero-source classification"}


def radial_modes(radius: np.ndarray, z: float, k: float, m: int) -> np.ndarray:
    t = z/k  # frozen waist a=1 for physical smokes
    q = 1+1j*t
    q0 = radius**m*np.exp(-radius**2/(2*q))/(np.sqrt(np.pi*math.factorial(m))*q**(m+1))
    ratio = ((m+1)*(1+t*t)-radius**2)/(np.sqrt(m+1)*q*q)
    return np.stack((q0,ratio*q0),axis=-1)


def hankel_controls() -> dict:
    records = []
    for m in (1,3):
        for z in (1.5,8.0):
            for radius in (0.625,1.25,2.0):
                for n in (0,1):
                    def integrand(r: float) -> complex:
                        initial = r**m*np.exp(-r*r/2)/np.sqrt(np.pi*math.factorial(m))
                        if n:
                            initial *= (m+1-r*r)/np.sqrt(m+1)
                        return r*initial*np.exp(1j*7*r*r/(2*z))*jv(m,7*radius*r/z)
                    real,_ = quad(lambda r: integrand(r).real,0,12,epsabs=2e-11,epsrel=2e-11,limit=400)
                    imag,_ = quad(lambda r: integrand(r).imag,0,12,epsabs=2e-11,epsrel=2e-11,limit=400)
                    integrated = 7/(1j*z)*(-1j)**m*np.exp(1j*7*radius**2/(2*z))*(real+1j*imag)
                    expected = radial_modes(np.array(radius),z,7,m)[n]
                    error = float(abs(integrated-expected))
                    assert error < 2e-9, (m,n,z,radius,error)
                    records.append({"m":m,"n":n,"z":z,"r":radius,"amplitude_error":error})
    return {"status":"PASS","integrals":records,
            "max_amplitude_error":max(r["amplitude_error"] for r in records),
            "quadrature_is_not_an_interval_bound":True}


def physical_smoke(cases: dict) -> dict:
    ngrid,length,k = 256,24.,7.
    axis = (np.arange(ngrid)-ngrid//2)*length/ngrid
    xx,yy = np.meshgrid(axis,axis,indexing="ij")
    radius = np.hypot(xx,yy)
    angle = np.arctan2(yy,xx)
    dx = length/ngrid
    spatial_q = 2*np.pi*np.fft.fftfreq(ngrid,dx)
    q2 = spatial_q[:,None]**2+spatial_q[None,:]**2
    region = radius <= 4
    records = []
    for m in (1,3):
        initial_radial = radial_modes(radius,0,k,m)
        angular = {sign:np.exp(1j*sign*m*angle) for sign in (1,-1)}
        for name,(gplus,gminus,p2) in cases.items():
            gamma_sum = np.array(gplus+gminus,dtype=complex)
            # Independent physical realization of each sector covariance.
            coherent_fields = []
            for sign,g in ((1,gplus),(-1,gminus)):
                numeric = np.array(g,dtype=complex)
                eigenvalues,eigenvectors = np.linalg.eigh(numeric)
                assert eigenvalues.min() > -1e-12
                # Exact PSD was checked above; only roundoff-negative zeros are clipped.
                factors = (eigenvectors*np.sqrt(np.maximum(eigenvalues,0))[None,:]).reshape(2,2,4)
                sector = np.einsum("xyn,nil->xyil",initial_radial,factors)
                coherent_fields.append(sector*angular[sign][:,:,None,None])
            fields = np.concatenate(coherent_fields,axis=-1)
            spectrum = np.fft.fft2(fields,axes=(0,1))
            for z in (1.5,4.0,8.0):
                propagated = np.fft.ifft2(spectrum*np.exp(-1j*z*q2/(2*k))[:,:,None,None],axes=(0,1))
                actual = np.einsum("xyil,xyjl->xyij",propagated,propagated.conj())
                predicted = apply_choi(gamma_sum,radial_modes(radius,z,k,m))
                error = float(np.max(np.abs(actual[region]-predicted[region])))
                intensity = np.trace(predicted,axis1=-2,axis2=-1).real
                reliable = region & (intensity > 1e-6*intensity[region].max())
                p_expected = float(sp.sqrt(p2))
                p_error = float(np.max(np.abs(degree(actual[reliable])-p_expected)))
                assert error < 2e-9 and p_error < 5e-8, (name,m,z,error,p_error)
                records.append({"case":name,"m":m,"z":z,"matrix_max_error":error,
                                "degree_max_error":p_error,"degree_sample_count":int(reliable.sum())})
        # Physical negative control: independent radial polarization populations.
        bad = np.diag([3.,1.,1.,3.])
        bad_j = apply_choi(bad,radial_modes(radius,4,k,m))
        intensity = np.trace(bad_j,axis1=-2,axis2=-1).real
        mask = region & (intensity > 1e-6*intensity[region].max())
        bad_p = degree(bad_j[mask])
        assert bad_p.max()-bad_p.min() > .4
        records.append({"case":"noninvariant_negative_control","m":m,
                        "degree_range":[float(bad_p.min()),float(bad_p.max())]})
    return {"status":"PASS","grid":{"n":ngrid,"length":length,"k":k,"waist_a":1,
                "m":[1,3],"z":[1.5,4.,8.],"comparison_radius_max":4,
                "degree_relative_intensity_floor":1e-6},
            "records":records,
            "max_matrix_error":max(r["matrix_max_error"] for r in records if "matrix_max_error" in r),
            "max_degree_error":max(r["degree_max_error"] for r in records if "degree_max_error" in r)}


def main() -> None:
    cases = covariance_cases()
    exact = exact_controls(cases)
    hankel = hankel_controls()
    smoke = physical_smoke(cases)
    out = {"status":"PASS","claim":"RESULTS.md C8; restricted Fresnel sum-block classification",
           "versions":{"python":platform.python_version(),"numpy":np.__version__,
                       "scipy":scipy.__version__,"sympy":sp.__version__},
           "effective_thread_environment":{k:os.environ.get(k) for k in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS")},
           "exact":exact,"hankel":hankel,"physical_smoke":smoke,
           "scope":"Exact identities plus empirical physical propagation controls; the written open-set polynomial proof carries universal necessity."}
    (ROOT/'results/lg-fresnel-classification.json').write_text(json.dumps(out,indent=2)+'\n')
    print("PASS: arbitrary-m LG propagation and normalization identities")
    print("PASS: attained open response set; false projective-density route rejected")
    print("PASS: seven exact PSD sum/split families, endpoints, dark direction, negative controls")
    print("PASS: independent Hankel-Fresnel versus analytic LG amplitudes")
    print("PASS: physical sector-covariance FFT2 versus sum-block prediction at 42 cases")
    print("WROTE results/lg-fresnel-classification.json")


if __name__ == '__main__':
    main()
