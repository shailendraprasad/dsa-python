def power(x, n):
    """computing the power using recursion"""
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)


print(power(2, 5))

"""
power(2,5) returns 2*16=32 
    power(2,4) returns 2*8=16
        power(2,3) returns 2*4=8
            power(2,2) returns 2*2=4
                power(2,1) returns 2*1=2
                    power(2,0) returns 1
"""