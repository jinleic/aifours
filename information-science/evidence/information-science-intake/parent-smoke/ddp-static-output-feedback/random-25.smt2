(set-logic QF_NRA)
; benchmark generated from python API
(set-info :status unknown)
(declare-fun k_0_0 () Real)
(assert
 (= 2.0 0.0))
(assert
 (= (+ 1.0 (* (* 1.0 (- 4.0)) k_0_0)) 0.0))
(assert
 (let ((?x467 (+ 4.0 (* (* 1.0 (- 16.0)) k_0_0) (* (* 1.0 32.0) (^ k_0_0 2.0)))))
 (= ?x467 0.0)))
(assert
 (let ((?x54 (+ (- 3.0) (* (* 1.0 (- 256.0)) (^ k_0_0 3.0)) (* (* 1.0 (- 22.0)) k_0_0) (* (* 1.0 176.0) (^ k_0_0 2.0)))))
(= ?x54 0.0)))
(check-sat)
