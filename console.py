def console(payment, rate):
    ''' (num, num) -> num
    Takes a payment and rate of interest, returns the price (present value) of a consolidated stock
    console(100, 0.05)
    >>> 2000.0
    '''
    price = payment / rate
    return price