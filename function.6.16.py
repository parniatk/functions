#(Number of days in a year)

import calendar

def count_days_in_years(start_year, end_year):

    for year in range(start_year, end_year + 1):

        days_in_year = 366 if calendar.isleap(year) else 365
        
        print(f"Year {year} has {days_in_year} days.")

count_days_in_years(2010, 2020)