import unicodecsv

enrollments = []

def read_csvfile():
    
    f = open('enrollments.csv', 'rb')

    reader = unicodecsv.DictReader(f)

    for row in reader:
        enrollments.append(row)

    f.close()

    print(enrollments[0:3])



if __name__ == "__main__":
    read_csvfile()
