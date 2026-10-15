(set-logic QF_NRA)
; benchmark generated from python API
(set-info :status unknown)
(declare-fun k_0_0 () Real)
(assert
 (= (+ 1.0 k_0_0) 0.0))
(assert
 (let ((?x99 (* 1.0 2.0)))
 (let ((?x252 (* ?x99 k_0_0)))
 (= (+ 2.0 ?x252 (* ?x99 (^ k_0_0 2.0))) 0.0))))
(assert
 (let ((?x99 (* 1.0 2.0)))
 (let ((?x252 (* ?x99 k_0_0)))
 (let ((?x83 (+ (- 2.0) ?x252 (* (* 1.0 4.0) (^ k_0_0 3.0)) (* (* 1.0 5.0) (^ k_0_0 2.0)))))
 (= ?x83 0.0)))))
(assert
 (> (+ 1.0 (* (* 1.0 (- 2.0)) k_0_0)) 0.0))
(assert
 (let ((?x246 (+ (* (* 1.0 (- 3.0)) k_0_0) (* (* 1.0 6.0) (^ k_0_0 2.0)))))
(> ?x246 0.0)))
(check-sat)
