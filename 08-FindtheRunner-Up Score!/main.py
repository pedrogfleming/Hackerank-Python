# HackerRank: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    # SOLUTION 1
    # scores = list(sorted(set(arr)))
    # print(scores[-2])

    # SOLUTION 2
    # arr = list(arr)
    # win_val = max(arr)
    #
    # while (max(arr)) == win_val:
    #     arr.remove(win_val)
    # print(max(arr))

    # My solution
    # arr = sorted(arr, reverse=True)
    # i = 1
    # for x in arr:
    #     if x != arr[i]:
    #         print(arr[i])
    #         break
    #     i += 1

