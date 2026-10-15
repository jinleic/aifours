; benchmark generated from python API
(set-info :status unknown)
(declare-fun a () Real)
(assert
 (> 2.0 0.0))
(assert
 (> (+ 2.0 (* (* 1.0 (- 2.0)) (^ a 2.0))) 0.0))
(assert
 (> 0.0 0.0))
(check-sat)
