from datetime import datetime
import pytz

# get the standard UTC time
UTC = pytz.utc

# it will get the time zone
# of the specified location
IST = pytz.timezone('Asia/Kolkata')

# print the date and time in
# standard format
print("UTC in Default Format : ",
      datetime.now(UTC))

print("IST in Default Format : ",
      datetime.now(IST))

# print the date and time in
# specified format
datetime_utc = datetime.now(UTC)
utc_date=datetime_utc.strftime('%Y:%m:%d %H:%M:%S %Z %z')
print(f"Date & Time in UTC {utc_date}")

datetime_ist = datetime.now(IST)
ist_date=datetime_ist.strftime('%Y:%m:%d %H:%M:%S %Z %z')
print(f"Date & Time in IST {ist_date}")



