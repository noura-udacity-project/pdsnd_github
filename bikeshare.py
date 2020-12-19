## Python code
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

    while True:
        city = input("Please Enter a City Name (chicago, new york city, or washington):")
        city = city.lower().strip()
        if city in ["chicago", "new york city", "washington"]:
            # TO DO: get user input for month (all, january, february, ... , june)
            month = input('Enter a month:')
            month = month.lower().strip()
            if month != 'all':
                months = ['january', 'february', 'march', 'april', 'may', 'june']
                month = months.index(month) + 1

            
            # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
            day = input('Enter a Day:')
            day = day.lower().strip()
           
            return city, month, day
            # print('-'*40)
        else:
            print("City name is invalid")

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
    print("day is ", day)
    df = pd.read_csv(CITY_DATA[city])
    print("here")
    df["Start Time"] = pd.to_datetime(df["Start Time"], infer_datetime_format=True)
    print(df.dtypes)
   
    df["month"] = df["Start Time"].dt.month
    df["day"] = df["Start Time"].dt.day_name()

    df = df[(df["month"] == month) & (df["day"] == day.title())]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('Most common Month:', popular_month)

    # TO DO: display the most common day of week
    popular_day = df['day'].mode()[0]
    print('Common Day of Week:', popular_day)
    # TO DO: display the most common start hour
    df["start hour"] = df["Start Time"].dt.hour
    popular_hour = df["start hour"].mode()[0]

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    commonstart = df["Start Station"].mode()[0]


    # TO DO: display most commonly used end station
    commonend = df["End Station"].mode()[0]
    print("Commonend is ", commonend)
    

    # TO DO: display most frequent combination of start station and end station trip
def common_trip(df):
    """ Finds the mosy common combination of start station and end station"""
    start_time = time.time()
    df["common trip"] = df["Start Station"] + " " + df["End Station"]
    most_common_trip = df["common trip"].mode()[0]
    print("Most common trip ", most_common_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df["Trip Duration"].sum()

    # TO DO: display mean travel time
    mean_travel_time = df["Trip Duration"].mean()
    print("mean travel time is ", round(mean_travel_time,2))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types_count = df["User Type"]. value_counts()
    
    print(user_types_count)

    # TO DO: Display counts of gender
    try:
        gender = df["Gender"].value_counts()
        print(gender)
    except KeyError:
        pass

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_birth_year = df["Birth Year"].min()
        print(earliest_birth_year)
        most_recent_birth_year = df["Birth Year"].max()
        print(most_recent_birth_year)
        most_common_birth_year = df["Birth Year"].mode()[0]
        print(most_common_birth_year)
    except KeyError:
        pass
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        start = 0
        end = 5
        while True:
            raw_data = input("Would you like to view raw data?")
            if raw_data.lower() == "yes":
                print(df.iloc[start:end]) ## just read list slicing first
                start = end
                end += 5
                continue
            else:
                break
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        common_trip(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print("This session has ended")
            break

#
if __name__ == "__main__":
    main()
