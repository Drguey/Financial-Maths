import bs4
import requests

def get_yield():
    '''(noneType) -> float
    Scrapes 10 year australian government yield from tradingeconomics site

    get_yield()
    >>>
    '''
    yield_url = "https://tradingeconomics.com/australia/government-bond-yield"
    r1 = requests.get(yield_url)
    soup = bs4.BeautifulSoup(r1.text, features="html.parser")
    g_yield = soup.find_all('td', {'id' : 'p'})[0].get_text(strip=True)
    return float(g_yield)

def cash_rate():
    ''' (noneType) -> float
    Scrapes Australian Cash Rate from RBA

    cash_rate()
    >>>
    '''
    cash_rate_url = "https://www.rba.gov.au/statistics/cash-rate/"
    r2 = requests.get(cash_rate_url)
    soup2 = bs4.BeautifulSoup(r2.text, features="html.parser")
    g_cash_rate = soup2.find_all("tbody")[0].get_text(strip=True)
    return float(g_cash_rate[14:18])

def discount_rate():
    ''' (noneType) -> float
    Calls on get_yield() and cash_rate() and returns the larger of the two to provide a conservative yield rate

    discount_rate()
    >>>
    '''
    global r
    r = max(get_yield(), cash_rate()) / 100
    return r
