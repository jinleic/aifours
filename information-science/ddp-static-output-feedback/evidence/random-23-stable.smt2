(set-logic QF_NRA)
; benchmark generated from python API
(set-info :status unknown)
(declare-fun k_0_0 () Real)
(assert
 (= (+ 1.0 (* (* 1.0 2.0) k_0_0)) 0.0))
(assert
 (let ((?x556 (^ k_0_0 2.0)))
 (let ((?x531 (* 1.0 2.0)))
 (let ((?x40 (* ?x531 ?x556)))
 (= (+ (- 2.0) (* (* 1.0 (- 2.0)) k_0_0) ?x40) 0.0)))))
(assert
 (let ((?x556 (^ k_0_0 2.0)))
 (let ((?x531 (* 1.0 2.0)))
 (let ((?x40 (* ?x531 ?x556)))
 (let ((?x244 (+ 3.0 ?x40 (* ?x531 (^ k_0_0 3.0)) (* (* 1.0 9.0) k_0_0))))
 (= ?x244 0.0))))))
(assert
 (> (+ 2.0 (* (* 1.0 (- 1.0)) k_0_0)) 0.0))
(assert
 (let ((?x352 (+ 4.0 (* (* 1.0 (- 10.0)) k_0_0) (* (* 1.0 4.0) (^ k_0_0 2.0)))))
(> ?x352 0.0)))
(check-sat)
