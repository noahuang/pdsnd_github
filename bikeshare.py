import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
#MONTH Dict
MONTH = {"all":0, "january":1, "february":2, "march":3 , "april":4 , "may":5 , "june":6 ,"july":7 , "august":8 , "september":9 , "october":10 , "november":11 , "december":12 }
#DAY Dict
DAY = {"all":7, "monday":1, "tuesday":2, "wednesday":3, "thursday":4 , "friday":5 , "saturday":6 , "sunday":0}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True :
        city  = input("Enter your city (chicago, new york city, washington): ").lower()
        if city not in CITY_DATA.keys():
            print('It is not a correct city!')  
        else : break
     
    # TO DO: get user input for month (all, january, february, ... , june)
    while True :
        month  = input("Enter the month (e.g. january) or all (no filter): ").lower()
        if month not in MONTH.keys():
            print('It is not a correct input!')  
        else : break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True :
        day  = input("Enter the day of week (e.g. monday) or all (no filter): ").lower()
        if day not in DAY.keys():
            print('It is not a correct input!')  
        else : break

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    df = pd.read_csv(CITY_DATA.get(city))
    if df.empty: print('no data in the csv file!')
    month = MONTH.get(month)
    day = DAY.get(day)
    df['Month'] = pd.DatetimeIndex(df['Start Time']).month
    df['Day'] = pd.DatetimeIndex(df['Start Time']).weekday
    df['Start Time Hour'] = pd.DatetimeIndex(df['Start Time']).hour
    df['Trip'] = 'from ' + df['Start Station'] + ' to ' + df['End Station']
    if month != 0:
        df = df[df.Month == month]
    else: df = df
    if day != 7:
        df = df[df.Day == day]
    else: df = df
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    month = df.loc[:,'Month'].value_counts().idxmax()
    month = {v:k for k,v in MONTH.items()}.get(month)
    print('\nThe Most Common Month is {}.\n'.format(month))
    
    # TO DO: display the most common day of week
    day = df.loc[:,'Day'].value_counts().idxmax()
    day = {v:k for k,v in DAY.items()}.get(day)
    print('\nThe most common day of week is {}.\n'.format(day))
    
    # TO DO: display the most common start hour
    start_hour = df.loc[:,'Start Time Hour'].value_counts().idxmax()
    print('\nThe most common start hour is {} o\'clock.\n'.format(start_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df.loc[:,'Start Station'].value_counts().idxmax()
    print('\nThe most common used start station is {}.\n'.format(start_station))

    # TO DO: display most commonly used end station
    end_station = df.loc[:,'End Station'].value_counts().idxmax()
    print('\nThe most common used end station is {}.\n'.format(end_station))

    # TO DO: display most frequent combination of start station and end station trip
    trip = df.loc[:,'Trip'].value_counts().idxmax()
    print('\nThe most frequent combination of start station and end station trip is {}.\n'.format(trip))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
   

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df.loc[:,'Trip Duration'].sum()
    print('\nThe total travel time is {} hours.\n'.format(np.around(total_travel_time/60/60,2)))

    # TO DO: display mean travel time
    total_travel_time = df.loc[:,'Trip Duration'].mean()
    print('\nThe mean travel time is {} minutes.\n'.format(np.around(total_travel_time/60,2)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('\nThe counts of user types is below:')
    print(df.loc[:,'User Type'].value_counts().to_string())
    print('\n')
    
    # TO DO: Display counts of gender
    print('\nThe counts of gender is below:')
    if 'Gender' in df.columns:
        print(df.loc[:,'Gender'].value_counts().to_string())
    else : print('No data in this city')
    print('\n')

    # TO DO: Display earliest, most recent, and most common year of birth
    print('\nThe earliest, most recent, and most common year of birth is below:')
    if 'Birth Year' in df.columns:
        earliest_birth = df.loc[:,'Birth Year'].min()
        most_recent_birth = df.loc[:,'Birth Year'].max()
        most_common_birth = df.loc[:,'Birth Year'].value_counts().idxmax()
        birth = {'Earliest birth year': int(earliest_birth),
                 'Most recent birth year': int(most_recent_birth),
                 'Most common birth year': int(most_common_birth)}
        birth = pd.DataFrame.from_dict(birth,orient='index',dtype=np.int)
        print(birth.loc[:,0].to_string())
    else : print('No data in this city')
    print('\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
        start_loc = 0
        while (view_data.lower() == 'yes'):
            print(df.iloc[start_loc:start_loc+5])
            start_loc += 5
            view_data = input('Do you wish to continue? Enter yes or no\n').lower()

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()