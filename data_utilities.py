import unicodecsv
import numpy as np
from datetime import datetime as dt
from collections import defaultdict


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
    return time_delta.days < 7 and time_delta.days >=0


def remove_free_trial_canceled(data, students):
    new_data = []

    for data_point in data:
        if data_point['account_key'] in students:
            new_data.append(data_point)

    return new_data

def find_paid_engagement_in_first_week(paid_engagement, students):
    first_week_paid_engagements = []

    for engagement_record in paid_engagement:
        account_key = engagement_record['account_key']
        join_date = students[account_key]
        engagement_record_date = engagement_record['utc_date']

        if within_one_week(join_date, engagement_record_date):
            first_week_paid_engagements.append(engagement_record)

    return first_week_paid_engagements

# Create a dictionary of grouped data by student.
# The keys are key_name, and the values are lists of grouped data.
def group_data(data, key_name):

    grouped_data = defaultdict(list)
    for data_point in data:
        key = data_point[key_name]
        grouped_data[key].append(data_point)

    return grouped_data

# Create a dictionary with the total minutes each student spent in the classroom during the first week.
# The keys are account keys, and the values are numbers (total minutes)
def sum_grouped_items(grouped_data, field_name):
    summed_data = {}

    for key, data_points in grouped_data.items():
        total = 0
        for data_point in data_points:
            total += data_point[field_name]
        summed_data[key] = total

    return summed_data

def describe_data(data):
    print('Mean: {}'.format(np.mean(data)))
    print 'Standard deviation:', np.std(data)
    print 'Minimum:', np.min(data)
    print('Maximum: {}\n'.format(np.max(data)))


# Find the student that spends max. minutes
def find_student_with_max_minutes(minutes_by_account):
    max_student = None
    max_minutes = 0
    
    for student, total_minutes in minutes_by_account.items():
        if total_minutes > max_minutes:
            max_minutes = total_minutes
            max_student = student

    #print max_minutes

    return max_student, max_minutes




