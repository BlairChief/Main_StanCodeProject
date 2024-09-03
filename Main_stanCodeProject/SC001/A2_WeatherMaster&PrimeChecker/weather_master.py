"""
File: weather_master.py
Name: Blair
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
"""
EXIT = 2


def main():
    """
    Finding the highest and the lowest ones, computing the average,
    and counting the cold days among the temperatures entered.
    """
    print('stanCode \"Weather Master 4.0" !')
    n = int(input('Next Temperature: (or ' + str(EXIT) + ' to quit)?'))
    day = 0
    if n < 16:
        day += 1
    if n == EXIT:
        print('No temperatures were entered')
    else:
        highest = n
        lowest = n
        # to calculate average( = total/step)
        total = n
        step = 1
        n = int(input('Next Temperature: (or ' + str(EXIT) + ' to quit)?'))
        while n != EXIT:
            if n > highest:
                highest = n
            if n < lowest:
                lowest = n
            total = total + n
            if n < 16:
                day += 1
            n = int(input('Next Temperature: (or ' + str(EXIT) + ' to quit)?'))
            step += 1
        print('Highest temperature = ' + str(highest))
        print('Lowest temperature = ' + str(lowest))
        print('Average = ' + str(total / step))
        print(str(day) + ' cold(below 16) day(s)')


if __name__ == "__main__":
    main()
