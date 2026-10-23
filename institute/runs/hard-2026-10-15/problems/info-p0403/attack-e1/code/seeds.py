"""Staged published tables; integers x index inputs, x_i=(x>>i)&1.

Hex digits are decoded from left to right, most significant bit first in
each nibble; the first decoded bit is f(0), the last is f(511).
"""

SEEDS = {
    "dsbf40": (
        "68B7EF2DA03B0D3EA00DB6A96DD99AEAFDB9C842B6D5DC8C4526CE0DD29020DB"
        "B75FE3314568344E73688FF0CB2482E065231869E1AA4583765CC491F8A8DB12"
    ),
    "dsbf32": (
        "125425D30A398F36508C06817BEE122E250D973314F976AED58A3EA9120DA4FE"
        "0E4D4575C42DD0426365EBA7FC5F45BE9B2F336981B5E1863618F49474F6FE00"
    ),
    "rsbf56": (
        "3740B6A118A1E19642A85E2B7E2F3C3CB65FA0D95EC9DB1EA92BDB3666185AE0"
        "087F5FE6E0757106A12FC918754C40E8A1BCCB7A714032A8961456E066E8A801"
    ),
}


def decode(hx):
    return [int(b) for ch in hx for b in format(int(ch, 16), "04b")]


def fwht(bits):
    w = [1 - 2*b for b in bits]
    size = 1
    while size < len(w):
        for start in range(0, len(w), 2*size):
            for j in range(size):
                u, v = w[start+j], w[start+j+size]
                w[start+j], w[start+j+size] = u+v, u-v
        size *= 2
    return w
