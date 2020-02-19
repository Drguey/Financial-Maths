def effective_annual(nominal, frequency):
    ''' (num, int) -> num
    Takes a nominal interest rate (given in decimal form), and compounding frequency, then outputs the effective annual interest rate

    effective_annual(0.05, 12)
    >>> 0.051161897881732976
    '''
    return (1 + nominal / frequency) ** frequency - 1
