# Positive-control check of Kavut-Yucel (arXiv:0808.0684) printed 9-variable truth tables.
# Bit order convention unknown: try MSB-first and LSB-first; nonlinearity is invariant under
# input reversal, so both orders must give the same nl if the hex is transcribed correctly.
import numpy as np
T = {
 "3-DSBF ai=40": "68B7EF2DA03B0D3EA00DB6A96DD99AEAFDB9C842B6D5DC8C4526CE0DD29020DB" "B75FE3314568344E73688FF0CB2482E065231869E1AA4583765CC491F8A8DB12",
 "3-DSBF ai=32": "125425D30A398F36508C06817BEE122E250D973314F976AED58A3EA9120DA4FE" "0E4D4575C42DD0426365EBA7FC5F45BE9B2F336981B5E1863618F49474F6FE00",
 "3-RSBF ai=56": "3740B6A118A1E19642A85E2B7E2F3C3CB65FA0D95EC9DB1EA92BDB3666185AE0" "087F5FE6E0757106A12FC918754C40E8A1BCCB7A714032A8961456E066E8A801",
}
def fwht(v):
    v = v.astype(np.int64).copy(); h = 1
    while h < len(v):
        for i in range(0, len(v), 2 * h):
            a = v[i:i+h].copy(); b = v[i+h:i+2*h].copy()
            v[i:i+h] = a + b; v[i+h:i+2*h] = a - b
        h *= 2
    return v
for name, hx in T.items():
    bits = np.array([int(c) for c in bin(int(hx, 16))[2:].zfill(512)])
    for order, tt in (("msb", bits), ("lsb", bits[::-1])):
        W = fwht(1 - 2 * tt)
        print(f"{name} [{order}]: weight={tt.sum()} nl={256 - np.abs(W).max()//2} walsh_zeros={(W==0).sum()} W0={W[0]} all_W_mod4={set((W % 4).tolist())}")
