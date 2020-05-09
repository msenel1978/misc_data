import numpy as np

def max_employment(countries, employment):
    '''
    Fill in this function to return the name of the country
    with the highest employment in the given employment
    data, and the employment in that country.
    '''

    max_country = None      # Replace this with your code
    max_value = 0           # Replace this with your code

    for i in range(len(countries)):
        country_employment = employment[i]
        if country_employment > max_value:
            max_value = country_employment
            max_country = countries[i]
    
    #print 'Country with the highest emplyment {} has employment {}'.\
    #                                format(max_country, max_value)

    return (max_country, max_value)

def max_employment2(countries, employment):
    '''
    Using numpy argmax or max
    '''
    i = employment.argmax()

    return (countries[i], employment[i])

def overall_completion_rate(female_completion, male_completion):
    '''
    Fill in this function to return a NumPy array containing the overall
    school completion rate for each country. The arguments are NumPy
    arrays giving the female and male completion of each country in
    the same order.
    '''
    return ((female_completion + male_completion) / 2)

def standardize_data(values):
    '''
    Fill in this function to return a standardized version of the given values,
    which will be in a NumPy array. Each value should be translated into the
    number of standard deviations that value is away from the mean of the data.
    (A positive number indicates a value higher than the mean, and a negative
    number indicates a value lower than the mean.)
    '''
    return ((values - values.mean()) / values.std())

def mean_time_for_paid_students(time_spent, days_to_cancel):
    '''
    Fill in this function to calculate the mean time spent in the classroom
    for students who stayed enrolled at least (greater than or equal to) 7 days.
    Unlike in Lesson 1, you can assume that days_to_cancel will contain only
    integers (there are no students who have not canceled yet).
    
    The arguments are NumPy arrays. time_spent contains the amount of time spent
    in the classroom for each student, and days_to_cancel contains the number
    of days until each student cancel. The data is given in the same order
    in both arrays.
    '''
    
    return time_spent[days_to_cancel >= 7].mean()

def main():
    # First 20 countries with employment data
    countries = np.array([
        'Afghanistan', 'Albania', 'Algeria', 'Angola', 'Argentina',
        'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas',
        'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium',
        'Belize', 'Benin', 'Bhutan', 'Bolivia',
        'Bosnia and Herzegovina'
    ])

    # Employment data in 2007 for those 20 countries
    employment = np.array([
        55.70000076,  51.40000153,  50.5       ,  75.69999695,
        58.40000153,  40.09999847,  61.5       ,  57.09999847,
        60.90000153,  66.59999847,  60.40000153,  68.09999847,
        66.90000153,  53.40000153,  48.59999847,  56.79999924,
        71.59999847,  58.40000153,  70.40000153,  41.20000076
    ])

    # Change False to True for each block of code to see what it does

    # Accessing elements
    if False:
        print countries[0]
        print countries[3]

    # Slicing
    if False:
        print countries[0:3]
        print countries[:3]
        print countries[17:]
        print countries[:]

    # Element types
    if False:
        print countries.dtype
        print employment.dtype
        print np.array([0, 1, 2, 3]).dtype
        print np.array([1.0, 1.5, 2.0, 2.5]).dtype
        print np.array([True, False, True]).dtype
        print np.array(['AL', 'AK', 'AZ', 'AR', 'CA']).dtype

    # Looping
    if False:
        for country in countries:
            print 'Examining country {}'.format(country)

        for i in range(len(countries)):
            country = countries[i]
            country_employment = employment[i]
            print 'Country {} has employment {}'.format(country,
                    country_employment)

    # Numpy functions
    if True:
        print employment.mean()
        print employment.std()
        print employment.max()
        print employment.sum()

    #max_employment(countries, employment)
    max_employment_country, max_employment_rate = max_employment2(countries, employment)
    print 'Country with the highest employment {} has employment {}'.\
                                    format(max_employment_country, max_employment_rate)

    # Arithmetic operations between 2 NumPy arrays
    if False:
        a = np.array([1, 2, 3, 4])
        b = np.array([1, 2, 1, 2])
        
        print a + b
        print a - b
        print a * b
        print a / b
        print a ** b
        
    # Arithmetic operations between a NumPy array and a single number
    if False:
        a = np.array([1, 2, 3, 4])
        b = 2
        
        print a + b
        print a - b
        print a * b
        print a / b
        print a ** b
        
    # Logical operations with NumPy arrays
    if False:
        a = np.array([True, True, False, False])
        b = np.array([True, False, True, False])
        
        print a & b
        print a | b
        print ~a
        
        print a & True
        print a & False
        
        print a | True
        print a | False
        
    # Comparison operations between 2 NumPy Arrays
    if True:
        a = np.array([1, 2, 3, 4, 5])
        b = np.array([5, 4, 3, 2, 1])
        
        print a > b
        print a >= b
        print a < b
        print a <= b
        print a == b
        print a != b
        
    # Comparison operations between a NumPy array and a single number
    if True:
        a = np.array([1, 2, 3, 4])
        b = 2
        
        print a > b
        print a >= b
        print a < b
        print a <= b
        print a == b
        print a != b
        
    # First 20 countries with school completion data
    countries = np.array([
           'Algeria', 'Argentina', 'Armenia', 'Aruba', 'Austria','Azerbaijan',
           'Bahamas', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Bolivia',
           'Botswana', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi',
           'Cambodia', 'Cameroon', 'Cape Verde'
    ])

    # Female school completion rate in 2007 for those 20 countries
    female_completion = np.array([
        97.35583,  104.62379,  103.02998,   95.14321,  103.69019,
        98.49185,  100.88828,   95.43974,   92.11484,   91.54804,
        95.98029,   98.22902,   96.12179,  119.28105,   97.84627,
        29.07386,   38.41644,   90.70509,   51.7478 ,   95.45072
    ])

    # Male school completion rate in 2007 for those 20 countries
    male_completion = np.array([
         95.47622,  100.66476,   99.7926 ,   91.48936,  103.22096,
         97.80458,  103.81398,   88.11736,   93.55611,   87.76347,
        102.45714,   98.73953,   92.22388,  115.3892 ,   98.70502,
         37.00692,   45.39401,   91.22084,   62.42028,   90.66958
    ])

    print 'Overall completion rate (Male/Female ratio 1): {}'.\
            format(overall_completion_rate(female_completion, male_completion))

    # Change this country name to change what country will be printed when you
    # click "Test Run". Your function will be called to determine the standardized
    # score for this country for each of the given 5 Gapminder variables in 2007.
    # The possible country names are available in the Downloadables section.

    country_name = 'United States'

    print 'Standardized Employment Rate: {}'.format(standardize_data(employment))

    # Change False to True for each block of code to see what it does

    # Using index arrays
    if False:
        a = np.array([1, 2, 3, 4])
        b = np.array([True, True, False, False])
        
        print a[b]
        print a[np.array([True, False, True, False])]
        
    # Creating the index array using vectorized operations
    if False:
        a = np.array([1, 2, 3, 2, 1])
        b = (a >= 2)
        
        print a[b]
        print a[a >= 2]
        
    # Creating the index array using vectorized operations on another array
    if False:
        a = np.array([1, 2, 3, 4, 5])
        b = np.array([1, 2, 3, 2, 1])
        
        print b == 2
        print a[b == 2]

    # Time spent in the classroom in the first week for 20 students
    time_spent = np.array([
           12.89697233,    0.        ,   64.55043217,    0.        ,
           24.2315615 ,   39.991625  ,    0.        ,    0.        ,
          147.20683783,    0.        ,    0.        ,    0.        ,
           45.18261617,  157.60454283,  133.2434615 ,   52.85000767,
            0.        ,   54.9204785 ,   26.78142417,    0.
    ])

    # Days to cancel for 20 students
    days_to_cancel = np.array([
          4,   5,  37,   3,  12,   4,  35,  38,   5,  37,   3,   3,  68,
         38,  98,   2, 249,   2, 127,  35
    ])

    print 'Mean time spent of students enrolled >= 7 days: {}'.format(mean_time_for_paid_students(time_spent, days_to_cancel))

if __name__ == "__main__":
    main()