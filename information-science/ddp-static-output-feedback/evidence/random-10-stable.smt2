(set-logic QF_NRA)
; benchmark generated from python API
(set-info :status unknown)
(declare-fun k_0_0 () Real)
(assert
 (= (+ (- 2.0) (* (* 1.0 (- 4.0)) k_0_0)) 0.0))
(assert
 (let ((?x98 (+ 8.0 (* (* 1.0 (- 4.0)) (^ k_0_0 2.0)) (* (* 1.0 8.0) k_0_0))))
 (= ?x98 0.0)))
(assert
 (let ((?x45 (+ (* (* 1.0 (- 4.0)) (^ k_0_0 3.0)) (* (* 1.0 12.0) k_0_0) (* (* 1.0 16.0) (^ k_0_0 2.0)))))
 (= ?x45 0.0)))
(assert
 (let ((?x63 (* (* 1.0 (- 1.0)) k_0_0)))
 (> ?x63 0.0)))
(assert
 (let ((?x63 (* (* 1.0 (- 1.0)) k_0_0)))
(> (+ ?x63 (* (* 1.0 (- 2.0)) (^ k_0_0 2.0))) 0.0)))
(check-sat)
