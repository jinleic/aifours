# Reduced GS basis, type D4, order [0, 2, 3, 1] (letters a<b<c<... in this order)

Delta = `abcdabcdabcd`, phi = [0, 1, 2, 3]. All parameters k_i range over integers >= 0.
Plus the twist rules x Δ^{±1} -> Δ^{±1} φ(x) and the cancellations ΔΔ^{-1} -> 1, Δ^{-1}Δ -> 1.

| # | leading word | right side |
|---|---|---|
| P1 | `ab b^{k1} c c^{k2} dabcdabcd` | `Δ b^{k1} c^{k2}` |
| P2 | `ba` | `ab` |
| P3 | `ca` | `ac` |
| P4 | `cb` | `bc` |
| P5 | `daa a^{k1} bb b^{k2} cdabcc c^{k3} daa a^{k4} bb b^{k5} c` | `cdabcdaa a^{k2} bb b^{k1} cdd d^{k3} aa a^{k4} bb b^{k5}` |
| P6 | `daa a^{k1} bb b^{k2} cdabcc c^{k3} daa a^{k4} bc` | `cdabcdaa a^{k2} bb b^{k1} cdd d^{k3} aa a^{k4} b` |
| P7 | `daa a^{k1} bb b^{k2} cdabcc c^{k3} daa a^{k4} c` | `cdabcdaa a^{k2} bb b^{k1} cdd d^{k3} aa a^{k4}` |
| P8 | `daa a^{k1} bb b^{k2} cdabcc c^{k3} dabb b^{k4} c` | `cdabcdaa a^{k2} bb b^{k1} cdd d^{k3} abb b^{k4}` |
| P9 | `daa a^{k1} bb b^{k2} cdabcc c^{k3} dabc` | `cdabcdaa a^{k2} bb b^{k1} cdd d^{k3} ab` |
| P10 | `daa a^{k1} bb b^{k2} cdabcc c^{k3} dac` | `cdabcdaa a^{k2} bb b^{k1} cdd d^{k3} a` |
| P11 | `daa a^{k1} bb b^{k2} cdabcc c^{k3} dbb b^{k4} c` | `cdabcdaa a^{k2} bb b^{k1} cdd d^{k3} bb b^{k4}` |
| P12 | `daa a^{k1} bb b^{k2} cdabcc c^{k3} dbc` | `cdabcdaa a^{k2} bb b^{k1} cdd d^{k3} b` |
| P13 | `daa a^{k1} bb b^{k2} cdabcc c^{k3} dc` | `cdabcdaa a^{k2} bb b^{k1} cdd d^{k3}` |
| P14 | `daa a^{k1} bb b^{k2} cdabcdaa a^{k3} bb b^{k4} c` | `cdabcdaa a^{k2} bb b^{k1} cdaa a^{k3} bb b^{k4}` |
| P15 | `daa a^{k1} bb b^{k2} cdabcdaa a^{k3} bc` | `cdabcdaa a^{k2} bb b^{k1} cdaa a^{k3} b` |
| P16 | `daa a^{k1} bb b^{k2} cdabcdaa a^{k3} c` | `cdabcdaa a^{k2} bb b^{k1} cdaa a^{k3}` |
| P17 | `daa a^{k1} bb b^{k2} cdabcdabb b^{k3} c` | `cdabcdaa a^{k2} bb b^{k1} cdabb b^{k3}` |
| P18 | `daa a^{k1} bb b^{k2} cdabcdabc` | `cdabcdaa a^{k2} bb b^{k1} cdab` |
| P19 | `daa a^{k1} bb b^{k2} cdabcdac` | `cdabcdaa a^{k2} bb b^{k1} cda` |
| P20 | `daa a^{k1} bb b^{k2} cdabcdbb b^{k3} c` | `cdabcdaa a^{k2} bb b^{k1} cdbb b^{k3}` |
| P21 | `daa a^{k1} bb b^{k2} cdabcdbc` | `cdabcdaa a^{k2} bb b^{k1} cdb` |
| P22 | `daa a^{k1} bb b^{k2} cdabcdc` | `cdabcdaa a^{k2} bb b^{k1} cd` |
| P23 | `daa a^{k1} bb b^{k2} cdabd` | `cdabcdaa a^{k2} bb b^{k1}` |
| P24 | `daa a^{k1} bb b^{k2} dabcc c^{k3} daa a^{k4} bb b^{k5} c` | `abdabdda a^{k2} b b^{k1} cdd d^{k3} aa a^{k4} bb b^{k5}` |
| P25 | `daa a^{k1} bb b^{k2} dabcc c^{k3} daa a^{k4} bc` | `abdabdda a^{k2} b b^{k1} cdd d^{k3} aa a^{k4} b` |
| P26 | `daa a^{k1} bb b^{k2} dabcc c^{k3} daa a^{k4} c` | `abdabdda a^{k2} b b^{k1} cdd d^{k3} aa a^{k4}` |
| P27 | `daa a^{k1} bb b^{k2} dabcc c^{k3} dabb b^{k4} c` | `abdabdda a^{k2} b b^{k1} cdd d^{k3} abb b^{k4}` |
| P28 | `daa a^{k1} bb b^{k2} dabcc c^{k3} dabc` | `abdabdda a^{k2} b b^{k1} cdd d^{k3} ab` |
| P29 | `daa a^{k1} bb b^{k2} dabcc c^{k3} dac` | `abdabdda a^{k2} b b^{k1} cdd d^{k3} a` |
| P30 | `daa a^{k1} bb b^{k2} dabcc c^{k3} dbb b^{k4} c` | `abdabdda a^{k2} b b^{k1} cdd d^{k3} bb b^{k4}` |
| P31 | `daa a^{k1} bb b^{k2} dabcc c^{k3} dbc` | `abdabdda a^{k2} b b^{k1} cdd d^{k3} b` |
| P32 | `daa a^{k1} bb b^{k2} dabcc c^{k3} dc` | `abdabdda a^{k2} b b^{k1} cdd d^{k3}` |
| P33 | `daa a^{k1} bb b^{k2} dabcdaa a^{k3} bb b^{k4} c` | `abdabdda a^{k2} b b^{k1} cdaa a^{k3} bb b^{k4}` |
| P34 | `daa a^{k1} bb b^{k2} dabcdaa a^{k3} bc` | `abdabdda a^{k2} b b^{k1} cdaa a^{k3} b` |
| P35 | `daa a^{k1} bb b^{k2} dabcdaa a^{k3} c` | `abdabdda a^{k2} b b^{k1} cdaa a^{k3}` |
| P36 | `daa a^{k1} bb b^{k2} dabcdabb b^{k3} c` | `abdabdda a^{k2} b b^{k1} cdabb b^{k3}` |
| P37 | `daa a^{k1} bb b^{k2} dabcdabc` | `abdabdda a^{k2} b b^{k1} cdab` |
| P38 | `daa a^{k1} bb b^{k2} dabcdac` | `abdabdda a^{k2} b b^{k1} cda` |
| P39 | `daa a^{k1} bb b^{k2} dabcdbb b^{k3} c` | `abdabdda a^{k2} b b^{k1} cdbb b^{k3}` |
| P40 | `daa a^{k1} bb b^{k2} dabcdbc` | `abdabdda a^{k2} b b^{k1} cdb` |
| P41 | `daa a^{k1} bb b^{k2} dabcdc` | `abdabdda a^{k2} b b^{k1} cd` |
| P42 | `daa a^{k1} bb b^{k2} dabd` | `abdabdda a^{k2} b b^{k1}` |
| P43 | `daa a^{k1} bcc c^{k2} dabb b^{k3} cdaa a^{k4} b` | `bdabcdaa a^{k2} bcc c^{k1} dd d^{k3} aa a^{k4}` |
| P44 | `daa a^{k1} bcc c^{k2} dabb b^{k3} cdab` | `bdabcdaa a^{k2} bcc c^{k1} dd d^{k3} a` |
| P45 | `daa a^{k1} bcc c^{k2} dabb b^{k3} cdb` | `bdabcdaa a^{k2} bcc c^{k1} dd d^{k3}` |
| P46 | `daa a^{k1} bcc c^{k2} dabcdaa a^{k3} b` | `bdabcdaa a^{k2} bcc c^{k1} daa a^{k3}` |
| P47 | `daa a^{k1} bcc c^{k2} dabcdab` | `bdabcdaa a^{k2} bcc c^{k1} da` |
| P48 | `daa a^{k1} bcc c^{k2} dabcdb` | `bdabcdaa a^{k2} bcc c^{k1} d` |
| P49 | `daa a^{k1} bcc c^{k2} dacd` | `bdabcdaa a^{k2} cc c^{k1}` |
| P50 | `daa a^{k1} bcdabb b^{k2} cdaa a^{k3} b` | `bdabcdabcc c^{k1} dd d^{k2} aa a^{k3}` |
| P51 | `daa a^{k1} bcdabb b^{k2} cdab` | `bdabcdabcc c^{k1} dd d^{k2} a` |
| P52 | `daa a^{k1} bcdabb b^{k2} cdb` | `bdabcdabcc c^{k1} dd d^{k2}` |
| P53 | `daa a^{k1} bcdabcc c^{k2} daa a^{k3} bb b^{k4} c` | `cdabcdabb b^{k1} cdd d^{k2} aa a^{k3} bb b^{k4}` |
| P54 | `daa a^{k1} bcdabcc c^{k2} daa a^{k3} bc` | `cdabcdabb b^{k1} cdd d^{k2} aa a^{k3} b` |
| P55 | `daa a^{k1} bcdabcc c^{k2} daa a^{k3} c` | `cdabcdabb b^{k1} cdd d^{k2} aa a^{k3}` |
| P56 | `daa a^{k1} bcdabcc c^{k2} dabb b^{k3} c` | `cdabcdabb b^{k1} cdd d^{k2} abb b^{k3}` |
| P57 | `daa a^{k1} bcdabcc c^{k2} dabc` | `cdabcdabb b^{k1} cdd d^{k2} ab` |
| P58 | `daa a^{k1} bcdabcc c^{k2} dac` | `cdabcdabb b^{k1} cdd d^{k2} a` |
| P59 | `daa a^{k1} bcdabcc c^{k2} dbb b^{k3} c` | `cdabcdabb b^{k1} cdd d^{k2} bb b^{k3}` |
| P60 | `daa a^{k1} bcdabcc c^{k2} dbc` | `cdabcdabb b^{k1} cdd d^{k2} b` |
| P61 | `daa a^{k1} bcdabcc c^{k2} dc` | `cdabcdabb b^{k1} cdd d^{k2}` |
| P62 | `daa a^{k1} bcdabcdaa a^{k2} b` | `bdabcdabcc c^{k1} daa a^{k2}` |
| P63 | `daa a^{k1} bcdabcdaa a^{k2} c` | `cdabcdabb b^{k1} cdaa a^{k2}` |
| P64 | `daa a^{k1} bcdabcdab` | `bdabcdabcc c^{k1} da` |
| P65 | `daa a^{k1} bcdabcdac` | `cdabcdabb b^{k1} cda` |
| P66 | `daa a^{k1} bcdabcdb` | `bdabcdabcc c^{k1} d` |
| P67 | `daa a^{k1} bcdabcdc` | `cdabcdabb b^{k1} cd` |
| P68 | `daa a^{k1} bcdabd` | `cdabcdabb b^{k1}` |
| P69 | `daa a^{k1} bcdacd` | `bdabcdacc c^{k1}` |
| P70 | `daa a^{k1} bda` | `bdabdd d^{k1}` |
| P71 | `daa a^{k1} cc c^{k2} dabb b^{k3} cdaa a^{k4} b` | `acdacdda a^{k2} bc c^{k1} dd d^{k3} aa a^{k4}` |
| P72 | `daa a^{k1} cc c^{k2} dabb b^{k3} cdab` | `acdacdda a^{k2} bc c^{k1} dd d^{k3} a` |
| P73 | `daa a^{k1} cc c^{k2} dabb b^{k3} cdb` | `acdacdda a^{k2} bc c^{k1} dd d^{k3}` |
| P74 | `daa a^{k1} cc c^{k2} dabcdaa a^{k3} b` | `acdacdda a^{k2} bc c^{k1} daa a^{k3}` |
| P75 | `daa a^{k1} cc c^{k2} dabcdab` | `acdacdda a^{k2} bc c^{k1} da` |
| P76 | `daa a^{k1} cc c^{k2} dabcdb` | `acdacdda a^{k2} bc c^{k1} d` |
| P77 | `daa a^{k1} cc c^{k2} dacd` | `acdacdda a^{k2} c c^{k1}` |
| P78 | `daa a^{k1} cda` | `cdacdd d^{k1}` |
| P79 | `daa a^{k1} da` | `adaad d^{k1}` |
| P80 | `dabb b^{k1} cc c^{k2} daa a^{k3} bcda` | `adabcdabb b^{k2} cc c^{k1} dd d^{k3}` |
| P81 | `dabb b^{k1} cc c^{k2} dabcda` | `adabcdabb b^{k2} cc c^{k1} d` |
| P82 | `dabb b^{k1} cc c^{k2} dbcd` | `adabcdbb b^{k2} cc c^{k1}` |
| P83 | `dabb b^{k1} cdaa a^{k2} bcda` | `adabcdabcc c^{k1} dd d^{k2}` |
| P84 | `dabb b^{k1} cdabcc c^{k2} daa a^{k3} bb b^{k4} c` | `cdabcdaa a^{k1} bcdd d^{k2} aa a^{k3} bb b^{k4}` |
| P85 | `dabb b^{k1} cdabcc c^{k2} daa a^{k3} bc` | `cdabcdaa a^{k1} bcdd d^{k2} aa a^{k3} b` |
| P86 | `dabb b^{k1} cdabcc c^{k2} daa a^{k3} c` | `cdabcdaa a^{k1} bcdd d^{k2} aa a^{k3}` |
| P87 | `dabb b^{k1} cdabcc c^{k2} dabb b^{k3} c` | `cdabcdaa a^{k1} bcdd d^{k2} abb b^{k3}` |
| P88 | `dabb b^{k1} cdabcc c^{k2} dabc` | `cdabcdaa a^{k1} bcdd d^{k2} ab` |
| P89 | `dabb b^{k1} cdabcc c^{k2} dac` | `cdabcdaa a^{k1} bcdd d^{k2} a` |
| P90 | `dabb b^{k1} cdabcc c^{k2} dbb b^{k3} c` | `cdabcdaa a^{k1} bcdd d^{k2} bb b^{k3}` |
| P91 | `dabb b^{k1} cdabcc c^{k2} dbc` | `cdabcdaa a^{k1} bcdd d^{k2} b` |
| P92 | `dabb b^{k1} cdabcc c^{k2} dc` | `cdabcdaa a^{k1} bcdd d^{k2}` |
| P93 | `dabb b^{k1} cdabcda` | `adabcdabcc c^{k1} d` |
| P94 | `dabb b^{k1} cdabcdbb b^{k2} c` | `cdabcdaa a^{k1} bcdbb b^{k2}` |
| P95 | `dabb b^{k1} cdabcdbc` | `cdabcdaa a^{k1} bcdb` |
| P96 | `dabb b^{k1} cdabcdc` | `cdabcdaa a^{k1} bcd` |
| P97 | `dabb b^{k1} cdabd` | `cdabcdaa a^{k1} b` |
| P98 | `dabb b^{k1} cdbcd` | `adabcdbcc c^{k1}` |
| P99 | `dabb b^{k1} daa a^{k2} b` | `adabdd d^{k1} aa a^{k2}` |
| P100 | `dabb b^{k1} dab` | `adabdd d^{k1} a` |
| P101 | `dabb b^{k1} db` | `adabdd d^{k1}` |
| P102 | `dabcc c^{k1} daa a^{k2} bcda` | `adabcdabb b^{k1} cdd d^{k2}` |
| P103 | `dabcc c^{k1} dabb b^{k2} cdaa a^{k3} b` | `bdabcdaa a^{k1} bcdd d^{k2} aa a^{k3}` |
| P104 | `dabcc c^{k1} dabb b^{k2} cdab` | `bdabcdaa a^{k1} bcdd d^{k2} a` |
| P105 | `dabcc c^{k1} dabb b^{k2} cdb` | `bdabcdaa a^{k1} bcdd d^{k2}` |
| P106 | `dabcc c^{k1} dabcda` | `adabcdabb b^{k1} cd` |
| P107 | `dabcc c^{k1} dabcdb` | `bdabcdaa a^{k1} bcd` |
| P108 | `dabcc c^{k1} dacd` | `bdabcdaa a^{k1} c` |
| P109 | `dabcc c^{k1} dbcd` | `adabcdbb b^{k1} c` |
| P110 | `dabcdaa a^{k1} bcda` | `adabcdabcdd d^{k1}` |
| P111 | `dabcdabb b^{k1} cdaa a^{k2} b` | `bdabcdabcdd d^{k1} aa a^{k2}` |
| P112 | `dabcdabb b^{k1} cdab` | `bdabcdabcdd d^{k1} a` |
| P113 | `dabcdabb b^{k1} cdb` | `bdabcdabcdd d^{k1}` |
| P114 | `dabcdabcc c^{k1} daa a^{k2} bb b^{k3} c` | `cdabcdabcdd d^{k1} aa a^{k2} bb b^{k3}` |
| P115 | `dabcdabcc c^{k1} daa a^{k2} bc` | `cdabcdabcdd d^{k1} aa a^{k2} b` |
| P116 | `dabcdabcc c^{k1} daa a^{k2} c` | `cdabcdabcdd d^{k1} aa a^{k2}` |
| P117 | `dabcdabcc c^{k1} dabb b^{k2} c` | `cdabcdabcdd d^{k1} abb b^{k2}` |
| P118 | `dabcdabcc c^{k1} dabc` | `cdabcdabcdd d^{k1} ab` |
| P119 | `dabcdabcc c^{k1} dac` | `cdabcdabcdd d^{k1} a` |
| P120 | `dabcdabcc c^{k1} dbb b^{k2} c` | `cdabcdabcdd d^{k1} bb b^{k2}` |
| P121 | `dabcdabcc c^{k1} dbc` | `cdabcdabcdd d^{k1} b` |
| P122 | `dabcdabcc c^{k1} dc` | `cdabcdabcdd d^{k1}` |
| P123 | `dabcdabcda` | `adabcdabcd` |
| P124 | `dabcdabcdb` | `bdabcdabcd` |
| P125 | `dabcdabcdc` | `cdabcdabcd` |
| P126 | `dabcdabd` | `cdabcdab` |
| P127 | `dabcdacd` | `bdabcdac` |
| P128 | `dabcdbcd` | `adabcdbc` |
| P129 | `dabda` | `bdabd` |
| P130 | `dabdb` | `adabd` |
| P131 | `dacc c^{k1} daa a^{k2} bb b^{k3} c` | `adacdd d^{k1} aa a^{k2} bb b^{k3}` |
| P132 | `dacc c^{k1} daa a^{k2} bc` | `adacdd d^{k1} aa a^{k2} b` |
| P133 | `dacc c^{k1} daa a^{k2} c` | `adacdd d^{k1} aa a^{k2}` |
| P134 | `dacc c^{k1} dabb b^{k2} c` | `adacdd d^{k1} abb b^{k2}` |
| P135 | `dacc c^{k1} dabc` | `adacdd d^{k1} ab` |
| P136 | `dacc c^{k1} dac` | `adacdd d^{k1} a` |
| P137 | `dacc c^{k1} dbb b^{k2} c` | `adacdd d^{k1} bb b^{k2}` |
| P138 | `dacc c^{k1} dbc` | `adacdd d^{k1} b` |
| P139 | `dacc c^{k1} dc` | `adacdd d^{k1}` |
| P140 | `dacda` | `cdacd` |
| P141 | `dacdbb b^{k1} c` | `adacdbb b^{k1}` |
| P142 | `dacdbc` | `adacdb` |
| P143 | `dacdc` | `adacd` |
| P144 | `dad` | `ada` |
| P145 | `dbb b^{k1} cc c^{k2} daa a^{k3} bcda` | `bcdbcddab b^{k2} c c^{k1} dd d^{k3}` |
| P146 | `dbb b^{k1} cc c^{k2} dabcda` | `bcdbcddab b^{k2} c c^{k1} d` |
| P147 | `dbb b^{k1} cc c^{k2} dbcd` | `bcdbcddb b^{k2} c c^{k1}` |
| P148 | `dbb b^{k1} cdaa a^{k2} b` | `cdbcdd d^{k1} aa a^{k2}` |
| P149 | `dbb b^{k1} cdab` | `cdbcdd d^{k1} a` |
| P150 | `dbb b^{k1} cdb` | `cdbcdd d^{k1}` |
| P151 | `dbb b^{k1} daa a^{k2} b` | `bdbbd d^{k1} aa a^{k2}` |
| P152 | `dbb b^{k1} dab` | `bdbbd d^{k1} a` |
| P153 | `dbb b^{k1} db` | `bdbbd d^{k1}` |
| P154 | `dbcc c^{k1} daa a^{k2} bb b^{k3} c` | `bdbcdd d^{k1} aa a^{k2} bb b^{k3}` |
| P155 | `dbcc c^{k1} daa a^{k2} bc` | `bdbcdd d^{k1} aa a^{k2} b` |
| P156 | `dbcc c^{k1} daa a^{k2} c` | `bdbcdd d^{k1} aa a^{k2}` |
| P157 | `dbcc c^{k1} dabb b^{k2} c` | `bdbcdd d^{k1} abb b^{k2}` |
| P158 | `dbcc c^{k1} dabc` | `bdbcdd d^{k1} ab` |
| P159 | `dbcc c^{k1} dac` | `bdbcdd d^{k1} a` |
| P160 | `dbcc c^{k1} dbb b^{k2} c` | `bdbcdd d^{k1} bb b^{k2}` |
| P161 | `dbcc c^{k1} dbc` | `bdbcdd d^{k1} b` |
| P162 | `dbcc c^{k1} dc` | `bdbcdd d^{k1}` |
| P163 | `dbcdaa a^{k1} b` | `cdbcdaa a^{k1}` |
| P164 | `dbcdaa a^{k1} c` | `bdbcdaa a^{k1}` |
| P165 | `dbcdab` | `cdbcda` |
| P166 | `dbcdac` | `bdbcda` |
| P167 | `dbcdb` | `cdbcd` |
| P168 | `dbcdc` | `bdbcd` |
| P169 | `dbd` | `bdb` |
| P170 | `dcc c^{k1} daa a^{k2} bb b^{k3} c` | `cdccd d^{k1} aa a^{k2} bb b^{k3}` |
| P171 | `dcc c^{k1} daa a^{k2} bc` | `cdccd d^{k1} aa a^{k2} b` |
| P172 | `dcc c^{k1} daa a^{k2} c` | `cdccd d^{k1} aa a^{k2}` |
| P173 | `dcc c^{k1} dabb b^{k2} c` | `cdccd d^{k1} abb b^{k2}` |
| P174 | `dcc c^{k1} dabc` | `cdccd d^{k1} ab` |
| P175 | `dcc c^{k1} dac` | `cdccd d^{k1} a` |
| P176 | `dcc c^{k1} dbb b^{k2} c` | `cdccd d^{k1} bb b^{k2}` |
| P177 | `dcc c^{k1} dbc` | `cdccd d^{k1} b` |
| P178 | `dcc c^{k1} dc` | `cdccd d^{k1}` |
| P179 | `dcd` | `cdc` |
