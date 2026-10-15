(set-logic QF_NRA)
; benchmark generated from python API
(set-info :status unknown)
(declare-fun k_1_0 () Real)
(declare-fun k_0_0 () Real)
(assert
 (= 1.0 0.0))
(assert
 (= (+ 2.0 (* (* 1.0 (- 2.0)) k_1_0)) 0.0))
(assert
 (let ((?x177 (* 1.0 (- 2.0))))
(let ((?x676 (* ?x177 k_0_0)))
(= (+ 12.0 ?x676 (* (* 1.0 16.0) k_1_0) (* ?x676 k_1_0)) 0.0))))
(check-sat)
