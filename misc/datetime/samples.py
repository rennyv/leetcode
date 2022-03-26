import datetime

def get_first_day_of_month(d):
    return d.replace(day=1)

def get_last_day_of_month(d):
    if d.month == 12:
        return d.replace(day=31)
    return d.replace(month=d.month+1, day=1) - datetime.timedelta(days=1)

def get_date_from_datetime(dt):
    return dt.date()

def get_days_from_beginning_of_month(d):
    fd = get_first_day_of_month(d)
    days = d - fd
    print(d, fd, days)
    return days.days + 1

def get_days_to_end_of_month(d):
    ld = get_last_day_of_month(d)
    days = ld - d
    return days.days + 1

def get_active_days_in(month, start, end):
    #this was a test question, given a month how many active days between, start and end, (end can be None)
    #month is "YYYY-MM" always present

    firstDay = datetime.datetime.strptime(month, "%Y-%m").date()
    lastDay = get_last_day_of_month(firstDay)
    
    #if end is not set, set it to the last day
    if not end:
        end = lastDay

    if start > end or end < firstDay:
        return 0

    if start > lastDay:
        return 0
    
    if end < lastDay:
        lastDay = end
    
    if start > firstDay:
        firstDay = start

    return (lastDay - firstDay).days + 1

def test_get_first_day_of_month():
    ans = datetime.date(2022,2,1)

    assert ans == get_first_day_of_month(datetime.date(2022,2,3))

    assert ans == get_first_day_of_month(datetime.date(2022,2,1))
    assert ans == get_first_day_of_month(datetime.date(2022,2,28))
    assert ans != get_first_day_of_month(datetime.date(2022,3,28))

def test_get_last_day_of_month():
    feb_2022_28 = datetime.date(2022,2,28)
    feb_2024_29 = datetime.date(2024,2,29)
    mar_2022_31 = datetime.date(2022,3,31)
    apr_2022_30 = datetime.date(2022,4,30)
    dec_2022_31 = datetime.date(2022,12,31)

    assert feb_2022_28 == get_last_day_of_month(datetime.date(2022,2,13))
    assert feb_2022_28 == get_last_day_of_month(datetime.date(2022,2,1))
    assert feb_2022_28 == get_last_day_of_month(datetime.date(2022,2,28))

    assert feb_2024_29 == get_last_day_of_month(datetime.date(2024,2,13))
    assert feb_2024_29 == get_last_day_of_month(datetime.date(2024,2,1))
    assert feb_2024_29 == get_last_day_of_month(datetime.date(2024,2,28))

    assert mar_2022_31 == get_last_day_of_month(datetime.date(2022,3,13))
    assert mar_2022_31 == get_last_day_of_month(datetime.date(2022,3,1))
    assert mar_2022_31 == get_last_day_of_month(datetime.date(2022,3,31))

    assert apr_2022_30 == get_last_day_of_month(datetime.date(2022,4,13))
    assert apr_2022_30 == get_last_day_of_month(datetime.date(2022,4,1))
    assert apr_2022_30 == get_last_day_of_month(datetime.date(2022,4,30))

    assert dec_2022_31 == get_last_day_of_month(datetime.date(2022,12,13))
    assert dec_2022_31 == get_last_day_of_month(datetime.date(2022,12,1))
    assert dec_2022_31 == get_last_day_of_month(datetime.date(2022,12,31))

def test_get_days_from_beginning_of_month():
    assert 13 == get_days_from_beginning_of_month(datetime.date(2022,2,13))
    assert 31 == get_days_from_beginning_of_month(datetime.date(2022,12,31))
    assert 1 == get_days_from_beginning_of_month(datetime.date(2022,12,1))

def test_get_days_to_end_of_month():
    assert 4 == get_days_to_end_of_month(datetime.date(2022,2,25))
    assert 28 == get_days_to_end_of_month(datetime.date(2022,2,1))
    assert 1 == get_days_to_end_of_month(datetime.date(2022,2,28))

def test_get_active_days_in():
    assert 31 == get_active_days_in("2022-05", datetime.date(2022, 4, 13), None)
    assert 2 == get_active_days_in("2022-05", datetime.date(2022, 5, 30), None)
    assert 31 == get_active_days_in("2022-05", datetime.date(2022, 4, 13), datetime.date(2022, 6, 13))
    assert 13 == get_active_days_in("2022-05", datetime.date(2022, 4, 13), datetime.date(2022, 5, 13))
    assert 2 == get_active_days_in("2022-05", datetime.date(2022, 5, 13), datetime.date(2022, 5, 14))
    assert 2 == get_active_days_in("2022-05", datetime.date(2022, 5, 30), datetime.date(2022, 6, 13))
    assert 1 == get_active_days_in("2022-05", datetime.date(2022, 5, 13), datetime.date(2022, 5, 13))
    assert 0 == get_active_days_in("2022-05", datetime.date(2022, 5, 16), datetime.date(2022, 5, 13))
    assert 0 == get_active_days_in("2022-05", datetime.date(2022, 6, 16), None)
    assert 0 == get_active_days_in("2022-05", datetime.date(2022, 4, 16), datetime.date(2022, 4, 18))