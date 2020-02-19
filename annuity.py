from interest_rates import effective_annual
def ordinary_annuity(rate, principal, payment, frequency, term):
    ''' (num, num, num, int, int) -> (num, num, num)
    Calculates the present and future value of an ordinary annuity given a rate of return, principal, payment, frequency of payments per year, and term of annuity in years.
    Rate of return given should be nominal per annum

    ordinary_annuity(0.05, 1000, 100, 12, 5)
    >>> (0.051161897881732976, 2892.9289525070117, 3712.6654774939466)
    '''
    effective_rate = effective_annual(rate, frequency)
    present_value = principal + payment * (1-(1+rate)**(-frequency * term))/(rate)
    future_value = present_value * (1 + effective_rate) ** term
    return (effective_rate, present_value, future_value)

def annuity_due(rate, principal, payment, frequency, term):
    ''' (num, num, num, int, int) -> (num, num, num)
    Calculates the present and future value of an annuity due given a rate of return, principal, payment, frequency of payments per year, and term of annuity in years.
    Rate of return given should be nominal per annum

    annuity_due(0.05, 1000, 100, 12, 5)
    >>> (0.051161897881732976, 2904.9828231424576, 3728.134916983505)
    '''
    effective_rate = effective_annual(rate, frequency)
    present_value = (principal + payment * (1 - (1 + rate) ** (-frequency * term)) / (rate)) * (1 + rate / frequency)
    future_value = present_value * (1 + effective_rate) ** term
    return (effective_rate, present_value, future_value)
