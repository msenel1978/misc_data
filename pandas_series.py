import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import code

def variable_correlation(variable1, variable2):
    '''
    Fill in this function to calculate the number of data points for which
    the directions of variable1 and variable2 relative to the mean are the
    same, and the number of data points for which they are different.
    Direction here means whether each value is above or below its mean.
    
    You can classify cases where the value is equal to the mean for one or
    both variables however you like.
    
    Each argument will be a Pandas series.
    
    For example, if the inputs were pd.Series([1, 2, 3, 4]) and
    pd.Series([4, 5, 6, 7]), then the output would be (4, 0).
    This is because 1 and 4 are both below their means, 2 and 5 are both
    below, 3 and 6 are both above, and 4 and 7 are both above.
    
    On the other hand, if the inputs were pd.Series([1, 2, 3, 4]) and
    pd.Series([7, 6, 5, 4]), then the output would be (0, 4).
    This is because 1 is below its mean but 7 is above its mean, and
    so on.
    '''
    num_same_direction = 0        # Replace this with your code
    num_different_direction = 0   # Replace this with your code
        
    var1_above_average = [variable1 >= variable1.mean()]
    var2_above_average = [variable2 >= variable2.mean()]

    #code.interact(local=locals())
    num_same_direction = (~np.logical_xor(var1_above_average, var2_above_average)).sum()
    num_different_direction = len(variable1) - num_same_direction
    return (num_same_direction, num_different_direction)

def reverse_a_name(name):
    split_name = name.split(" ")
    first_name = split_name[0]
    last_name = split_name[1]
    return last_name + ", " + first_name

def reverse_names(names):
    '''
    Fill in this function to return a new series where each name
    in the input series has been transformed from the format
    "Firstname Lastname" to "Lastname, FirstName".
    
    Try to use the Pandas apply() function rather than a loop.
    '''
    return names.apply(reverse_a_name)

def main():
    countries = ['Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda',
                 'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan',
                 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus',
                 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia']

    life_expectancy_values = [74.7,  75. ,  83.4,  57.6,  74.6,  75.4,  72.3,  81.5,  80.2,
                              70.3,  72.1,  76.4,  68.1,  75.2,  69.8,  79.4,  70.8,  62.7,
                              67.3,  70.6]

    gdp_values = [ 1681.61390973,   2155.48523109,  21495.80508273,    562.98768478,
                  13495.1274663 ,   9388.68852258,   1424.19056199,  24765.54890176,
                  27036.48733192,   1945.63754911,  21721.61840978,  13373.21993972,
                    483.97086804,   9783.98417323,   2253.46411147,  25034.66692293,
                   3680.91642923,    366.04496652,   1175.92638695,   1132.21387981]

    # Life expectancy and gdp data in 2007 for 20 countries
    life_expectancy = pd.Series(life_expectancy_values, index = countries)
    gdp = pd.Series(gdp_values, index = countries)

    # Change False to True for each block of code to see what it does

    # Accessing elements and slicing
    if False:
        print life_expectancy[0]
        print gdp[3:6]
        
    # Looping
    if False:
        for country_life_expectancy in life_expectancy:
            print 'Examining life expectancy {}'.format(country_life_expectancy)
            
    # Pandas functions
    if True:
        print life_expectancy.mean()
        print life_expectancy.std()
        print gdp.max()
        print gdp.sum()

    # Vectorized operations and index arrays
    if True:
        a = pd.Series([1, 2, 3, 4])
        b = pd.Series([1, 2, 1, 2])
      
        print a + b
        print a * 2
        print a >= 3
        print a[a >= 3]

    num_same_direction, num_different_direction =\
        variable_correlation(life_expectancy, gdp)
    print '# of countries with the same life expectancy',\
            ' and GDP profile {} and different profile {}'.\
            format(num_same_direction, num_different_direction)

    # Addition when indexes are the same
    if True:
        s1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
        s2 = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
        print s1 + s2

    # Indexes have same elements in a different order
    if True:
        s1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
        s2 = pd.Series([10, 20, 30, 40], index=['b', 'd', 'a', 'c'])
        print s1 + s2

    # Indexes overlap, but do not have exactly the same elements
    if True:
        s1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
        s2 = pd.Series([10, 20, 30, 40], index=['c', 'd', 'e', 'f'])
        #print (s1 + s2).dropna()
        print s1.add(s2, fill_value = 0)

    # Indexes do not overlap
    if True:
        s1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
        s2 = pd.Series([10, 20, 30, 40], index=['e', 'f', 'g', 'h'])
        print s1 + s2

    # Example pandas apply() usage (although this could have been done
    # without apply() using vectorized operations)
    if False:
        s = pd.Series([1, 2, 3, 4, 5])
        def add_one(x):
            return x + 1
        print s.apply(add_one)

    names = pd.Series([
        'Andre Agassi',
        'Barry Bonds',
        'Christopher Columbus',
        'Daniel Defoe',
        'Emilio Estevez',
        'Fred Flintstone',
        'Greta Garbo',
        'Humbert Humbert',
        'Ivan Ilych',
        'James Joyce',
        'Keira Knightley',
        'Lois Lane',
        'Mike Myers',
        'Nick Nolte',
        'Ozzy Osbourne',
        'Pablo Picasso',
        'Quirinus Quirrell',
        'Rachael Ray',
        'Susan Sarandon',
        'Tina Turner',
        'Ugueth Urbina',
        'Vince Vaughn',
        'Woodrow Wilson',
        'Yoji Yamada',
        'Zinedine Zidane'
    ])

    print reverse_names(names)

    # The following code reads all the Gapminder data into Pandas DataFrames. You'll
    # learn about DataFrames next lesson.

    path = './'
    employment = pd.read_csv(path + 'employment_above_15.csv', index_col='Country')
    female_completion = pd.read_csv(path + 'female_completion_rate.csv', index_col='Country')
    male_completion = pd.read_csv(path + 'male_completion_rate.csv', index_col='Country')
    life_expectancy = pd.read_csv(path + 'life_expectancy.csv', index_col='Country')
    gdp = pd.read_csv(path + 'gdp_per_capita.csv', index_col='Country')

    # The following code creates a Pandas Series for each variable for the United States.
    # You can change the string 'United States' to a country of your choice.

    employment_us = employment.loc['United States']
    female_completion_us = female_completion.loc['United States']
    male_completion_us = male_completion.loc['United States']
    life_expectancy_us = life_expectancy.loc['United States']
    gdp_us = gdp.loc['United States']

    # Uncomment the following line of code to see the available country names
    print employment.index.values

    # Use the Series defined above to create a plot of each variable over time for
    # the country of your choice. You will only be able to display one plot at a time
    # with each "Test Run".
    employment_us.plot()
    plt.show()
    female_completion_us.plot()
    plt.show()



if __name__ == "__main__":
    main()