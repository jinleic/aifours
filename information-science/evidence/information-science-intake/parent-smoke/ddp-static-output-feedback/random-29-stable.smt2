(set-logic QF_NRA)
; benchmark generated from python API
(set-info :status unknown)
(declare-fun k_0_0 () Real)
(assert
 (= 2.0 0.0))
(assert
 (= 0.0 0.0))
(assert
 (= (+ 6.0 (* (* 1.0 (- 2.0)) k_0_0)) 0.0))
(assert
 (let ((?x270 (+ (* (* 1.0 (- 10.0)) (^ k_0_0 2.0)) (* (* 1.0 6.0) k_0_0))))
 (= ?x270 0.0)))
(assert
 (> (* (* 1.0 (- 5.0)) k_0_0) 0.0))
(assert
 (let ((?x350 (+ (* (* 1.0 (- 5.0)) (^ k_0_0 2.0)) (* (* 1.0 3.0) k_0_0))))
 (> ?x350 0.0)))
(assert
 (let ((?x606 (+ (* (* 1.0 (- 24.0)) (^ k_0_0 2.0)) (* (* 1.0 40.0) (^ k_0_0 3.0)))))
(> ?x606 0.0)))
(check-sat)
