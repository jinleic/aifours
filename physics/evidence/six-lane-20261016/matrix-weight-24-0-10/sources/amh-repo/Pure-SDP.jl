using JuMP, Combinatorics, ClusteredLowRankSolver, Infinity, LinearAlgebra, Dualization, Clarabel, Nemo
include("fun.jl")

function SDP_pure(n,K,d,f4,f2,N,z)
    y=[]

    for i in 0:n
        for j in 0:n
            for t in (i + j - n):min(i, j)
                for p in 0:t
                    dict_sum = Dict()
                    
                    for k in 0:min(i, j)
                        for a in (max(i, j) + k - n):k
                            if a >= 0                          
                                coeff=alpha_field(i, j, t, p, a, k, n, z)/gamma_field(i,j,t,p,n,z)

                                matrix = zero_matrix(N, n + a - 2*k+1, n + a - 2*k+1)
                                
                                matrix[i-k+1,j-k+1] = 1
                                dict_sum[(:Y,f2[a,k])] = Matrix(matrix*coeff)

                            end
                        end
                    end
                    
                    push!(y, dict_sum)
                    
                end
            end
        end
    end

    D=[]

    for i in 0:n
        
        D_dict=Dict()
        
        for j in 0:d-1
            D_dict[(:C1,j)]=[(2//1)^(-n)*K*Kw_field(j,i,n);;]
            D_dict[(:C2,j)]=[-(2//1)^(-n)*K*Kw_field(j,i,n);;]
        end
        
        push!(D, D_dict)
    end

    #const

    constraints = []

    Q_psd=[]


    for i in d:n
        
        Dict_Q_psd=mergewith(+, multi(y[f4[i,0,0,0]+1],2), y[f4[i,i,i,i]+1])

        Dict_Q_psd=mergewith(+, Dict_Q_psd, multi(D[i+1],-1)) 
        
        Dict_Q_psd=multi(Dict_Q_psd, 1//(2^n//K - 2))
        
        push!(Q_psd,Dict_Q_psd)
    end

    no_rep_key=[]
    all_sets=[]

    for (i, j, t, p) in keys(f4)
        if (t - p) % 2 == 0 && i+j-t-p >= d && i>=d && j>=d
        
            if (i, j, i + j - t - p, t-p) ∉ all_sets
                    
                perm=collect(permutations((i, j, i + j - t - p)))
                sets=[(a,b,c,t-p) for (a,b,c) in perm]
                
                append!(all_sets, sets)
                push!(no_rep_key,(i,j,t,p))

            end
        end
    end

    for (i,j,t,p) in no_rep_key
        
        total_psd=Dict()
        total_free=Dict()

        for (a, b, c, q) in keys(f4) 
        
            if t - p == c - q && [i, j, i + j - t - p] in collect(permutations((a, b, a + b - c - q)))

                total_psd=mergewith(+,total_psd,y[f4[a, b, c, q]+1])
                total_psd=mergewith(+,total_psd, Q_psd[a+b-c-q-d+1])
                        
            end
        end
        con = Constraint(0, total_psd, total_free)
        push!(constraints, con)
    end   

    #obj


    Dict_obj_psd=mergewith(+, D[1], Dict((:C1,0) => [-1;;],(:C2,0) => [1;;]))

    Dict_obj_psd=mergewith(+, Dict_obj_psd, multi(y[f4[0,0,0,0]+1],-1))

    Dict_obj_psd=mergewith(+, Dict(:v => [1;;]), multi(Dict_obj_psd,1))
    con = Constraint(1, Dict_obj_psd, Dict())
    push!(constraints, con)
    obj = Objective(1, Dict(:v => [-1;;]), Dict())

    problem = Problem(Maximize(obj), constraints)

    problem_highprecision = map(x->generic_embedding(x, g), problem)
    status, primalsol, dualsol = solvesdp(problem_highprecision)
    # status, primalsol, dualsol = solvesdp(problem_highprecision, prec=500,step_length_threshold= 10^-16, gamma=0.5)
    println([n,K,d])
    println(status)
    println(objvalue(problem_highprecision, dualsol))

    settings=RoundingSettings()

    _, exactsol = exact_solution(problem, primalsol,dualsol; FF=N, g=g, settings=settings)

    return exactsol
end

R, x = polynomial_ring(QQ, :x)
N, z = number_field(x^2 - 3, :z)
g = sqrt(big(3)) 

n,K,d=[6, 2, 3]

f4, size  = f4_fun(n)
f2, size2 = f2_fun(n)

exactsol=SDP_pure(n,K,d,f4,f2,N,z)

Y = [exactsol.matrixvars[(:Y, i)] for i in 0:size2-1]
C = [exactsol.matrixvars[(:C1,i)][1,1]-exactsol.matrixvars[(:C2,i)][1,1] for i in 0:d-1]

Yext=[exactsol.matrixvars[(:Y, i)] for i in 0:size2-1]

open("Solution.txt", "w") do io
     println(io, Y,C);
end