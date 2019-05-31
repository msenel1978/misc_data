import unicodecsv
from datetime import datetime as dt

# Reads the csv file
def read_csvfile(filename):
    
    with open(filename, 'rb') as f:
        reader = unicodecsv.DictReader(f)
        return list(reader)
# Takes a date as a string, and returns a Python datetime object. 
# If there is no date given, returns None
def parse_date(date):
    if date =='':
        return None
    else:
        return dt.strptime(date, '%Y-%m-%d')

# Takes a string which is either an empty string or represents an integer,
# and returns an int or None.
def parse_maybe_int(i):
    if i == '':
        return None
    else:
        return int(i)

def get_unique_students(data):
    unique_students = set()
    for student_record in data:
        unique_students.add(student_record['account_key'])

    return unique_students

