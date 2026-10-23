import Gc80.DataMcB
import Gc80.DataMcP0
import Gc80.DataMcP1
import Gc80.DataMcP2
import Gc80.DataMcP3
import Gc80.DataMcP4
import Gc80.DataMcP5
import Gc80.DataMcP6
import Gc80.DataMcP7

/-
GENERATED FILE - do not edit.  Produced by gen_lean80.py from the raw mcDSQS(80) certificate
review/mcdsqs80-parent-inputs-v1/mcdsqs80_c21_A.txt
(973886 bytes, SHA-256 49f500c5eedd9a79553e1228d0232e203a749bbda04e3a891c52778dbe9d44a3, 105985 lines),
first line `# mcDSQS(80) by Tan-Zhou Construction 2.1 (g=20, n=4, s=0) from GCDCQS sha256 58b51b50b5281df613c5fae0a3b0178a374554a2f062e55bd8fc25250922a0ca`.
`colourMc80` lists the 80 raw `POINT` sections in raw order (`POINT 0`, ..., `POINT 79`).
Nothing is assumed about these numbers here: Gc80.Check80 states the checkers and their
soundness theorems, and the Gc80.Cert* modules run them in the Lean kernel.
-/

namespace Mcd.Kernel

/-- The 80 raw `POINT` sections, in raw order. -/
def colourMc80 : List (List (List RawTriple)) := [
    colMc80_0, colMc80_1, colMc80_2, colMc80_3, colMc80_4, colMc80_5, colMc80_6, colMc80_7,
    colMc80_8, colMc80_9, colMc80_10, colMc80_11, colMc80_12, colMc80_13, colMc80_14, colMc80_15,
    colMc80_16, colMc80_17, colMc80_18, colMc80_19, colMc80_20, colMc80_21, colMc80_22, colMc80_23,
    colMc80_24, colMc80_25, colMc80_26, colMc80_27, colMc80_28, colMc80_29, colMc80_30, colMc80_31,
    colMc80_32, colMc80_33, colMc80_34, colMc80_35, colMc80_36, colMc80_37, colMc80_38, colMc80_39,
    colMc80_40, colMc80_41, colMc80_42, colMc80_43, colMc80_44, colMc80_45, colMc80_46, colMc80_47,
    colMc80_48, colMc80_49, colMc80_50, colMc80_51, colMc80_52, colMc80_53, colMc80_54, colMc80_55,
    colMc80_56, colMc80_57, colMc80_58, colMc80_59, colMc80_60, colMc80_61, colMc80_62, colMc80_63,
    colMc80_64, colMc80_65, colMc80_66, colMc80_67, colMc80_68, colMc80_69, colMc80_70, colMc80_71,
    colMc80_72, colMc80_73, colMc80_74, colMc80_75, colMc80_76, colMc80_77, colMc80_78, colMc80_79]

end Mcd.Kernel
