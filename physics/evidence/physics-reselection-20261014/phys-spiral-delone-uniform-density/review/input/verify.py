#!/usr/bin/env python3
"""Replay exact finite controls and deterministic observations for RESULTS.md.

The infinite Delone/density conclusions come from the written proof, not this
finite sample. No network, optimization, package installation, or random search.
"""
from __future__ import annotations

import hashlib
import json
import math
import os
import platform
from pathlib import Path

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("OMP_NUM_THREADS", "1")

import numpy as np
import scipy
from scipy.integrate import quad
from scipy.spatial import cKDTree
from scipy.special import gamma, jv
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def lattice_ball(n: int, squared_radius: int) -> np.ndarray:
    """Every nonzero integer point in a CLOSED ball, exact norm/lexicographic key."""
    if n < 2 or squared_radius < 0:
        raise ValueError("Require dimension >=2 and nonnegative squared radius")
    if squared_radius == 0:
        return np.empty((0, n), dtype=np.int64)
    m = math.isqrt(squared_radius)
    points = np.indices((2*m+1,)*n, dtype=np.int64).reshape(n, -1).T - m
    norms = np.sum(points*points, axis=1)
    keep = (norms > 0) & (norms <= squared_radius)
    points, norms = points[keep], norms[keep]
    keys = tuple(points[:, j] for j in range(n-1, -1, -1)) + (norms,)
    return points[np.lexsort(keys)]


def initial_lattice_vectors(n: int, count: int) -> np.ndarray:
    """Effectively constructible exact first count vectors, including partial ties."""
    if count < 0:
        raise ValueError("Negative prefix count")
    if count == 0:
        return lattice_ball(n, 0)
    radius = 1
    while True:
        points = lattice_ball(n, radius*radius)
        if len(points) >= count:
            return points[:count]
        radius *= 2


def shell_reference(n: int, squared_radius: int) -> np.ndarray:
    """Independent recursive sum-of-squares enumeration, no cube or NumPy sort."""
    def sphere(dim: int, q: int):
        if dim == 1:
            root = math.isqrt(q)
            if root*root == q:
                yield (-root,)
                if root:
                    yield (root,)
            return
        bound = math.isqrt(q)
        for x in range(-bound, bound+1):
            for rest in sphere(dim-1, q-x*x):
                yield (x,)+rest
    vectors = [z for q in range(1, squared_radius+1) for z in sphere(n, q)]
    return np.array(vectors, dtype=np.int64).reshape(-1, n)


def spiral(points: np.ndarray) -> np.ndarray:
    n = points.shape[1]
    rank = np.arange(1, len(points)+1, dtype=float)
    return points*(rank**(1/n)/np.linalg.norm(points, axis=1))[:, None]


def exact_controls() -> dict:
    m = sp.symbols("m", integer=True, nonnegative=True)
    n = m+2
    beta = (n-1)/(n+1)
    alpha = n*(n-1)/(n+1)
    assert sp.simplify((n-1)-beta-alpha) == 0
    assert sp.simplify((n-1)*(1+beta)/2-alpha) == 0
    assert sp.simplify(alpha-(n-1)+beta) == 0
    assert beta.is_positive
    r, q, x = sp.symbols("r q x", positive=True)
    integral = sp.integrate(sp.pi*(r*r-x*x)*sp.cos(2*sp.pi*q*x), (x,-r,r))
    transform = (sp.sin(2*sp.pi*r*q)-2*sp.pi*r*q*sp.cos(2*sp.pi*r*q))/(2*sp.pi**2*q**3)
    assert sp.simplify(integral-transform) == 0
    v3 = 4*sp.pi/3
    assert sp.simplify(v3*(1/v3)) == 1
    wrong_normalization = sp.pi*v3
    assert sp.simplify(wrong_normalization-1).is_positive
    # The leading asymptotic alone does not imply vanishing root displacement.
    assert sp.limit((r+1)**3/r**3, r, sp.oo) == 1
    assert sp.simplify(sp.cbrt((r+1)**3)-r) == 1

    records = []
    for dim, cutoff in ((2,64),(3,64),(4,16)):
        cube = lattice_ball(dim,cutoff)
        reference = shell_reference(dim,cutoff)
        assert np.array_equal(cube,reference)
        assert not np.any(np.all(cube == 0,axis=1))
        assert any(np.array_equal(z,[2]+[0]*(dim-1)) for z in cube)
        records.append({"dimension":dim,"squared_radius":cutoff,"count":len(cube),
                        "independent_exact_enumerators":"equal"})
    assert [len(lattice_ball(3,qmax)) for qmax in (0,1,2,3,4)] == [0,6,18,26,32]
    reference = shell_reference(3,64)
    cuts = [1,5,6,7,17,18,19,25,26,27,31,32,33,100]
    for count in cuts:
        assert np.array_equal(initial_lattice_vectors(3,count),reference[:count])
    # Reversing a tie is allowed mathematically but fails the chosen reproducibility key.
    altered = reference.copy()
    altered[:6] = altered[:6][::-1]
    assert not np.array_equal(altered,reference)
    # Primitive-only enumeration is not this construction.
    primitive = reference[np.gcd.reduce(np.abs(reference),axis=1) == 1]
    assert not np.any(np.all(primitive == [2,0,0],axis=1))
    assert not np.array_equal(primitive[:100],reference[:100])
    return {
        "status":"PASS", "arbitrary_dimension_exponent_identities":"zero; beta>0 for n>=2",
        "three_dimensional_ball_Fourier_identity":"zero symbolic residual",
        "density_normalization":"rho=1/V_3=3/(4*pi); rho*V_3=1",
        "OCR_wrong_V2_control":str(wrong_normalization),
        "main_term_only_negative_control":"(R+1)^3/R^3 ->1, but cube-root displacement is exactly 1",
        "enumerators":records, "closed_ball_boundary_counts_3d":{
            "q0":0,"q1":6,"q2":18,"q3":26,"q4":32},
        "partial_tie_prefix_checks":cuts,
        "nonprimitive_axis_vector":"included in the construction; primitive-only mutation rejected",
        "lexicographic_tie_mutation":"detected as a canonical-generator mismatch, not a theorem counterexample",
    }


def fourier_quadrature_controls() -> dict:
    results = []
    for n in (2,3,4,5,6):
        vprev = np.pi**((n-1)/2)/gamma((n-1)/2+1)
        radius = 1.3
        for freq in (.4,1.1,2.):
            numerical, estimate = quad(
                lambda x: vprev*max(radius*radius-x*x,0)**((n-1)/2)*np.cos(2*np.pi*freq*x),
                -radius,radius,epsabs=1e-11,epsrel=1e-11,limit=200)
            bessel = radius**(n/2)*freq**(-n/2)*jv(n/2,2*np.pi*radius*freq)
            residual = abs(numerical-bessel)
            assert residual < 2e-10
            results.append({"n":n,"radius":radius,"frequency":freq,
                            "absolute_residual":float(residual),
                            "quadrature_error_estimate":float(estimate)})
    return {"status":"PASS","samples":results,
            "max_residual":max(row["absolute_residual"] for row in results),
            "evidence":"Floating quadrature consistency, not a rigorous error bound"}


def empirical_controls() -> dict:
    n, radius = 3,24
    points = lattice_ball(n,radius*radius)
    squared = np.sum(points*points,axis=1)
    generated = spiral(points)
    ranks = np.arange(1,len(points)+1,dtype=float)
    target_radii = np.cbrt(ranks)
    radius_error = float(np.max(np.abs(np.linalg.norm(generated,axis=1)-target_radii)))
    assert radius_error < 1e-10
    v3 = 4*np.pi/3
    c = np.cbrt(v3)
    scaled_lattice = c*points
    displacement = np.linalg.norm(generated-scaled_lattice,axis=1)
    counting = []
    for r in (4,8,12,16,24):
        count = int(np.searchsorted(squared,r*r,side="right"))
        assert np.array_equal(points[:count],lattice_ball(3,r*r))
        ring = (squared > (r/2)**2) & (squared <= r*r)
        error = count+1-v3*r**3
        counting.append({"lattice_radius":r,"nonzero_lattice_count":count,
                         "full_lattice_count_error":float(error),
                         "absolute_error_over_R_power_1_5":float(abs(error)/r**1.5),
                         "max_displacement_in_outer_half_annulus":float(displacement[ring].max())})
    tree = cKDTree(generated)
    distances,_ = tree.query(generated,k=2,workers=1)
    min_separation = float(distances[:,1].min())
    coordinates = np.linspace(-8,8,33)
    query_grid = np.stack(np.meshgrid(coordinates,coordinates,coordinates,indexing="ij"),axis=-1).reshape(-1,3)
    assert np.linalg.norm(query_grid,axis=1).max()+2 < target_radii[-1]
    covering,_ = tree.query(query_grid,k=1,workers=1)

    caps = []
    for count in (1000,10000,50000):
        assert count <= len(points)
        prefix = points[:count]
        norm2 = squared[:count]
        deviations = []
        frequencies = []
        for axis in range(3):
            for sign in (-1,1):
                component = sign*prefix[:,axis]
                hemi = component >= 0
                halfcap = (component >= 0) & (4*component*component >= norm2)
                for name, mask, limit in (("h=0",hemi,.5),("h=1/2",halfcap,.25)):
                    observed = float(mask.mean())
                    deviations.append(abs(observed-limit))
                    frequencies.append({"axis":axis,"sign":sign,"cap":name,
                                        "observed":observed,"uniform_limit":limit})
        caps.append({"prefix_length":count,"max_of_12_cap_deviations":max(deviations),
                     "cap_counts_use_integer_predicates":True,"frequencies":frequencies})

    boxes = [([-0.5,-0.5,-0.5],[0.5,0.5,0.5]),
             ([0.4,-0.3,-0.4],[1.1,0.6,0.5])]
    region_counts = []
    for scale in (4.,8.,12.):
        for low,high in boxes:
            lo,hi = scale*np.array(low),scale*np.array(high)
            corner_radius = np.linalg.norm(np.maximum(np.abs(lo),np.abs(hi)))
            # Both finite samples contain ALL points that can lie in these regions.
            assert corner_radius < min(target_radii[-1],c*radius)
            in_spiral = np.all((generated >= lo) & (generated <= hi),axis=1)
            in_lattice = np.all((scaled_lattice >= lo) & (scaled_lattice <= hi),axis=1)
            mismatch = in_spiral != in_lattice
            if mismatch.any():
                # Distance to some box boundary hyperplane bounds boundary crossing.
                plane_distance = np.min(np.minimum(np.abs(scaled_lattice-lo),np.abs(scaled_lattice-hi)),axis=1)
                assert np.all(plane_distance[mismatch] <= displacement[mismatch]+1e-12)
            volume = float(np.prod(np.array(high)-np.array(low)))
            region_counts.append({"scale":scale,"low":low,"high":high,
                                  "spiral_count":int(in_spiral.sum()),
                                  "scaled_lattice_count":int(in_lattice.sum()),
                                  "normalized_spiral_count":float(in_spiral.sum()/scale**3),
                                  "target_density_times_volume":volume/v3,
                                  "membership_mismatch_count":int(mismatch.sum())})

    # Same exact radii alone do NOT imply separation, covering, or angular UD.
    constant = np.zeros_like(generated)
    constant[:,0] = target_radii
    negative_gap = float(target_radii[-1]-target_radii[-2])
    negative_cover = float(np.linalg.norm(constant-np.array([0.,100.,0.]),axis=1).min())
    assert negative_gap < .001 and negative_cover >= 100
    assert min_separation > 10*negative_gap
    return {
        "status":"PASS", "dimension":n,"lattice_ball_radius":radius,"point_count":len(points),
        "ordered_integer_vectors_sha256":hashlib.sha256(points.astype('<i8').tobytes()).hexdigest(),
        "first_12_integer_vectors":points[:12].tolist(),
        "max_float_exact_radius_residual":radius_error,
        "finite_minimum_separation":min_separation,
        "sampled_covering_radius_in_cube_minus8_to8":float(covering.max()),
        "covering_query_count":len(query_grid),
        "lattice_counts_and_displacements":counting,
        "angular_caps":caps,"Jordan_box_observations":region_counts,
        "negative_constant_direction":{
            "same_radial_count":True,"last_adjacent_gap":negative_gap,
            "distance_from_query_0_100_0":negative_cover,
            "hemisphere_fraction":1.,"uniform_sphere_hemisphere_fraction":.5},
        "scope":"Finite exact generator controls and numerical observations only. No global separation, covering constant, or uniform-distribution theorem is inferred from the sample."
    }


def main() -> None:
    output = {
        "status":"PASS",
        "versions":{"python":platform.python_version(),"numpy":np.__version__,
                    "scipy":scipy.__version__,"sympy":sp.__version__},
        "thread_environment":{name:os.environ.get(name) for name in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS")},
        "exact":exact_controls(),
        "fourier_quadrature":fourier_quadrature_controls(),
        "finite_geometry":empirical_controls(),
        "proof_authority":"RESULTS.md; universal statements are not inferred from finite observations."
    }
    (ROOT/'results/verification.json').write_text(json.dumps(output,indent=2)+'\n')
    print('PASS: exact discrepancy exponents, 3D Fourier identity, density normalization')
    print('PASS: independent exact enumerators, origin/nonprimitive and partial-tie boundaries')
    print('PASS: main-term-only and constant-direction negative controls')
    print('PASS: independent sliced-ball quadrature versus Bessel Fourier formula')
    print('PASS: deterministic finite separation, covering, cap and translated-box observations')
    print('WROTE results/verification.json')


if __name__ == '__main__':
    main()
