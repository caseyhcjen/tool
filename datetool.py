import datetime as dt
import pandas as pd

def fmt2str(dt_val):
    """
    Convert a datetime obj to string 'YYYY-MM-DD HH:mm:SS'
    :rtype : str
    """
    if pd.isnull(dt_val):
        return 'NA'
    else:
        return dt_val.strftime('%Y-%m-%d %H:%M:%S') if isinstance(dt_val, dt.datetime) else 'NA'


def fmt2YMD(dt_val):
    """
    Convert a datetime obj to string 'YYYYMMDD'
    :rtype : str
    """
    return dt_val.strftime('%Y%m%d') if isinstance(dt_val, dt.datetime) else 'NA'


def fmt2Y_M_D(dt_val):
    """
    Convert a datetime obj to string 'YYYY-MM-DD'
    :rtype : str
    """
    return dt_val.strftime('%Y-%m-%d') if isinstance(dt_val, dt.datetime) else 'NA'


def parse(dt_str):
    """
    parse a string to datetime obj according to avaiable format string
    :rtype : datetime.datetime
    """
    timeTypeList = [
        "<class 'pandas.tslib.Timestamp'>", 
        "<class 'pandas._libs.tslib.Timestamp'>",
        "<type 'datetime.datetime'>",
    ]

    fmtList = [
        '%Y-%m-%d %H:%M:%S',  # 'YYYY-MM-DD HH:mm:SS'
        '%Y-%m-%d',
        '%Y%m%d',
        '%Y-%m-%d %H:%M:%S.0%f',
        '%m/%d/%Y',
        '%m/%d/%Y %H:%M',
    ]     

    result = None
    if dt_str and str(type(dt_str)) in timeTypeList:  
        result = dt_str  # already is datetime, for Pandas read SQL
    elif isinstance(dt_str, str):
        for fmt in fmtList:
            try:
                result = dt.datetime.strptime(dt_str, fmt)
                if result:
                    break                
            except ValueError:
                result = None
            except TypeError:
                # print("type({0}) = {1}".format(dt_str, str(type(dt_str))))
                result = None
    else:
        msg = '[{0}]({1}) will be treated as None ...'.format(dt_str, str(type(dt_str)))
        # raise TypeError(msg)
        # print("[WARN] : {0}".format(msg))
    return result


def fmt2HHMM(dt_val):
    return dt_val.strftime('%H:%M') if isinstance(dt_val, dt.datetime) else 'NA'


def days_hours_minutes(td):
    days, hours, minutes = td.days, td.seconds // 3600, td.seconds // 60 % 60
    return days, hours, minutes


def hours(td):
    days, hours, minutes = days_hours_minutes(td)
    total_hours = days * 24 + hours + minutes/ 60.
    return total_hours


def weekdayAsSQL(dt_val):
    """
    MS SQLServer -- datepart(WEEKDAY, convert(datetime, '1900-01-01')) -- Sun: 1, Mon: 2, ..., Sat: 7
    Python -- t.weekday() -- Sun: 6, Mon: 0, ..., Sat: 5
    """
    if isinstance(dt_val, dt.datetime):
        return 1 if (dt_val.weekday() + 2 == 8) else (dt_val.weekday() + 2)
    else:
        return None
