def sample_return(n):

    # sum = value + sum
    if( n!=1):
        return n * sample_return(n-1)
    else:
        return n
    
b = sample_return(4)
print(b)