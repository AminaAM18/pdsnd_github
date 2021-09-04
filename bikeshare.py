import time
import pandas as pd
import numpy as np
import datetime

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
    while True:
        city= input('Would you like to see data for Chicago, New York city, or Washington?\n').lower()
        while city not in CITY_DATA:
            city= input('Please enter a valid city name \n').lower()
        break

    while True:
        choice= input("Would you like to filter the data by month, day, or not at all?\n").lower()

        if choice=='month':
            while True:
                month=input("Which month - January, February, March, April, May, or June?\n").lower()
                while month not in ('january', 'february', 'march', 'april', 'may', 'june'):
                    month=input('pleeeeeeeeease enter a valid month name\n').lower()
                break
            day='all'
            break
            # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
        elif choice=='day':
            while True:
                day=input("Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?\n").lower()
                while day not in ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'Saturday', 'sunday'):
                    day=input('pleeeeeeeeeease enter a valid day name\n').lower()
                break
            month='all'
            break
        elif choice=='not at all':
                month='all'
                day='all'
                break
        else:
            print('innnnnvalid input, pleeeeeease enter a valid answer\n')
    return city, month, day

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

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print('the most common month: \n', most_common_month)

    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print('the most common day of week: \n', most_common_day)

    # TO DO: display the most common start hour
    df['hour']=df['Start Time'].dt.hour
    most_common_hour = df['hour'].mode()[0]
    print('the most common start hour: \n', most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start=df['Start Station'].mode()[0]
    print('The most commonly used start station : \n',most_common_start)

    # TO DO: display most commonly used end station
    most_common_end=df['End Station'].mode()[0]
    print('The most commonly used end station :\n',most_common_end)

    # TO DO: display most frequent combination of start station and end station trip
    most_frenquent_comb=df.groupby(['Start Station', 'End Station']).size().nlargest(1)
    print('the most frequent combination of start station and end station trip: \n',most_frenquent_comb)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel=df['Trip Duration'].sum()
    print('Total travel time is: ',str(datetime.timedelta(seconds=int(total_travel))))

    # TO DO: display mean travel time
    mean_travel=df['Trip Duration'].mean()
    print('Mean travel time is: ',str(datetime.timedelta(seconds=mean_travel)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type=df['User Type'].value_counts()
    print('Counts of user types: \n',user_type)
    # TO DO: Display counts of gender
    if "Gender" in df.columns:
        gender=df['Gender'].value_counts()
        print('Counts of gender: \n',gender)

    # TO DO: Display earliest, most recent, and most common year of birth
        recent_birth= df['Birth Year'].max()
        print('most recent year of birth: \n',recent_birth)

        earliest_birth=df['Birth Year'].min()
        print('earliest year of birth:\n', earliest_birth)

        most_common_birth= df['Birth Year'].mode()[0]
        print('most common year of birth: \n', most_common_birth)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_data(df):
    view_data = input('Would you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
    start_loc = 0
    if view_data == 'yes':
        while True:
            print(df.iloc[start_loc:start_loc+5])
            start_loc += 5
            view_display = input('Do you wish to continue?: ').lower()
            if view_display != 'yes':
                break



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
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
