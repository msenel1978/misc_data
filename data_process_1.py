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

if __name__ == "__main__":
    enrollments = read_csvfile('enrollments.csv') 
    print(enrollments[0])

    daily_engagement = read_csvfile('daily_engagement.csv')
    print(daily_engagement[0])

    project_submissions = read_csvfile('project_submissions.csv')
    print(project_submissions[0])

    for enrollment in enrollments:
        enrollment['cancel_date'] = parse_date(enrollment['cancel_date'])
        enrollment['days_to_cancel'] = parse_maybe_int(enrollment['days_to_cancel'])
        enrollment['is_canceled'] = (enrollment['is_canceled'] == 'True')
        enrollment['is_udacity'] = (enrollment['is_udacity'] == 'True')
        enrollment['join_date'] = parse_date(enrollment['join_date'])

    print('\nData Processed - Enrollments:\n')
    print('Number of columns: {}\n'.format(len(enrollments)))
    print(enrollments[0])

    # Clean up the data types in the engagement table
    for engagement_record in daily_engagement:
        engagement_record['lessons_completed'] = int(float(engagement_record['lessons_completed']))
        engagement_record['num_courses_visited'] = int(float(engagement_record['num_courses_visited']))
        engagement_record['projects_completed'] = int(float(engagement_record['projects_completed']))
        engagement_record['total_minutes_visited'] = float(engagement_record['total_minutes_visited'])
        engagement_record['utc_date'] = parse_date(engagement_record['utc_date'])

    print('\nData Processed - Engagement:\n')
    print('Number of columns: {}\n'.format(len(daily_engagement)))
    print(daily_engagement[0])

    # Clean up the data types in the submissions table
    for submission in project_submissions:
        submission['completion_date'] = parse_date(submission['completion_date'])
        submission['creation_date'] = parse_date(submission['creation_date'])
 
    print('\nData Processed - Submission:\n')
    print('Number of columns: {}\n'.format(len(project_submissions)))
    print(project_submissions[0])
                            
