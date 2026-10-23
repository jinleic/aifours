using JuMP, Combinatorics, ClusteredLowRankSolver, Infinity, LinearAlgebra, Dualization, Clarabel, Nemo
include("fun.jl")

function SDP_selfdual(n,d,f4,f2,N,z)
    
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


    # y=[]

    # for i in 0:n
    #     for j in 0:n
    #         for t in (i + j - n):min(i, j)
    #             for p in 0:t
    #                 dict_sum = Dict()
                    
    #                 for k in 0:min(i, j)
    #                     for a in (max(i, j) + k - n):k
    #                         if a >= 0
    #                             matrix = (zero_matrix(N, n + a - 2*k+1, n + a - 2*k+1))
    #                             matrix[i-k+1,j-k+1]=1
    #                             dict_sum[(:Y,f2[a,k])] = Matrix(matrix*alpha_field(i, j, t, p, a, k, n, z)
    #                                 /gamma_field(i,j,t,p,n,z))

    #                             # matrix=zeros(BigFloat, n + a - 2*k+1,  n + a - 2*k+1)
    #                             # matrix[i-k+1,j-k+1]=1
    #                             # dict_sum[(:Y,f2[a,k])] = Matrix(matrix*alpha(i, j, t, p, a, k, n)
    #                             #     *(2 - kron_delta(i, j))/gamma(i,j,t,p,n))
    #                         end
    #                     end
    #                 end
                    
    #                 push!(y, dict_sum)
                    
    #             end
    #         end
    #     end
    # end

    constraints = []

    # #const

    w=mergewith(+, multi(y[f4[n,0,0,0]+1],2), y[f4[n,n,n,n]+1])

    for i in d:n-1

        Dict_const1=mergewith(+, multi(y[f4[i,0,0,0]+1],2), y[f4[i,i,i,i]+1])
        Dict_const1=mergewith(+, multi(w,-1), Dict_const1)
        con = Constraint(0, Dict_const1, Dict())
        push!(constraints, con)
        
    end


    for (i, j, t, p) in keys(f4)
        if ((t - p) % 2 == 0 && i >= d && j >= d && i+j-t-p >= d && i>=j)
            con = Constraint(0, y[f4[i,j,t,p]+1] , Dict())
            push!(constraints, con)
        end
    end


    # obj

    Dict_obj=mergewith(+, multi(w,(2^n-1)), y[f4[0,0,0,0]+1])

    Dict_obj=mergewith(+, Dict(:v => [1;;]), multi(Dict_obj,-1))

    con = Constraint(1, Dict_obj , Dict())
    push!(constraints, con)


    obj = Objective(1, Dict(:v => [-1;;]), Dict())


    problem = Problem(Maximize(obj), constraints)

    problem_highprecision = map(x->generic_embedding(x, g), problem)

    status, primalsol, dualsol = solvesdp(problem_highprecision)
   
    println([n,d])
    println(status)
    println(objvalue(problem_highprecision, dualsol))

    settings=RoundingSettings()

    _, exactsol = exact_solution(problem, primalsol,dualsol; FF=N, g=g, settings=settings)

    return exactsol
end

R, x = polynomial_ring(QQ, :x)
N, z = number_field(x^2 - 3, :z)
g = sqrt(big(3)) 

n,d=[13, 5]

f4, size  = f4_fun(n)
f2, size2 = f2_fun(n)


exactsol=SDP_selfdual(n,d,f4,f2,N,z)

Y = [exactsol.matrixvars[(:Y, i)] for i in 0:size2-1]

open("Solution.txt", "w") do io
     println(io, Y);
end