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

def remove_udacity_accounts(data, test_accounts):
    non_udacity_data = []
    for data_point in data:
        if data_point['account_key'] not in test_accounts:
        	non_udacity_data.append(data_point)
    return non_udacity_data

# Find paid students
def find_paid_sudents(enrollment_data):

    paid = {}

    for student in enrollment_data:
        if (student['days_to_cancel'] is None) or \
                        (student['days_to_cancel'] > 7):
            account_key = student['account_key']
            enrollment_date = student['join_date']

            if (account_key not in paid) or (enrollment_date > paid[account_key]):
                paid[account_key] = enrollment_date
    return paid

# Takes a student's join date and the date of a specific engagement record,
# and returns True if that engagement record happened within one week
# of the student joining.
def within_one_week(join_date, engagement_date):
    time_delta = engagement_date - join_date
    return time_delta.days < 7