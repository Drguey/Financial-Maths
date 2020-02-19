def zcb(principal, rate, time_to_maturity):
    ''' (num, num, num) -> num
    Takes a principal and calculates the present value by discounting using simple interest.
    time_to_maturity is in years

    zcb(100, 0.05, 0.5)
    >>> 97.5609756097561
    '''
    present_value = principal / (1 + rate * time_to_maturity)
    return present_value
