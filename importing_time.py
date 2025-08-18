from datetime import datetime

today = datetime.today()
print( 'Today Is: ' , today)

for attr in \
    [ 'year', 'month', 'day' , 'hour', 'minute', 'second', 'microsecond'] :
        print( attr , ':\t', getattr(today, attr))

day = today.strftime('%A')
month = today.strftime('%B')

print('Date:', day, month, today.day)