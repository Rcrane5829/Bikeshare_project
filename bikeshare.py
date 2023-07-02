import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
   
    while True:
        city=input("Enter the name of a city (chicago, new york city, or washington):").lower()
        if city in ['chicago', 'new york city', 'washington']:
            break
        else:
            print("Invalid input. Please enter a valid city name.")
   
    while True:
        month=input("Enter the name of a month (All, January, February, March, April, May, June ):").title()
        if month in ['All', 'January', 'February','March','April','May','June']:
            break
        else:
            print("Invalid input. Please enter a valid month.")

    
    while True:
        day=input("Enter the name of a day (all, monday, tuesday ,wednesday, thursday, friday, saturday, sunday ):").lower()
        if day in ['all', 'monday', 'tuesday','wednesday','thursday','friday','saturday', 'sunday']:
          break
        else:
         print("Invalid input. Please enter a valid day.")

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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month']=df['Start Time'].dt.month
    df['Day of Week'] = df['Start Time'].dt.day_name()

    # Apply filters for month and day if specified
    if month != 'All':
        df['month'] = df['Start Time'].dt.month
        month_num = ['January', 'February', 'March', 'April', 'May', 'June'].index(month) + 1
        df = df[df['month'] == month_num]
        

    if day != 'all':
        df = df[df['Day of Week'] == day.title()]


    return df


        
        
        
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month


    common_month= df['month'].mode()[0]

    print('The most common month is:', common_month)
    # TO DO: display the most common day of week

    common_day_of_week= df['Day of Week'].mode()[0]

    print('The most common day of the week is:', common_day_of_week)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour

    popular_hour = df['hour'].mode()[0]
    
    print('Most Popular Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station= df['Start Station'].mode()[0]

    print('The most commonly used start station is:', common_start_station)
    # TO DO: display most commonly used end station
    common_end_station= df['End Station'].mode()[0]

    print('The most commonly used end station is:', common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    Frequent_trip=df.groupby(['Start Station', 'End Station']).size().idxmax()
                          
    print('The most frequent combination of start station and end station trip is:', Frequent_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
        
    df['Start Time'] = pd.to_datetime(df['Start Time'])
        
    df['End Time'] = pd.to_datetime(df['End Time'])
      
    df['Travel Time'] = df['End Time'] - df['Start Time']
      
    T_T_time=df['Travel Time'].sum()
      
    print("The total Travel time is:",T_T_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Travel Time'].mean()

    print("The mean travel time is:", mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].unique()
    print("The display counts of user times is:",user_types)

    
    if 'Gender' in df:
        gender_column = df['Gender']
        genders=df['Gender'].unique()
        print("The display counts of gender is:",genders)
    # Perform actions using the gender_column
    else:
        print('Gender stats cannot be calculated because Gender does not appear in the dataframe')


    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        df['Birth Year'] = pd.to_numeric(df['Birth Year'], errors='coerce')

        earliest_birth_year = int(df['Birth Year'].min())
      
        print("Earliest birth year:", earliest_birth_year)
      
        most_recent_birth_year = int(df['Birth Year'].max())
      
        print("Most recent birth year:", most_recent_birth_year)
      
        most_common_birth_year = int(df['Birth Year'].mode()[0])
        print("Most common birth year:", most_common_birth_year)
    else:
       print('Birth year stats cannot be calculated because Birth Year does not appear in the dataframe')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    """ displays raw data upon request"""
    view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no?").lower()
    start_loc = 0
    while True:
        if(view_data =='yes'):
            print(df.iloc[start_loc:start_loc+5])
            start_loc += 5
            view_data = input("Do you wish to continue?: ").lower()
        elif view_data =='no':
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
            view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no?").lower()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

 
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() == 'yes':
            pass
        elif restart.lower() == 'no':
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
            restart = input('\nWould you like to restart? Enter yes or no.\n')

if __name__ == "__main__":
	 main()
