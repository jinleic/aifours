(set-logic QF_NRA)
; benchmark generated from python API
(set-info :status unknown)
(declare-fun k_0_0 () Real)
(assert
 (= (+ (- 2.0) k_0_0) 0.0))
(assert
 (let ((?x402 (+ (- 2.0) (* (* 1.0 (- 1.0)) (^ k_0_0 2.0)) (* (* 1.0 2.0) k_0_0))))
 (= ?x402 0.0)))
(assert
 (let ((?x157 (^ k_0_0 3.0)))
(let ((?x568 (+ 4.0 ?x157 (* (* 1.0 (- 1.0)) k_0_0) (* (* 1.0 (- 2.0)) (^ k_0_0 2.0)))))
(= ?x568 0.0))))
(check-sat)
