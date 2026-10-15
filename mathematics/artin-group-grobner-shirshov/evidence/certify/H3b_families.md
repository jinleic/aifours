# Reduced GS basis, type H3, order [0, 2, 1] (letters a<b<c<... in this order)

Delta = `abcabcabcabcabc`, phi = [0, 1, 2]. All parameters k_i range over integers >= 0.
Plus the twist rules x Δ^{±1} -> Δ^{±1} φ(x) and the cancellations ΔΔ^{-1} -> 1, Δ^{-1}Δ -> 1.

| # | leading word | right side |
|---|---|---|
| P1 | `ab b^{k1} cabcabcabcabc` | `Δ b^{k1}` |
| P2 | `ba` | `ab` |
| P3 | `caa a^{k1} bcabb b^{k2} cabcabb b^{k3} caa a^{k4} b` | `bcabcabcabb b^{k1} caa a^{k2} bcc c^{k3} aa a^{k4}` |
| P4 | `caa a^{k1} bcabb b^{k2} cabcabb b^{k3} cab` | `bcabcabcabb b^{k1} caa a^{k2} bcc c^{k3} a` |
| P5 | `caa a^{k1} bcabb b^{k2} cabcabb b^{k3} cb` | `bcabcabcabb b^{k1} caa a^{k2} bcc c^{k3}` |
| P6 | `caa a^{k1} bcabb b^{k2} cabcabcaa a^{k3} b` | `bcabcabcabb b^{k1} caa a^{k2} bcaa a^{k3}` |
| P7 | `caa a^{k1} bcabb b^{k2} cabcabcab` | `bcabcabcabb b^{k1} caa a^{k2} bca` |
| P8 | `caa a^{k1} bcabb b^{k2} cabcabcb` | `bcabcabcabb b^{k1} caa a^{k2} bc` |
| P9 | `caa a^{k1} bcabb b^{k2} cabcac` | `bcabcabcabb b^{k1} caa a^{k2}` |
| P10 | `caa a^{k1} bcabcabcabb b^{k2} caa a^{k3} b` | `bcabcabcabb b^{k1} cabcc c^{k2} aa a^{k3}` |
| P11 | `caa a^{k1} bcabcabcabb b^{k2} cab` | `bcabcabcabb b^{k1} cabcc c^{k2} a` |
| P12 | `caa a^{k1} bcabcabcabb b^{k2} cb` | `bcabcabcabb b^{k1} cabcc c^{k2}` |
| P13 | `caa a^{k1} bcabcabcabcaa a^{k2} b` | `bcabcabcabb b^{k1} cabcaa a^{k2}` |
| P14 | `caa a^{k1} bcabcabcabcab` | `bcabcabcabb b^{k1} cabca` |
| P15 | `caa a^{k1} bcabcabcabcb` | `bcabcabcabb b^{k1} cabc` |
| P16 | `caa a^{k1} bcabcabcac` | `bcabcabcabb b^{k1} ca` |
| P17 | `caa a^{k1} bcaca` | `bcabcacc c^{k1}` |
| P18 | `caa a^{k1} cabb b^{k2} cabcabb b^{k3} caa a^{k4} b` | `acacaabcab b^{k1} caa a^{k2} bcc c^{k3} aa a^{k4}` |
| P19 | `caa a^{k1} cabb b^{k2} cabcabb b^{k3} cab` | `acacaabcab b^{k1} caa a^{k2} bcc c^{k3} a` |
| P20 | `caa a^{k1} cabb b^{k2} cabcabb b^{k3} cb` | `acacaabcab b^{k1} caa a^{k2} bcc c^{k3}` |
| P21 | `caa a^{k1} cabb b^{k2} cabcabcaa a^{k3} b` | `acacaabcab b^{k1} caa a^{k2} bcaa a^{k3}` |
| P22 | `caa a^{k1} cabb b^{k2} cabcabcab` | `acacaabcab b^{k1} caa a^{k2} bca` |
| P23 | `caa a^{k1} cabb b^{k2} cabcabcb` | `acacaabcab b^{k1} caa a^{k2} bc` |
| P24 | `caa a^{k1} cabb b^{k2} cabcac` | `acacaabcab b^{k1} caa a^{k2}` |
| P25 | `caa a^{k1} cabcabcabb b^{k2} caa a^{k3} b` | `acacaabcab b^{k1} cabcc c^{k2} aa a^{k3}` |
| P26 | `caa a^{k1} cabcabcabb b^{k2} cab` | `acacaabcab b^{k1} cabcc c^{k2} a` |
| P27 | `caa a^{k1} cabcabcabb b^{k2} cb` | `acacaabcab b^{k1} cabcc c^{k2}` |
| P28 | `caa a^{k1} cabcabcabcaa a^{k2} b` | `acacaabcab b^{k1} cabcaa a^{k2}` |
| P29 | `caa a^{k1} cabcabcabcab` | `acacaabcab b^{k1} cabca` |
| P30 | `caa a^{k1} cabcabcabcb` | `acacaabcab b^{k1} cabc` |
| P31 | `caa a^{k1} cabcabcac` | `acacaabcab b^{k1} ca` |
| P32 | `caa a^{k1} caca` | `acacaac c^{k1}` |
| P33 | `cabb b^{k1} cabcabcabca` | `acabcabcabcabcc c^{k1}` |
| P34 | `cabcabb b^{k1} cabcabb b^{k2} caa a^{k3} b` | `bcabcabcabcaa a^{k1} bcc c^{k2} aa a^{k3}` |
| P35 | `cabcabb b^{k1} cabcabb b^{k2} cab` | `bcabcabcabcaa a^{k1} bcc c^{k2} a` |
| P36 | `cabcabb b^{k1} cabcabb b^{k2} cb` | `bcabcabcabcaa a^{k1} bcc c^{k2}` |
| P37 | `cabcabb b^{k1} cabcabcaa a^{k2} b` | `bcabcabcabcaa a^{k1} bcaa a^{k2}` |
| P38 | `cabcabb b^{k1} cabcabcab` | `bcabcabcabcaa a^{k1} bca` |
| P39 | `cabcabb b^{k1} cabcabcb` | `bcabcabcabcaa a^{k1} bc` |
| P40 | `cabcabb b^{k1} cabcac` | `bcabcabcabcaa a^{k1}` |
| P41 | `cabcabcabcabb b^{k1} caa a^{k2} b` | `bcabcabcabcabcc c^{k1} aa a^{k2}` |
| P42 | `cabcabcabcabb b^{k1} cab` | `bcabcabcabcabcc c^{k1} a` |
| P43 | `cabcabcabcabb b^{k1} cb` | `bcabcabcabcabcc c^{k1}` |
| P44 | `cabcabcabcabca` | `acabcabcabcabc` |
| P45 | `cabcabcabcabcb` | `bcabcabcabcabc` |
| P46 | `cabcabcabcac` | `bcabcabcabca` |
| P47 | `cabcaca` | `bcabcac` |
| P48 | `cacabb b^{k1} caa a^{k2} b` | `acacabcc c^{k1} aa a^{k2}` |
| P49 | `cacabb b^{k1} cab` | `acacabcc c^{k1} a` |
| P50 | `cacabb b^{k1} cb` | `acacabcc c^{k1}` |
| P51 | `cacabcaa a^{k1} b` | `acacabcaa a^{k1}` |
| P52 | `cacabcab` | `acacabca` |
| P53 | `cacabcb` | `acacabc` |
| P54 | `cacac` | `acaca` |
| P55 | `cbb b^{k1} caa a^{k2} b` | `bcbbc c^{k1} aa a^{k2}` |
| P56 | `cbb b^{k1} cab` | `bcbbc c^{k1} a` |
| P57 | `cbb b^{k1} cb` | `bcbbc c^{k1}` |
| P58 | `cbc` | `bcb` |
