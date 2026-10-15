(set-logic QF_NRA)
; benchmark generated from python API
(set-info :status unknown)
(declare-fun k_0_0 () Real)
(assert
 (= 1.0 0.0))
(assert
 (= 1.0 0.0))
(assert
 (= (+ 8.0 (* (* 1.0 (- 16.0)) k_0_0)) 0.0))
(assert
 (> (+ (- 4.0) (* (* 1.0 4.0) k_0_0)) 0.0))
(assert
 (let ((?x247 (+ (- 32.0) (* (* 1.0 (- 64.0)) (^ k_0_0 2.0)) (* (* 1.0 96.0) k_0_0))))
(> ?x247 0.0)))
(check-sat)
