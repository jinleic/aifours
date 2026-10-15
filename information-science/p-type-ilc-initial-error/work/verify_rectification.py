"""One bounded supplementary assay for the parent's explicit rectifier candidate."""
import os
for key in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[key] = "1"
from fractions import Fraction as Q
from math import comb, factorial
from pathlib import Path
import hashlib
import json
import sys
import time
import numpy as np
import mpmath as mp
from verify_continuation import physical_trial

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "evidence/continuation"


def integrated_power(n, degree, q, x, ell=Q(1)):
    return sum((Q(comb(n,k))*(-ell)**k*x**(degree+q*k)/factorial(degree+q*k)
                for k in range(n+1)), Q(0))


def rectified_impulse(n, h=Q(1,4), x=Q(1)):
    if n == 0:
        return Q(1)
    return -(integrated_power(n-1,2,1,x)-integrated_power(n-1,2,1,max(Q(0),x-h)))/h


def ramp_impulse(n, q, width, tau=Q(1,4), x=Q(1)):
    if n == 0:
        return min(max((x-tau)/width, Q(0)), Q(1))
    left, right = max(x-tau,Q(0)), max(x-tau-width,Q(0))
    return -(integrated_power(n-1,q+1,q,left)-integrated_power(n-1,q+1,q,right))/width


def shifted_step_impulse(n,q,tau=Q(1,4),x=Q(1)):
    return Q(1) if n == 0 else -integrated_power(n-1,q,q,x-tau)


def exact_identities():
    count = 0
    for ell in (Q(1), Q(2)):
        for n in range(13):
            for t in (Q(0),Q(1,8),Q(1,2),Q(1)):
                lag = sum((Q((-1)**k*comb(n+2,n-k),factorial(k))*(ell*t)**k
                           for k in range(n+1)),Q(0))
                actual = integrated_power(n,2,1,t,ell)
                assert actual == t*t*lag/((n+1)*(n+2))
                count += 1
    return count


def nominal_endpoint(n):
    # r=sin(t)+t^2, not a finite-dimensional polynomial target.
    mp.mp.dps = 100
    value = mp.mpf(0)
    for k in range(n+1):
        jsin = sum((-1)**j/mp.factorial(k+2*j+1) for j in range(45))
        value += (-1)**k*mp.mpf(comb(n,k))*(jsin+2/mp.factorial(k+2))
    return float(value)


def positive_checks():
    n = 48
    impulse = [rectified_impulse(k) for k in range(n+1)]
    signs = [1 if c>=0 else -1 for c in reversed(impulse)]
    expected = sum(map(abs,impulse))/20
    records = []
    for steps in (512,1024):
        t = np.linspace(0,1,steps+1)
        theta = np.maximum(1-4*t,0)
        u = np.zeros(steps+1)
        for sign in signs:
            y = physical_trial(1,u,sign*0.05)
            e = -y
            u += e-theta*e[0]
        discrepancy = abs(float(y[-1])-float(expected))
        assert discrepancy < 1e-4
        records.append({"kind":"adversarial_initial_only","steps":steps,"N":n,
                        "exact_endpoint":float(expected),"actual_endpoint":float(y[-1]),"difference":discrepancy,
                        "signs":signs})
    steps = 800
    t = np.linspace(0,1,steps+1)
    theta = np.maximum(1-4*t,0)
    target = np.sin(t)+t*t
    u = np.zeros(steps+1)
    for n in range(257):
        y = physical_trial(1,u,0)
        error = target-y
        if n in (0,16,64,256):
            exact = nominal_endpoint(n)
            discrepancy = abs(float(error[-1])-exact)
            assert discrepancy < 1e-4
            records.append({"kind":"nonfinite_span_nominal","N":n,"steps":steps,
                            "exact_endpoint_error":exact,"actual_endpoint_error":float(error[-1]),
                            "sup_error":float(np.max(abs(error))),"endpoint_difference":discrepancy})
        u += error-theta*error[0]
    return records


def negative_checks():
    records=[]
    for q in (1,2,3):
        n=24
        step = [shifted_step_impulse(k,q) for k in range(n+1)]
        step_gain=sum(map(abs,step))
        discrepancies=[]
        for width in (Q(1,8),Q(1,32),Q(1,128)):
            response=[ramp_impulse(k,q,width) for k in range(n+1)]
            discrepancy=sum(abs(response[k]-step[k]) for k in range(n+1))
            discrepancies.append(float(discrepancy))
            records.append({"kind":"continuous_ramp_approaching_delayed_step","q":q,"N":n,
                            "width":str(width),"amplification":float(sum(map(abs,response))),
                            "delayed_step_amplification":float(step_gain),"impulse_l1_difference":float(discrepancy)})
        assert discrepancies[-1] < discrepancies[0]
        width=Q(1,32)
        response=[ramp_impulse(k,q,width) for k in range(n+1)]
        signs=[1 if c>=0 else -1 for c in reversed(response)]
        expected=sum(map(abs,response))/20
        steps=1024
        t=np.linspace(0,1,steps+1)
        theta=np.maximum(1-4*t,0)
        psi=np.clip((t-0.25)/float(width),0,1)
        u=np.zeros(steps+1)
        for sign in signs:
            physical=physical_trial(q,u,0)
            measured=physical+sign*0.05*psi
            error=-measured
            assert error[0] == 0
            u+=error-theta*error[0]
        discrepancy=abs(float(measured[-1])-float(expected))
        assert discrepancy < 1e-4
        records.append({"kind":"nonlinear_noise_countercheck","q":q,"N":n,"steps":steps,
                        "noise_zero_on":"[0,1/4]","noise_bound":0.05,"exact_measured_endpoint":float(expected),
                        "measured_endpoint":float(measured[-1]),"physical_endpoint":float(physical[-1]),
                        "difference":discrepancy,"signs":signs})
    return records


def main():
    start=time.time()
    count=exact_identities()
    report={"date_pt":"2026-10-14","protocol":"Fixed rectifier h=1/4, ell=1; no adaptive search. Positive result initial-only; arbitrary-noise counterchecks distinct.",
            "exact_identity_checks":count,"positive":positive_checks(),"negative":negative_checks(),
            "command":f"{sys.executable} {Path(__file__).resolve()}",
            "proof_sha256":hashlib.sha256((ROOT/"work/rectification-boundary.md").read_bytes()).hexdigest()}
    report["seconds"]=time.time()-start
    (OUT/"rectification-verification.json").write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps({"pass":True,"exact_identity_checks":count,"positive_checks":len(report["positive"]),"negative_checks":len(report["negative"]),"seconds":report["seconds"]},indent=2))


if __name__ == "__main__":
    main()
