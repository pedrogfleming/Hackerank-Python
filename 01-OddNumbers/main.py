# https://www.hackerrank.com/challenges/py-if-else/problem?isFullScreen=false
if __name__ == '__main__':

    # SOLUTION 4
    n = int(input().strip())
    if n % 2 == 0 and (n in range(2,6) or n in range(21,101)):
        print('Not Weird')
    else: print('Weird')

    # SOLUTION 2:
    # n = int(input().strip())
    # if (n % 2) != 0 or ((n % 2 == 0) and (n >= 6) and (n <= 20)):
    #     print("Weird")
    # else:
    #     print("Not Weird")

    # My solution:
    # n = int(input().strip())
    # even = n % 2 == 0
    # result = "Weird"
    # if even:
    #     if n >= 2:
    #         if n >= 6:
    #             if n > 20:
    #                 result = "Not Weird"
    #             else:
    #                 result = "Weird"
    #         else:
    #             result = "Not Weird"
    # print(result)

    # SOLUTION 3:

    # n = int(input().strip())
    # status = "Not Weird"
    # if n % 2 != 0 or (n % 2 == 0 and 5 < n < 21):
    #     status = "Weird"
    # print(status)





