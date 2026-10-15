; benchmark generated from python API
(set-info :status unknown)
(declare-fun a () Real)
(assert
 (> 1.0 0.0))
(assert
 (> (* (* 1.0 (- 2.0)) (^ a 2.0)) 0.0))
(assert
 (let ((?x74 (+ (* (* 1.0 (- 2.0)) (^ a 4.0)) (* (* 1.0 2.0) (^ a 2.0)))))
(> ?x74 0.0)))
(check-sat)
