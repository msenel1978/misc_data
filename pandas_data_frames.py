import pandas as pd

# Subway ridership for 5 stations on 10 different days
ridership_df = pd.DataFrame(
    data=[[   0,    0,    2,    5,    0],
          [1478, 3877, 3674, 2328, 2539],
          [1613, 4088, 3991, 6461, 2691],
          [1560, 3392, 3826, 4787, 2613],
          [1608, 4802, 3932, 4477, 2705],
          [1576, 3933, 3909, 4979, 2685],
          [  95,  229,  255,  496,  201],
          [   2,    0,    1,   27,    0],
          [1438, 3785, 3589, 4174, 2215],
          [1342, 4043, 4009, 4665, 3033]],
    index=['05-01-11', '05-02-11', '05-03-11', '05-04-11', '05-05-11',
           '05-06-11', '05-07-11', '05-08-11', '05-09-11', '05-10-11'],
    columns=['R003', 'R004', 'R005', 'R006', 'R007']
)

def mean_riders_for_max_station(ridership):
    '''
    Fill in this function to find the station with the maximum riders on the
    first day, then return the mean riders per day for that station. Also
    return the mean ridership overall for comparsion.
    
    This is the same as a previous exercise, but this time the
    input is a Pandas DataFrame rather than a 2D NumPy array.
    '''
    station_max_day_one = ridership.iloc[0].argmax()
    overall_mean = ridership.values.mean()
    mean_for_max = ridership[station_max_day_one].mean()
    
    return (overall_mean, mean_for_max)

def get_hourly_entries_and_exits(entries_and_exits):
    '''
    Fill in this function to take a DataFrame with cumulative entries
    and exits (entries in the first column, exits in the second) and
    return a DataFrame with hourly entries and exits (entries in the
    first column, exits in the second).
    '''

    return entries_and_exits - entries_and_exits.shift(periods = 1)

def convert_to_lettter_grade(grade):
  if (grade >= 90) and (grade <= 100):
    return 'A'
  if (grade >= 80) and (grade <= 89):
    return 'B'
  if (grade >= 70) and (grade <= 79):
    return 'C'
  if (grade >= 60) and (grade <= 69):
    return 'D'
  if (grade >= 0) and (grade <= 59):
    return 'F'
  

def convert_grades(grades):
    '''
    Fill in this function to convert the given DataFrame of numerical
    grades to letter grades. Return a new DataFrame with the converted
    grade.
    
    The conversion rule is:
        90-100 -> A
        80-89  -> B
        70-79  -> C
        60-69  -> D
        0-59   -> F
    '''
    return (grades.applymap(convert_to_lettter_grade))

def standardize_column (column):
  return (column - column.mean()) / column.std(ddof = 0)


def standardize(df):
    '''
    Fill in this function to standardize each column of the given
    DataFrame. To standardize a variable, convert each value to the
    number of standard deviations it is above or below the mean.
    '''
    
    return df.apply(standardize_column)
    
def convert_grades_curve(exam_grades):
    # Pandas has a bult-in function that will perform this calculation
    # This will give the bottom 0% to 10% of students the grade 'F',
    # 10% to 20% the grade 'D', and so on. You can read more about
    # the qcut() function here:
    # http://pandas.pydata.org/pandas-docs/stable/generated/pandas.qcut.html
    return pd.qcut(exam_grades,
                   [0, 0.1, 0.2, 0.5, 0.8, 1],
                   labels=['F', 'D', 'C', 'B', 'A'])

def main():
  # DataFrame creation
  if False:
      # You can create a DataFrame out of a dictionary mapping column names to values
      df_1 = pd.DataFrame({'A': [0, 1, 2], 'B': [3, 4, 5]})
      print df_1

      # You can also use a list of lists or a 2D NumPy array
      df_2 = pd.DataFrame([[0, 1, 2], [3, 4, 5]], columns=['A', 'B', 'C'])
      print df_2
     

  # Accessing elements
  if False:
      print ridership_df.iloc[0]
      print ridership_df.loc['05-05-11']
      print ridership_df['R003']
      print ridership_df.iloc[1, 3]
      
  # Accessing multiple rows
  if False:
      print ridership_df.iloc[1:4]
      
  # Accessing multiple columns
  if False:
      print ridership_df[['R003', 'R005']]
      
  # Pandas axis
  if False:
      df = pd.DataFrame({'A': [0, 1, 2], 'B': [3, 4, 5]})
      print df
      print df.sum()
      print df.sum(axis=1)
      print df.values.sum()

  mean_rider , mean_max_station = mean_riders_for_max_station(ridership_df)
  print "Overall mean: {}, mean rider of the station with max riders on day 1:{}".\
          format(mean_rider, mean_max_station)

  #Change False to True for each block of code to see what it does

  # Adding DataFrames with the column names
  if False:
      df1 = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]})
      df2 = pd.DataFrame({'a': [10, 20, 30], 'b': [40, 50, 60], 'c': [70, 80, 90]})
      print df1 + df2
      
  # Adding DataFrames with overlapping column names 
  if False:
      df1 = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]})
      df2 = pd.DataFrame({'d': [10, 20, 30], 'c': [40, 50, 60], 'b': [70, 80, 90]})
      print df1 + df2

  # Adding DataFrames with overlapping row indexes
  if False:
      df1 = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]},
                         index=['row1', 'row2', 'row3'])
      df2 = pd.DataFrame({'a': [10, 20, 30], 'b': [40, 50, 60], 'c': [70, 80, 90]},
                         index=['row4', 'row3', 'row2'])
      print df1 + df2

  # --- Quiz ---
  # Cumulative entries and exits for one station for a few hours.
  entries_and_exits = pd.DataFrame({
      'ENTRIESn': [3144312, 3144335, 3144353, 3144424, 3144594,
                   3144808, 3144895, 3144905, 3144941, 3145094],
      'EXITSn': [1088151, 1088159, 1088177, 1088231, 1088275,
                 1088317, 1088328, 1088331, 1088420, 1088753]
  })

  hourly_entries_exists = get_hourly_entries_and_exits(entries_and_exits)
  print hourly_entries_exists

  # DataFrame applymap()
  if True:
      df = pd.DataFrame({
          'a': [1, 2, 3],
          'b': [10, 20, 30],
          'c': [5, 10, 15]
      })
      
      def add_one(x):
          return x + 1
          
      print df.applymap(add_one)
      
  grades_df = pd.DataFrame(
      data={'exam1': [43, 81, 78, 75, 89, 70, 91, 65, 98, 87],
            'exam2': [24, 63, 56, 56, 67, 51, 79, 46, 72, 60]},
      index=['Andre', 'Barry', 'Chris', 'Dan', 'Emilio', 
             'Fred', 'Greta', 'Humbert', 'Ivan', 'James']
  )
  # DataFrame apply()
        
  # qcut() operates on a list, array, or Series. This is the
  # result of running the function on a single column of the
  # DataFrame.
  print "\n Applying qcut on exam1 column"
  print convert_grades_curve(grades_df['exam1'])
  
  # qcut() does not work on DataFrames, but we can use apply()
  # to call the function on each column separately
  print "\n Applying qcut on each column"
  print grades_df.apply(convert_grades_curve)

  print "\n Standardizing each column"
  print grades_df.apply(convert_grades_curve)

  print "Standardize Grades"
  print standardize(grades_df)


    
if __name__ == "__main__":
    main()