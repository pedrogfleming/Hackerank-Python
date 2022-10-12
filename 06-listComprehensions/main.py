# HackerRank: https://www.hackerrank.com/challenges/list-comprehensions/problem
if __name__ == '__main__':
    # FROM https://www.youtube.com/watch?v=gAYRPL90Etg
    # SOLUTION :
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    s = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n]
    print(s)

    # SOLUTION 2
   # l=[]
   #  for a in range(x+1):
   #      for b in range(y+1):
   #          for c in range(z+1):
   #              if a+b+c!=n:
   #                  l.append([a,b,c])
   #  print(l)