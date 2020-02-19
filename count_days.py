#Packages such as FinDates already accomplish this, but this project showcases how it all works
#Date is in format (yyyy, m, d)
from datetime import date
def count_days(date1, date2):
    ''' (str, str) -> num
    Takes two input dates in the format 'dd/mm/yyyy' and returns number of days between the two dates.

    count_days('15/01/2020', '18/01/2020')
    >>> 3
    '''
    start_day = int(date1[0] + date1[1])
    start_month = int(date1[3] + date1[4])
    start_year = int(date1[6] + date1[7] + date1[8] + date1[9])
    end_day = int(date2[0] + date2[1])
    end_month = int(date2[3] + date2[4])
    end_year = int(date2[6] + date2[7] + date2[8] + date2[9])

    start_date = date(start_year,start_month,start_day)
    end_date = date(end_year, end_month, end_day)
    num_days = end_date - start_date
    return num_days.days