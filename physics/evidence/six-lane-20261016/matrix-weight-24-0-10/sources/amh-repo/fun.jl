# Multiplying Dict() for a constant

function multi(dic,cte)
    S=Dict()
    
    for k in keys(dic)
        S[k]=cte*dic[k]
    end 
    
    return S 
end 
# Mapping Functions 

function f4_fun(n) # (i,j,t,p) to a vector
    funct = Dict()
    size = 0
    for i in 0:n
        for j in 0:n
            for t in (i + j - n):min(i, j)
                for p in 0:t
                    funct[(i, j, t, p)] = size
                    size += 1
                end
            end
        end
    end
    return funct, size
end

function f2_fun(n) # (a,k) to a vector
    fun = Dict{Tuple{Int, Int}, Int}()
    count = 0
    for a in 0:n
        for k in a:div(n + a, 2)
            fun[(a, k)] = count
            count += 1
        end
    end
    return fun, count
end

# Combinatorial Functions

function comb(n, k)
    
    if n>=k && k>=0 && n>=0
        value=binomial(n,k)
    else
        value=0
    end
    
    return value
end

function beta(i, j, k, m, t)
    b = 0
    for u in 0:m
        b += comb(u, t) * comb(m - 2*k, u - k) * comb(m - k - u, i - u) * comb(m - k - u, j - u)*(-1)^(t - u)
    end
    return b
end

function multinomial_field(n,i,j,k,l,FF)

    value=FF^0*factorial(big(n))/(factorial(big(i))*factorial(big(j))*factorial(big(k))*factorial(big(l))*factorial(big(n-i-j-k-l)))
    return value
end

function gamma_field(i, j, t, p, n, FF)
    
    value = (big(3)//big(1))^(i + j - t) * (big(2)//big(1))^(t - p) *  multinomial_field(n, p, t - p, i - t, j - t, FF)
    return (value)

end

function alpha_field(i, j, t, p, a, k, n, FF)
    sum = 0
    for g in 0:p
        sum += (-1//1)^(a - g)*comb(a, g)*comb(t - a, p - g)*(2//1)^(t - a - p + g)
    end
    value=beta(i - a, j - a, k - a, n - a, t - a)*(FF^(i+j)/3^t)*sum
    return value
end

function Kw_field(m, k, n)
    sum = 0
    for alp in 0:n
        sum += z^0*(-1//1)^alp*comb(n-k, m-alp)*comb(k, alp)*(3//1)^(m-alp)
    end
    return sum
end

# Matrix Functions

function yijtp_fun_field(Y, n, f2, FF)
    yijkt = []
    for i in 0:n
        for j in 0:n
            for t in (i + j - n):min(i, j)
                for p in 0:t
                    y = 0
                    
                    for k in 0:min(i, j)
                        for a in (max(i, j) + k - n):k
                            if a >= 0
                                y += alpha_field(i, j, t, p, a, k, n, FF)*Y[f2[a, k]+1][i - k + 1, j - k + 1]
                            end
                        end
                    end
                    
                    push!(yijkt, y)
                    
                end
            end
        end
    end
    
    return yijkt
end

# LDL

function LDL(A,D) 

    d=Matrix(undef,D,1)
    d[1]=A[1,1]
    
    L=Matrix(undef,D,D)

    for j in 2:D
       
        for s in 1:j-1
    
            if s==1
                S=0
            else
                S=sum([L[j,p]*L[s,p]*d[p] for p in 1:s-1])
            end
    
            L[j,s]=(1//d[s])*(A[j,s] - S)
            
        end

        d[j]=A[j,j]-sum([L[j,k]^2*d[k] for k in 1:j-1])
    end
    
    return d
end

# A=Matrix([[2,4,-2,2] [4,9,-1,6] [-2,-1,14,13] [2,6,13,35]])
# D=length(A[1,:])
# # LDL(A,D)
