# SDP bounds on quantum codes: rational certificates

This repository complements the work from URL, which disproves the existence of $18$ qubit quantum codes with parameters $((n,K,\delta))_2$.

The proof consists of solving an SDP that yields infeasibility certificates on code existence: If the objective function of the solution is positive, the code does not exist.

The folder `cerf` includes all certificates for general, pure, and self-dual codes. Inside each folder, a file named $n$ _ $K$ _ $\delta$.jl contains an infeasible certificate of a code $((n,K,\delta))_2$.

All certificates are written in an algebraic field $\mathbb{Q}(\sqrt{3})$ using the package `Nemo.jl`, such that $z=\sqrt{3}$.

The files `General-readout.ipynb`, `Pure-readout.ipynb`, and `Selfdual-readout.ipynb` read the certificates and check if they satisfy the constraints for each type of code. For all the solutions, the objective function is $1$. The positive semidefinite conditions are checked by using the LDL-decomposition, which simplifies the problem on checking whether elements like $a+bz \in \mathbb{Q}(\sqrt{3})$ are positive. This can be done by approximating $\sqrt{3}$ by two rational numbers such that $r_\ell < \sqrt{3} < r_u$ with $r_u,r_\ell \in \mathbb{Q}$ and then,

1. if $b/a \geq 0$, $a+br_\ell \geq 0$ implies $a+b\sqrt{3} \geq 0$,
  
2. if $b/a \leq 0$, $a+br_u \geq 0$ implies $a+b\sqrt{3} \geq 0$.

3. if $a=0$, $b \geq 0$ implies $a+b\sqrt{3} \geq 0$.

The files `General-SDP.jl`, `Pure-SDP.jl`, and `Selfdual-SDP.jl` contain the SDP program used to find the exact feasibility certificates. They use the Julia package `ClusteredLowRankSolver.jl`, which is a high-precision primal-dual interior-point solver. This solver also provides a heuristic rounding functionality for extracting solutions over algebraic numbers. 

# Links

https://github.com/Nemocas/Nemo.jl

https://github.com/nanleij/ClusteredLowRankSolver.jl

