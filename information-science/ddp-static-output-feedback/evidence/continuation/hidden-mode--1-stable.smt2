; benchmark generated from python API
(set-info :status unknown)
(declare-fun a () Real)
(assert
 (> 3.0 0.0))
(assert
 (> (+ 8.0 (* (* 1.0 (- 2.0)) (^ a 2.0))) 0.0))
(assert
 (let ((?x9 (+ 8.0 (* (* 1.0 (- 10.0)) (^ a 2.0)) (* (* 1.0 2.0) (^ a 4.0)))))
(> ?x9 0.0)))
(check-sat)
