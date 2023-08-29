def find_maxima(x):
    """Find local maxima of x.

    Input arguments:
    x -- 1D list of real numbers

    Output:
    idx -- list of indices of the local maxima in x
    """
    maxima = []

    for index in range(1, len(x)-1):
        if x[index] > x[index-1] and x[index] > x[index+1]:
            maxima.append(index)

    return maxima
