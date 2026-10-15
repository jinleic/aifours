(set-logic QF_NRA)
; benchmark generated from python API
(set-info :status unknown)
(declare-fun k_0_0 () Real)
(assert
 (= (+ 1.0 k_0_0) 0.0))
(assert
 (let ((?x170 (* 1.0 2.0)))
 (let ((?x246 (* ?x170 k_0_0)))
 (= (+ 2.0 ?x246 (* ?x170 (^ k_0_0 2.0))) 0.0))))
(assert
 (let ((?x170 (* 1.0 2.0)))
(let ((?x246 (* ?x170 k_0_0)))
(let ((?x60 (+ (- 2.0) ?x246 (* (* 1.0 4.0) (^ k_0_0 3.0)) (* (* 1.0 5.0) (^ k_0_0 2.0)))))
(= ?x60 0.0)))))
(check-sat)
