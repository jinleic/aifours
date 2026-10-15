#!/usr/bin/env python3
"""Deterministic finite controls for the written universal proof.

Arb inequalities are certified interval comparisons, not float tolerances.
The fixed-area and continued-fraction algebra controls use exact Fractions.
This program does NOT prove universal Chabauty classification by sampling.
"""
from fractions import Fraction as Q
from itertools import product
from math import factorial
from pathlib import Path
import hashlib
import json
import platform
from flint import arb, ctx
import flint

ROOT=Path(__file__).resolve().parents[1]
ctx.prec=256


def ball(value):
    if isinstance(value,Q):
        return arb(f'{value.numerator}/{value.denominator}')
    return arb(value)


def phase_error(alpha,index,nearest):
    if isinstance(alpha,Q):
        return ball(index*alpha-nearest)
    return index*alpha-nearest


def nearest_integer(alpha,index):
    if isinstance(alpha,Q):
        value=index*alpha+Q(1,2)
        return value.numerator//value.denominator
    value=(index*alpha+arb('1/2')).floor().unique_fmpz()
    if value is None:
        raise ArithmeticError('Interval does not determine the nearest integer')
    return int(value)


def certified_inside(squared_norm,radius_squared):
    limit=ball(radius_squared)
    if squared_norm.upper()<=limit.lower():
        return True
    if squared_norm.lower()>limit.upper():
        return False
    raise ArithmeticError('Undecided boundary membership; no tolerance fallback')


def local_data(n,q,alpha,p=None):
    if n<1 or n+q<1:
        raise ValueError('Both source indices must be at least one')
    r=arb(n).sqrt()
    s=arb(n+q).sqrt()
    if p is None:
        p=nearest_integer(alpha,q)
    theta=2*arb.pi()*phase_error(alpha,q,p)
    a=arb(q)/(2*r)
    b=r*theta
    re=s*theta.cos()-r
    im=s*theta.sin()
    error2=(re-a)**2+(im-b)**2
    physical2=(s-r)**2+4*s*r*(theta/2).sin()**2
    return {'p':p,'r':r,'a':a,'b':b,'re':re,'im':im,
            'v2':a*a+b*b,'physical2':physical2,'error2':error2}


def require_bound(error2,radius,r,constant):
    bound=constant*ball(radius)**2/r
    assert error2.upper()<=(bound*bound).lower()


def direct_cartesian(n,q,alpha,data):
    """Independent absolute points, then rotate their difference back."""
    p0=nearest_integer(alpha,n)
    p1=nearest_integer(alpha,n+q)
    t0=2*arb.pi()*phase_error(alpha,n,p0)
    t1=2*arb.pi()*phase_error(alpha,n+q,p1)
    r,s=arb(n).sqrt(),arb(n+q).sqrt()
    dx=s*t1.cos()-r*t0.cos()
    dy=s*t1.sin()-r*t0.sin()
    re=t0.cos()*dx+t0.sin()*dy
    im=-t0.sin()*dx+t0.cos()*dy
    assert re.overlaps(data['re']) and im.overlaps(data['im'])
    return (re-data['a'])**2+(im-data['b'])**2


def liouville_ball():
    # L=sum_{j>=1}10^(-j!). For j>=6 the omitted tail is <2*10^(-720).
    prefix=sum((Q(1,10**factorial(j)) for j in range(1,6)),Q(0))
    return ball(prefix)+arb(0,f'2e-{factorial(6)}')


def local_inclusions():
    angles=[('rational_zero',Q(0)),('rational_two_sevenths',Q(2,7)),
            ('rational_half',Q(1,2)),('sqrt2_minus1',arb(2).sqrt()-1),
            ('golden_conjugate',(arb(5).sqrt()-1)/2),('liouville',liouville_ball())]
    rows=[]
    direct_count=0
    for name,alpha in angles:
        for r_int in [4,12,100,1000]:
            for R in [1,3]:
                if r_int<4*R:
                    continue
                n=r_int*r_int
                reverse=r_int>=12*R
                qlo=-2*r_int*R
                qhi=2*r_int*R+(R*R if reverse else 0)
                forward_count=reverse_count=0
                max_f=max_r=arb(0)
                direct_in_case=0
                for q in range(qlo,qhi+1):
                    d=local_data(n,q,alpha)
                    if certified_inside(d['v2'],R*R):
                        assert abs(phase_error(alpha,q,d['p'])).upper()<arb('1/2')
                        assert n+q>=1
                        require_bound(d['error2'],R,d['r'],5)
                        forward_count+=1
                        ratio=(d['error2']*n/(R**4)).upper()
                        if ratio>max_f: max_f=ratio
                        if q and direct_in_case<2:
                            err2=direct_cartesian(n,q,alpha,d)
                            require_bound(err2,R,d['r'],5)
                            direct_in_case+=1
                            direct_count+=1
                    if reverse and certified_inside(d['physical2'],R*R):
                        # This bound can be an exact equality (r=12R,q=2rR+R^2).
                        # Use the exact rational coordinate, not opposite interval endpoints.
                        assert Q(abs(q),2*r_int)<=Q(25*R,24),(name,n,R,q)
                        assert abs(d['b']).upper()<=ball(Q(12*R,11)).lower()
                        assert d['v2'].upper()<9*R*R
                        require_bound(d['error2'],R,d['r'],45)
                        reverse_count+=1
                        ratio=(d['error2']*n/(R**4)).upper()
                        if ratio>max_r: max_r=ratio
                rows.append({'angle':name,'n':n,'R':R,'q_range':[qlo,qhi],
                             'forward_points_certified':forward_count,
                             'reverse_guard_holds':reverse,'reverse_points_certified':reverse_count,
                             'max_forward_scaled_error_squared_upper':str(max_f),
                             'max_reverse_scaled_error_squared_upper':str(max_r)})
    assert sum(row['forward_points_certified'] for row in rows)>100
    assert sum(row['reverse_points_certified'] for row in rows)>100
    return rows,direct_count


def exact_lattice_algebra():
    determinant_cases=0
    bases=[((1,0),(0,1)),((2,1),(3,2)),((13,8),(21,13)),((34,21),(55,34))]
    for alpha,r,pair in product([Q(0),Q(2,7),Q(-5,11)],[Q(1),Q(17),Q(101,3)],bases):
        (q1,p1),(q2,p2)=pair
        # Vertical coordinates divided by pi; determinant below is covolume/pi.
        u=(Q(q1,1)/(2*r),2*r*(q1*alpha-p1))
        v=(Q(q2,1)/(2*r),2*r*(q2*alpha-p2))
        determinant=u[0]*v[1]-v[0]*u[1]
        assert determinant==q2*p1-q1*p2
        assert abs(determinant)==1
        determinant_cases+=1
    meshes=[]
    for j in [4,8,16,32]:
        eps=Q(1,j)
        u=(eps,Q(0));v=(Q(1,3)*eps,1/eps)
        assert u[0]*v[1]-u[1]*v[0]==1
        assert abs(v[0])<=eps/2
        assert v[1]>3
        for numerator in range(-51,52):
            target=Q(numerator,17)
            nearest=(target/eps+Q(1,2)).numerator//(target/eps+Q(1,2)).denominator
            assert abs(nearest*eps-target)<=eps/2
        meshes.append({'j':j,'fixed_area':'1','transverse_spacing':str(v[1]),'line_mesh_error_bound':str(eps/2)})
    # Continuous scale changes give exactly the displayed diagonal map.
    for r,s,q,p in product([Q(2),Q(7)],[Q(3),Q(11)],[1,5],[-2,3]):
        alpha=Q(2,7)
        old=(Q(q)/(2*r),2*r*(q*alpha-p))
        new=(Q(q)/(2*s),2*s*(q*alpha-p))
        assert new==((r/s)*old[0],(s/r)*old[1])
    return {'unimodular_determinant_cases':determinant_cases,'fixed_area_degenerations':meshes,
            'diagonal_scale_identity_checked':True}


def thin_witnesses():
    old=ctx.prec
    ctx.prec=1024
    alpha=liouville_ball()
    rows=[]
    for q,n,R in [(10**6,10**24,Q(1)),(10**24,10**120,Q(1,10**30))]:
        d=local_data(n,q,alpha)
        assert certified_inside(d['v2'],R*R)
        require_bound(d['error2'],R,d['r'],5)
        rows.append({'q':str(q),'n':str(n),'R':str(R),'linear_length_squared':str(d['v2']),
                     'error_squared_enclosure':str(d['error2']),'proof_role':'finite witness only; non-BA/type existence is proved analytically'})
    ctx.prec=old
    return rows


def negative_controls():
    # A missing factor two in the angular linear term violates the actual bound.
    d=local_data(10**6,1,Q(1,10000))
    wrong=(d['re']-d['a'])**2+(d['im']-d['b']/2)**2
    bound=5/d['r']
    assert wrong.lower()>(bound*bound).upper()
    # Comparing an unrotated physical displacement with a frame lattice is wrong.
    n,q,R,alpha=101**2,4,Q(1,20),Q(1,4)
    d=local_data(n,q,alpha)
    assert certified_inside(d['v2'],R*R)
    require_bound(d['error2'],R,d['r'],5)
    # Here exp(2*pi*i*n*alpha)=i exactly, and q*alpha=1.
    radial=arb(n+q).sqrt()-arb(n).sqrt()
    wrong_rotation=d['a']**2+(radial-d['b'])**2
    limit=5*ball(R)**2/arb(n).sqrt()
    assert wrong_rotation.lower()>(limit*limit).upper()
    # Wrong lift p+1 leaves the physical point unchanged but ruins the linear term.
    good=local_data(10**6,1,Q(1,10000))
    wrong_b=good['b']-2*arb.pi()*good['r']
    err2=(good['re']-good['a'])**2+(good['im']-wrong_b)**2
    reverse_limit=45/good['r']
    assert err2.lower()>(reverse_limit*reverse_limit).upper()
    # The source definition does not allow n+q=0.
    rejected=False
    try:
        local_data(16,-16,Q(0))
    except ValueError:
        rejected=True
    assert rejected
    # Strip/plane limits can occur only after dropping this fixed-area hypothesis.
    for j in [2,4,8,16]:
        assert Q(1,j)!=1 and Q(1,j*j)!=1
    return {'missing_angular_factor_rejected':True,'missing_frame_rotation_rejected':True,
            'wrong_integer_lift_rejected':True,'invalid_source_index_rejected':True,
            'strip_family_nonconstant_area_detected':True,'plane_family_nonconstant_area_detected':True}


def source_integrity():
    entries=json.loads((ROOT/'source/manifest.json').read_text())
    for row in entries:
        data=(ROOT/'source'/row['file']).read_bytes()
        assert len(data)==row['bytes']
        assert hashlib.sha256(data).hexdigest()==row['sha256']
    return len(entries)


def main():
    rows,direct_count=local_inclusions()
    algebra=exact_lattice_algebra()
    thin=thin_witnesses()
    negatives=negative_controls()
    sources=source_integrity()
    report={'python':platform.python_version(),'python_flint':flint.__version__,
            'default_precision_bits':256,'thin_witness_precision_bits':1024,
            'evidence_boundary':'finite exact/interval controls, not a proof by sampling',
            'local_inclusion_cases':rows,'independent_cartesian_comparisons':direct_count,
            'exact_algebra':algebra,'liouville_thin_witnesses':thin,
            'negative_controls':negatives,'source_hashes_verified':sources}
    (ROOT/'results/verification.json').write_text(json.dumps(report,indent=2)+'\n')
    nf=sum(row['forward_points_certified'] for row in rows)
    nr=sum(row['reverse_points_certified'] for row in rows)
    print(f'PASS: {len(rows)} interval window cases; {nf} forward and {nr} reverse points certified, no tolerance fallback.')
    print(f'PASS: {direct_count} independent absolute-Cartesian comparisons.')
    print(f'PASS: {algebra["unimodular_determinant_cases"]} exact determinant cases, fixed-area line degenerations, and diagonal scale identity.')
    print('PASS: 2 rigorous Liouville finite witnesses; 6 negative/boundary controls detected.')
    print(f'PASS: {sources} pinned source hashes. Universal claims rest on RESULTS.md, not these finite checks.')


if __name__=='__main__':
    main()
