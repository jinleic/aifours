import Mathlib.Data.Finset.Card
import Mathlib.Data.Fintype.Basic

namespace Mcd.Kernel

abbrev RawQuad := ℕ × ℕ × ℕ × ℕ
abbrev RawTriple := ℕ × ℕ × ℕ

def insertAll : List ℕ → ℕ → Option ℕ
  | [], m => some m
  | c :: l, m => if m.testBit c then none else insertAll l (m ||| 2 ^ c)

def orAll (l : List ℕ) : ℕ := l.foldl (· ||| ·) 0

def quadOK (v : ℕ) (b : RawQuad) : Bool :=
  decide (b.1 < b.2.1) && decide (b.2.1 < b.2.2.1) && decide (b.2.2.1 < b.2.2.2) &&
    decide (b.2.2.2 < v)

def triOK (v : ℕ) (e : RawTriple) : Bool :=
  decide (e.1 < e.2.1) && decide (e.2.1 < e.2.2) && decide (e.2.2 < v)

def pts (e : RawTriple) : List ℕ := [e.1, e.2.1, e.2.2]

def code3 (v a b c : ℕ) : ℕ := (a * v + b) * v + c

def subCodes (v : ℕ) (b : RawQuad) : List ℕ :=
  [code3 v b.1 b.2.1 b.2.2.1, code3 v b.1 b.2.1 b.2.2.2, code3 v b.1 b.2.2.1 b.2.2.2,
    code3 v b.2.1 b.2.2.1 b.2.2.2]

def tripleList (v : ℕ) : List ℕ :=
  (List.range v).flatMap fun a => (List.range' (a + 1) (v - (a + 1))).flatMap fun b =>
    (List.range' (b + 1) (v - (b + 1))).map fun c => code3 v a b c

def allTripleMask (v : ℕ) : ℕ := orAll ((tripleList v).map (2 ^ ·))

def sqsCheck (v : ℕ) (bl : List RawQuad) : Bool :=
  bl.all (quadOK v) && insertAll (bl.flatMap (subCodes v)) 0 == some (allTripleMask v)

def eraseCode (v x : ℕ) (b : RawQuad) : Option ℕ :=
  if b.1 = x then some (code3 v b.2.1 b.2.2.1 b.2.2.2)
  else if b.2.1 = x then some (code3 v b.1 b.2.2.1 b.2.2.2)
  else if b.2.2.1 = x then some (code3 v b.1 b.2.1 b.2.2.2)
  else if b.2.2.2 = x then some (code3 v b.1 b.2.1 b.2.2.1)
  else none

def derivedMask (v : ℕ) (bl : List RawQuad) (x : ℕ) : ℕ :=
  orAll ((bl.filterMap (eraseCode v x)).map (2 ^ ·))

def classOK (v : ℕ) (c : List RawTriple) : Bool :=
  !c.isEmpty && c.all (triOK v) && (insertAll (c.flatMap pts) 0).isSome

def colCheck (v : ℕ) (bl : List RawQuad) (x : ℕ) (cls : List (List RawTriple)) : Bool :=
  cls.all (classOK v) &&
    insertAll (cls.flatten.map fun e => code3 v e.1 e.2.1 e.2.2) 0 == some (derivedMask v bl x)

def pairCodes (v : ℕ) (e : RawTriple) : List ℕ :=
  [e.1 * v + e.2.1, e.1 * v + e.2.2, e.2.1 * v + e.2.2]

def pairList (v : ℕ) : List ℕ :=
  (List.range v).flatMap fun p => (List.range' (p + 1) (v - (p + 1))).map fun q => p * v + q

def allPairMask (v : ℕ) : ℕ := orAll ((pairList v).map (2 ^ ·))

def stsColCheck (v : ℕ) (cls : List (List RawTriple)) : Bool :=
  cls.all (classOK v) && insertAll (cls.flatten.flatMap (pairCodes v)) 0 == some (allPairMask v)

end Mcd.Kernel
