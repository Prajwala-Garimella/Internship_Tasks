# Problem 4 : Find a String
# HackerRank Link: https://www.hackerrank.com/challenges/find-a-string/problem

def mutate_string(string, position, character):
      return string[:position] + character + string[position + 1:]

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)