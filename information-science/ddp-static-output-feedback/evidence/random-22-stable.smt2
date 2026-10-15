(set-logic QF_NRA)
; benchmark generated from python API
(set-info :status unknown)
(declare-fun k_0_0 () Real)
(assert
 (= 0.0 0.0))
(assert
 (= (+ 4.0 (* (* 1.0 8.0) k_0_0)) 0.0))
(assert
 (let ((?x76 (+ 4.0 (* (* 1.0 24.0) k_0_0) (* (* 1.0 32.0) (^ k_0_0 2.0)))))
 (= ?x76 0.0)))
(assert
 (> (+ (- 1.0) (* (* 1.0 (- 4.0)) k_0_0)) 0.0))
(assert
 (let ((?x215 (+ (- 1.0) (* (* 1.0 (- 8.0)) (^ k_0_0 2.0)) (* (* 1.0 (- 6.0)) k_0_0))))
(> ?x215 0.0)))
(check-sat)
