# Hackerank Challenge: https://www.hackerrank.com/challenges/python-arithmetic-operators/problem?isFullScreen=true
if __name__ == '__main__':
    # a = int(input())
    # b = int(input())
    # SOLUTION 1
    a, b = map(int, [input(), input()])
    for operator in ['+', '-', '*']:
        print(eval(F'a{operator}b'))

    # SOLUTION 2
    a = [int(input()) for _ in range(2)]
    print(sum(a), a[0] - a[1], a[0] * a[1], sep='\n')
    # SOLUTION 3
    # print(a + b, a - b, a * b, sep="\n")

    # SOLUTION 4
    # print(f"{a + b}\n{a - b}\n{a * b}")

    # My solution
#     print(f"""{a+b}
# {a-b}
# {a*b}""")
