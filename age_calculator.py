import datetime


def winery_age_calc():
    today = datetime.datetime.now()
    now_year = today.year
    winery_age = now_year - 1920
    return winery_age
