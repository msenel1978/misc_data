from data_utilities import *

if __name__ == "__main__":
    enrollments = read_csvfile('enrollments.csv') 
    print(enrollments[0])

    daily_engagement = read_csvfile('daily_engagement.csv')
    print(daily_engagement[0])

    project_submissions = read_csvfile('project_submissions.csv')
    print(project_submissions[0])

    # Clean up the data
    for enrollment in enrollments:
        enrollment['cancel_date'] = parse_date(enrollment['cancel_date'])
        enrollment['days_to_cancel'] = parse_maybe_int(enrollment['days_to_cancel'])
        enrollment['is_canceled'] = (enrollment['is_canceled'] == 'True')
        enrollment['is_udacity'] = (enrollment['is_udacity'] == 'True')
        enrollment['join_date'] = parse_date(enrollment['join_date'])

    print('\nData Processed - Enrollments:\n')
    print('Number of columns: {}\n'.format(len(enrollments)))
    print('Number of enrolled students: {}\n'.format(len(get_unique_students(enrollments))))
    print(enrollments[0])
    #print(unique_enrolled_students)

    # Clean up the data types in the engagement table
    for engagement_record in daily_engagement:
        engagement_record['lessons_completed'] = int(float(engagement_record['lessons_completed']))
        engagement_record['num_courses_visited'] = int(float(engagement_record['num_courses_visited']))
        engagement_record['projects_completed'] = int(float(engagement_record['projects_completed']))
        engagement_record['total_minutes_visited'] = float(engagement_record['total_minutes_visited'])
        engagement_record['utc_date'] = parse_date(engagement_record['utc_date'])
        engagement_record['account_key'] = engagement_record['acct']
        del engagement_record['acct']

    print('\nData Processed - Engagement:\n')
    print('Number of columns: {}\n'.format(len(daily_engagement)))

    unique_engagement_students = get_unique_students(daily_engagement)
    print('Number of engaged students: {}\n'.format(len(unique_engagement_students)))
    print(daily_engagement[0])

    # Clean up the data types in the submissions table
    for submission in project_submissions:
        submission['completion_date'] = parse_date(submission['completion_date'])
        submission['creation_date'] = parse_date(submission['creation_date'])
 
    print('\nData Processed - Submission:\n')
    print('Number of columns: {}\n'.format(len(project_submissions)))
    print('Number of project submitters: {}\n'.format(len(get_unique_students(project_submissions))))
    print(project_submissions[0])

    # Student missing in daily engagement
    num_problem_students = 0
    for enrollment in enrollments:
        student = enrollment['account_key']
        if (student not in unique_engagement_students) and \
            (enrollment['join_date'] != enrollment['cancel_date']):
           num_problem_students+=1
           print(enrollment)
            # Print only 10 of such students
            #if cnt == 10:
            #    break
    print('\nMissing students with days_to_cancel != 0: {}\n'.format(num_problem_students))

    # Udacity test accounts
    udacity_test_accounts = set()
    for enrollment in enrollments:
        if enrollment['is_udacity']:
            udacity_test_accounts.add(enrollment['account_key'])
    print('\nUdacity test accounts: {}\n'.format(len(udacity_test_accounts)))

    non_udacity_enrollments = remove_udacity_accounts(enrollments, udacity_test_accounts)
    non_udacity_engagement = remove_udacity_accounts(daily_engagement, udacity_test_accounts)
    non_udacity_submissions = remove_udacity_accounts(project_submissions, udacity_test_accounts)

    print('Number of non-Udacity enrollments: {}\n'.format(len(non_udacity_enrollments)))
    print('Number of non-Udacity engaged students: {}\n'.format(len(non_udacity_engagement)))
    print('Number of non-Udacity project submitters: {}\n'.format(len(non_udacity_submissions)))

