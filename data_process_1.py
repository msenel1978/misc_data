import unicodecsv


def read_csvfile(filename):
    
    with open(filename, 'rb') as f:
        reader = unicodecsv.DictReader(f)
        return list(reader)




if __name__ == "__main__":
    enrollments = read_csvfile('enrollments.csv') 
    print(enrollments[0:3])

    daily_engagement = read_csvfile('daily_engagement.csv')
    print(daily_engagement[0:3])

    project_submissions = read_csvfile('project_submissions.csv')
    print(project_submissions[0:3]) 
