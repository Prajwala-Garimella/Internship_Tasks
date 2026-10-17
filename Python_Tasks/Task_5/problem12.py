# Problem 12: Capitalize!
# HackerRank Link: https://www.hackerrank.com/challenges/capitalize/problem


import os

def solve(s):
    words = s.split(' ')
    result = ' '.join(word[0].upper() + word[1:] if word else '' for word in words)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
