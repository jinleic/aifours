(set-logic QF_NRA)
; benchmark generated from python API
(set-info :status unknown)
(declare-fun k_0_0 () Real)
(assert
 (= (+ 1.0 (* (* 1.0 2.0) k_0_0)) 0.0))
(assert
 (let ((?x18 (^ k_0_0 2.0)))
 (let ((?x531 (* 1.0 2.0)))
 (let ((?x76 (* ?x531 ?x18)))
 (= (+ (- 2.0) (* (* 1.0 (- 2.0)) k_0_0) ?x76) 0.0)))))
(assert
 (let ((?x18 (^ k_0_0 2.0)))
(let ((?x531 (* 1.0 2.0)))
(let ((?x76 (* ?x531 ?x18)))
(let ((?x47 (+ 3.0 ?x76 (* ?x531 (^ k_0_0 3.0)) (* (* 1.0 9.0) k_0_0))))
(= ?x47 0.0))))))
(check-sat)
