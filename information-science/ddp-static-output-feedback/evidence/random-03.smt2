(set-logic QF_NRA)
; benchmark generated from python API
(set-info :status unknown)
(declare-fun k_1_0 () Real)
(declare-fun k_0_0 () Real)
(assert
 (= (* (* 1.0 (- 4.0)) k_1_0) 0.0))
(assert
 (let ((?x83 (* (* 1.0 (- 8.0)) k_0_0)))
 (let ((?x119 (+ (- 2.0) ?x83 (* (* 1.0 4.0) k_1_0) (* (* 1.0 16.0) (^ k_1_0 2.0)))))
 (= ?x119 0.0))))
(assert
 (let ((?x83 (* (* 1.0 (- 8.0)) k_0_0)))
(let ((?x39 (+ (- 2.0) (* (* 1.0 (- 64.0)) (^ k_1_0 3.0)) ?x83 (* (* 1.0 28.0) k_1_0))))
(= ?x39 0.0))))
(check-sat)
