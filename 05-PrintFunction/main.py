# HackerRank : https://www.hackerrank.com/challenges/python-print/problem?isFullScreen=true
def printNums(max):
    for i in range(1, max+1):
        print(i, end='')


if __name__ == '__main__':
    n = int(input())
    printNums(n)

