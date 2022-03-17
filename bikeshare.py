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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while (True):
        try:
            print('Enter a city from Chicago,New york city or Washington to start\n')
            city = input().lower()
            CITY_DATA[city]
            break     
        except Exception as e:
            print('INVALID ENTRY !')
    

    # TO DO: get user input for month (all, january, february, ... , june)
    while (True):
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        try:
            print( 'Enter a month from january, february, march, april, may, june\n' )
            month = input().lower()
            if month == 'all':
                break
            elif month != 'all':
                month = months.index(month) + 1
                break
        except Exception as e:
            print('INVALID ENTRY !' )
    

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while (True):
        days=['sunday','monday','tuesday','wednesday','thursday','friday','saturday']
        try:
            print( 'Enter a day from saturday,sunday,monday,tuesday,wednesday,thursday,friday\n' )
            day = input().lower()
            if day == 'all':
                break
            elif day in days:
                break
            else:
                print('INVALID ENTRY !' )
        except Exception as e:
            print('INVALID ENTRY !')



    
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
    df.rename( columns={'Unnamed: 0':'TRIP ID'}, inplace=True )

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    if month != 'all':
        df = df[ df['month'] == month ]

    if day != 'all':
        df = df[ df['day_of_week'] == day.title()]
    return df


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating the Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print(df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print(df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('The most commonly used start station: ',df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print('The most commonly used end station: ',df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    print('The most frequent combination of start station and end station trip: ',df[['Start Station','End Station']].mode().values)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    
    print('The most common Month: ',df['month'].mode()[0])

    # TO DO: display the most common day of week
    print('The most common Day of week: ',df['day_of_week'].mode()[0])

    # TO DO: display the most common start hour
    print('The most common Start hour: ',df['Start Time'].mode().dt.hour[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)




def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('The counts of user types is: ')
    print(df['User Type'].value_counts())

    # TO DO: Display counts of gender
    print('The count of gender is: ')
    try:
        print(df['Gender'].value_counts())
    except Exception:
        print('There is no gender')
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        print('The recent year of birth: ',df['Birth Year'].max() )
        print('The earliest year of birth: ',df['Birth Year'].min())
        print('The most common year of birth: ',df['Birth Year'].mode()[0])
    except Exception:
        print('There is no birth year')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    start = 0
    end = 10
    while(True):
        print("Do you want to display data Ten more rows of data please type yes or no")
        x = input().lower()
        if(x == 'yes'):
            try:
                print( df.iloc[ start:end ] )
            except Exception:
                print('There is no more data\n')
        else:
            break    
        end = end +5
        start = start +5

    
def main():
    while True:
        city, month, day = get_filters()
        print(city,month, day)
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        restart = input('\nDo you want to continue? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
if __name__ == "__main__":
	main()        