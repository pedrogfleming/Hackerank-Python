# HackrRank: https://www.hackerrank.com/challenges/write-a-function/problem?isFullScreen=true

def is_leap(year):
    leap = False

    # Write your logic here
    # SOLUTION 1
    # return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    # My solution
    # if year % 4 == 0:
    #     if year % 100 == 0:
    #         if year % 400 == 0:
    #             leap = True
    #     else:
    #         leap = True
    # return leap


if __name__ == '__main__':
        # year = int(input())

    print(f"2000 its a leap year - Result: {is_leap(2000)}")
    print(f"2400 its a leap year - Result: {is_leap(2400)}")
    print(f"1800 is not a leap year - Result: {is_leap(1800)}")
    print(f"1900 is not a leap year - Result: {is_leap(1900)}")
    print(f"2100 is not a leap year - Result: {is_leap(2100)}")
    print(f"2200 is not a leap year - Result: {is_leap(2200)}")
    print(f"2300 is not a leap year - Result: {is_leap(2300)}")
    print(f"2500 is not a leap year - Result: {is_leap(2500)}")
