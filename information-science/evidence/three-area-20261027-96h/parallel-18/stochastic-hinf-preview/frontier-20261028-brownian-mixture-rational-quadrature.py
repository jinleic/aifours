#!/usr/bin/env python3
"""Exact rational lower Darboux certificate for one 2-time Gaussian mixture."""
from fractions import Fraction as F
from math import isqrt
import heapq

ROOT=10**24
SCALE=10**12
U=F(10000)
TARGET=F(283,200)


def floor_scaled(x):return (x.numerator*SCALE)//x.denominator

def ceil_scaled(x):return -((-x.numerator*SCALE)//x.denominator)


def g_bounds(u):
    if u==0:
        z=F(199,200)
        return floor_scaled(z),ceil_scaled(z)
    u2=u*u
    d=1+F(199,100)*u2+F(99,10000)*u2*u2
    root=isqrt((d.numerator*ROOT*ROOT)//d.denominator)
    lo=(1-F(ROOT,root))/u2
    hi=(1-F(ROOT,root+1))/u2
    lo=max(F(0),lo); hi=min(F(199,200),hi)
    return floor_scaled(lo),ceil_scaled(hi)


def main():
    left=F(0); right=U; gl,gu=g_bounds(left); rl,ru=g_bounds(right)
    lower=(right-left)*rl; upper=(right-left)*gu
    heap=[]; seq=0
    heapq.heappush(heap,(-float(upper-lower),seq,left,right,gl,gu,rl,ru))
    refinements=0; cap=40000
    while lower/F(SCALE)<TARGET and refinements<cap:
        _,_,lo,hi,glo,gup,hlo,hup=heapq.heappop(heap)
        mid=(lo+hi)/2; mlo,mup=g_bounds(mid)
        old_lo=(hi-lo)*hlo; old_hi=(hi-lo)*gup
        low_left=(mid-lo)*mlo; up_left=(mid-lo)*gup
        low_right=(hi-mid)*hlo; up_right=(hi-mid)*mup
        lower+=low_left+low_right-old_lo; upper+=up_left+up_right-old_hi
        seq+=1; heapq.heappush(heap,(-float(up_left-low_left),seq,lo,mid,glo,gup,mlo,mup))
        seq+=1; heapq.heappush(heap,(-float(up_right-low_right),seq,mid,hi,mlo,mup,hlo,hup))
        refinements+=1
    certified=lower/F(SCALE)
    assert certified>=TARGET,'finite refinement cap did not reach target'
    assert TARGET*TARGET*F(7,22)>F(399,500)**2
    print('PASS: exact right-Darboux lower >= 283/200')
    print('refinements:',refinements,'dyadic intervals:',len(heap),'integration cutoff:',U)
    print('PASS: pi<22/7 gives F(99/100 delta_1 + 1/100 delta_1/2)>399/500')
    print('scope: rational/isqrt quadrature conditional on the named Gaussian determinant identity; no optimizer run')


if __name__=='__main__':main()
