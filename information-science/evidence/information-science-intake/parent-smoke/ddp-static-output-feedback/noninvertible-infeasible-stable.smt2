(set-logic QF_NRA)
; benchmark generated from python API
(set-info :status unknown)
(declare-fun k_1_0 () Real)
(assert
 (= 0.0 0.0))
(assert
 (= 1.0 0.0))
(assert
 (= (- 1.0) 0.0))
(assert
 (= 1.0 0.0))
(assert
 (> (+ 6.0 (* (* 1.0 (- 1.0)) k_1_0)) 0.0))
(assert
 (let ((?x25 (+ 60.0 (* (* 1.0 (- 32.0)) k_1_0) (* (* 1.0 4.0) (^ k_1_0 2.0)))))
 (> ?x25 0.0)))
(assert
 (let ((?x137 (+ 360.0 (* (* 1.0 (- 372.0)) k_1_0) (* (* 1.0 (- 12.0)) (^ k_1_0 3.0)) (* (* 1.0 120.0) (^ k_1_0 2.0)))))
(> ?x137 0.0)))
(check-sat)
