def general_poly (L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    #YOUR CODE HERE    

    def f(x):
        k = len(L)-1
        sum = 0
        for val in L:
            sum += val * (x**k)
            k -= 1
        return sum

    return f





r = general_poly([1, 2, 3, 4])(10)
print(r)