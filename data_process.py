from data_utilities import *
import matplotlib.pyplot as plt
import code

def main():

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

    print('Number of non-Udacity enrollments: {}'.format(len(non_udacity_enrollments)))
    print('Number of non-Udacity engaged students: {}'.format(len(non_udacity_engagement)))
    print('Number of non-Udacity project submitters: {}\n'.format(len(non_udacity_submissions)))

    # Paid students
    paid_students = find_paid_sudents(non_udacity_enrollments)
    print('Number of paid students: {}\n'.format(len(paid_students)))

    ## Create a list of rows from the engagement table including only rows where
    ## the student is one of the paid students you just found, and the date is within
    ## one week of the student's join date.
    paid_enrollments = remove_free_trial_canceled(non_udacity_enrollments, paid_students)
    paid_engagement = remove_free_trial_canceled(non_udacity_engagement, paid_students) 
    paid_submissions = remove_free_trial_canceled(non_udacity_submissions, paid_students)

    print('Number of paid enrollments: {}'.format(len(paid_enrollments)))
    print('Number of paid engagement: {}'.format(len(paid_engagement)))
    print('Number of paid submissions: {}\n'.format(len(paid_submissions)))

    # Add has_visited field
    for engagement_record in paid_engagement:
        if engagement_record['num_courses_visited'] > 0:
            engagement_record['has_visited'] = 1
        else:
            engagement_record['has_visited'] = 0

    paid_engagement_in_first_week = find_paid_engagement_in_first_week(paid_engagement,\
                                        paid_students)
    print('Number of paid engagements in first week: {}\n'.\
        format(len(paid_engagement_in_first_week)))

    # Analyze 'total_minutes_visited' data 
    engagement_by_account = group_data(paid_engagement_in_first_week, 'account_key')

    total_minutes_by_account = sum_grouped_items(engagement_by_account,\
                                    'total_minutes_visited')
    print('Stats of total_minutes_visited data')
    describe_data(total_minutes_by_account.values())

    student_with_max_minutes, max_minutes = find_student_with_max_minutes(total_minutes_by_account)
    print('Maximum Minutes: {}\n'.format(max_minutes))

    for engagement_record in paid_engagement_in_first_week:
        if engagement_record['account_key'] == student_with_max_minutes:
            print(engagement_record)

    
    # Analyze 'lessons_completed' data 
    total_lessons_completed_by_account = sum_grouped_items(engagement_by_account,\
                                                    'lessons_completed')
    print('\nStats of lessons_completed data')
    describe_data( total_lessons_completed_by_account.values())

    # Group data by has_visited
    days_visited_by_account = sum_grouped_items(engagement_by_account, 'has_visited')
    #Print stats of days visited
    print('Stats of days class visited')
    describe_data(days_visited_by_account.values())

    ###############################################################
    # Group the students into passing/non-passing on Subway Project
    subway_project_lesson_keys = ['746169184', '3176718735']
    # Passing engagements
    pass_subway_project = set()

    for submission in paid_submissions:
        project = submission['lesson_key']
        rating = submission['assigned_rating']

        #if project == subway_project_lesson_keys[0] or \
        #        project = subway_project_lesson_keys[1]
        if project in subway_project_lesson_keys and \
            (rating == 'PASSED' or rating == 'DISTINCTION'):
            pass_subway_project.add(submission['account_key'])

    #len(pass_subway_project)

    passing_engagement = []
    non_passing_engagement = []
    for engagement_record in paid_engagement_in_first_week:
        if engagement_record['account_key'] in pass_subway_project:
            passing_engagement.append(engagement_record)
        else:
            non_passing_engagement.append(engagement_record)
    print "\nPassing engagements:", len(passing_engagement)
    print('Non-Passing Engagement: {}\n'.format(len(non_passing_engagement)))

    # Group passing / non-passing by account
    passing_engagement_by_account = group_data(passing_engagement, 'account_key')
    non_passing_engagement_by_account = group_data(non_passing_engagement, 'account_key')

    # Stats of Passing / Not-passing Students: total_minutes_visited
    total_minutes_of_passing = sum_grouped_items(passing_engagement_by_account,\
                                                    'total_minutes_visited')
    print "\nStats: Total Minutes Spent for Passing"
    describe_data(total_minutes_of_passing.values())


    total_minutes_of_non_passing = sum_grouped_items(non_passing_engagement_by_account,\
                                                    'total_minutes_visited')
    print "\nStats: Total Minutes Spent for Non-Passing"
    describe_data(total_minutes_of_non_passing.values())

    # Stats of Passing / Not-passing Students: lessons_completed
    lessons_completed_of_passing = sum_grouped_items(passing_engagement_by_account,\
                                                    'lessons_completed')
    print "\nStats: Lessons Completed for Passing"
    describe_data(lessons_completed_of_passing.values())

    lessons_completed_of_non_passing = sum_grouped_items(non_passing_engagement_by_account,\
                                                    'lessons_completed')
    print "\nStats: Lessons Completed for Non-Passing"
    describe_data(lessons_completed_of_non_passing.values())

     # Stats of Passing / Not-passing Students: has_visited
    has_visited_of_passing = sum_grouped_items(passing_engagement_by_account,\
                                                    'has_visited')
    print "\nStats: has_sisted for Passing"
    describe_data(has_visited_of_passing.values())

    has_visited_of_non_passing = sum_grouped_items(non_passing_engagement_by_account,\
                                                    'has_visited')
    print "\nStats: has_sisted for Non-Passing"
    describe_data(has_visited_of_non_passing.values())

    plt.figure()
    plt.hist(has_visited_of_passing.values(), bins=8)
    plt.xlabel('Number of days')
    plt.title('Distribution of classroom visits in the first week ' + 
                'for students who pass the subway project')
    plt.show()

    plt.figure()
    plt.hist(has_visited_of_non_passing.values(), bins=8)
    plt.xlabel('Number of days')
    plt.title('Distribution of classroom visits in the first week ' + 
                'for students who do not pass the subway project')
    plt.show()
    #code.interact(local=locals())

if __name__ == "__main__":
    main()

