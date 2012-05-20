import datetime

def get_dates(start, n):
    period = datetime.timedelta(14) # Periods of two weeks
    fmt = '%Y%m%dT%H%M' # Match the format 20110507T1156
    start_dt = datetime.datetime.strptime(start, fmt)
    afters = []
    befores = []
    for i in range(n):
        afters.append(start_dt + i*period)
        befores.append(start_dt + (i + 1)*period)
    # Convert to strings
    afters = [d.strftime(fmt) for d in afters]
    befores = [d.strftime(fmt) for d in befores]
    return zip(afters, befores)
    

dts = get_dates('20110506T1125', 10)
print dts
