# Problem: https://www.hackerrank.com/challenges/python-print/problem

# Given Code:
if __name__ == '__main__':
    n = int(input())

# Written Code:
print(*range(1, n+1), sep = "")

# The * tells the function to unpack the list and run itself on each element within the list

# The sep tells the function to separate the printed elements with anything with the " "