##  Compare Triplets    ##

# Complete the Compare the Triplets function below.
# def solve(a, b):
#     count1 = count2 = 0
#     for idx, val in enumerate(a):
#         if val > b[idx]:
#             count1 += 1
#         elif val < b[idx]:
#             count2 += 1
#     return count1,count2
#
#
# if __name__ == '__main__':
#     a = map(int, raw_input().rstrip().split())
#
#     b = map(int, raw_input().rstrip().split())
#
#     result = solve(a, b)
#     print(result)


##  Plus Minus  ##

# Complete the plusMinus function below.
# def plusMinus(arr):
#     total = len(arr)
#     positive = filter(lambda x: x > 0, arr)
#     negative = filter(lambda x: x < 0, arr)
#     zero = filter(lambda x: x == 0, arr)
#     print("{0:.6f}".format(len(positive) / float(total)))
#     print("{0:.6f}".format(len(negative) / float(total)))
#     print("{0:.6f}".format(len(zero) / float(total)))
#
#
# if __name__ == '__main__':
#     n = int(raw_input())
#     arr = map(int, raw_input().rstrip().split())
#     plusMinus(arr)


##  Staircase   ##

# Complete the staircase function below.
# def staircase(n):
#     #### in java convert it in python ####
#     # int i, j, k;
#     # for (i = 5; i >= 1; i--) {
#     # for (j = 1; j < i; j++) {
#     # System.out.print(" ");
#     # }
#     # for (k = 5; k >= i; k--) {
#     # System.out.print("*");
#     # }
#     # System.out.println(); }
#
# if __name__ == '__main__':
#     n = int(raw_input())
#     staircase(n)


##  Max-Min  ##

# Complete the miniMaxSum function below.
# def miniMaxSum(arr):
#     a = arr[1] + arr[2] + arr[3] + arr[4]
#     b = arr[0] + arr[2] + arr[3] + arr[4]
#     c = arr[0] + arr[1] + arr[3] + arr[4]
#     d = arr[0] + arr[1] + arr[2] + arr[4]
#     e = arr[0] + arr[1] + arr[2] + arr[3]
#     print min(a, b, c, d, e), max(a, b, c, d, e)
#
#
# if __name__ == '__main__':
#     arr = map(int, raw_input().rstrip().split())
#
#     miniMaxSum(arr)


##  Birthday Cake Candles   ##

# Complete the birthdayCakeCandles function below.
# from collections import Counter

# def birthdayCakeCandles(ar):
#     data = Counter([int(item) for item in input().split()])
#     return max(data.values())
#
#
# if __name__ == '__main__':
#     ar_count = int(raw_input())
#     ar = map(int, raw_input().rstrip().split())
#     result = birthdayCakeCandles(ar)
#     print(result)


## Time Conversion  ##

# Complete the timeConversion function below.
# #
# def timeConversion(s):
#     if s[8:9] == 'P' or s[8:9] == 'p':
#         if s[:2] == '12':
#             return s[:8]
#         return str(int(s[:2]) + 12) + s[2:8]
#     elif s[8:9] == 'A' or s[8:9] == 'a':
#         if s[:2] == '12':
#             return '00' + s[2:8]
#         return s[:8]
#
# if __name__ == '__main__':
#     s = raw_input()
#     result = timeConversion(s)
#     print(result)


##  Coutning valleys ##

# Complete the countingValleys function below.
# def countingValleys(n, s):
#     sum = 0
#     count = 0
#     for val in s:
#         if val == 'D':
#             count = count - 1
#             if count == -1:
#                 sum += 1
#         elif val == 'U':
#             count = count + 1
#     return sum
#
# if __name__ == '__main__':
#     n = int(raw_input())
#     s = raw_input()
#     result = countingValleys(n, s)
#     print(result)


##  The Hurdle Race ##

# Complete the hurdleRace function below.
# def hurdleRace(k, height):
#     maxim = max(height)
#     if k < maxim:
#         return maxim - k
#     else:
#         return 0
#
# if __name__ == '__main__':
#     nk = raw_input().split()
#     n = int(nk[0])
#     k = int(nk[1])
#     height = map(int, raw_input().rstrip().split())
#     result = hurdleRace(k, height)
#     print(result)


## List Comprehensions ##

# if __name__ == '__main__':
#     x = int(input())
#     y = int(input())
#     z = int(input())
#     n = int(input())

#     print([[a,b,c] for a in range(x+1) for b in range(y+1) for c in range(z + 1) if ((a+b+c)!=n)])


## Find the Runner-Up Score! ##

if __name__ == '__main__':
    n = int(input())
    arr= map(int, input().split())

    a =sorted(arr)
    print(i for i in range(n+1) if a[i]>a[i+1])
    # for i in range(n):
    #     if a[i]>a[i+1]:
    #         print(a[i+1])
    #         break
