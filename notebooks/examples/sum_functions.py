def iter_sum(end):
    """sums the numbers 1 to N :: iter"""
    sum_i = 0
    
    for i in range(int(end) + 1):
        sum_i += i
    
    return sum_i

def tri_sum(end):
    """
    sum of numbers from 1 to N :: triangle
    """    
    t_sum = end/2*(end + 1)
    
    return int(t_sum)

def cumul_sum(end, f=iter_sum):
    """calculates the cumulative sum for numbers 0 to M"""
    sum_list = []

    for n in range(end + 1):

        csum = f(n)

        sum_list.append(csum)

    return sum_list
