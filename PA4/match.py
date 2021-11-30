# Programming Assignment 4
# Erin Maines
# e@uky.edu
# 5 December, 2021

import sys
import pdb

def lcs_length(X, Y): #using same vaules from the pseudocode
    m = len(X)
    n = len(Y)
    b = [0] * (m+1)
    c = [0] * (m+1)
    for x in range((m+1)):
        b[x] = [0] * (n+1)
        c[x] = [0] * (n+1)
    for i in range((m+1)):
        c[i][0] = 0
    for j in range((n+1)):
        c[0][j] = 0

    for i in range(1,m+1):
        for j in range(1,n+1):
            # Pointers:
            # ^ = up
            # \ = diagonal left
            # < = left
            if X[i-1] == Y[j-1]:
                c[i][j] = (c[i-1][j-1] + 1)
                b[i][j] = "\\" # Diagonal left
            elif c[i-1][j] >= c[i][j-1]:
                c[i][j] = c[i-1][j]
                b[i][j] = "^" #up
            else:
                c[i][j] = c[i][j-1]
                b[i][j] = "<" #left
    return(c, b)

def print_lcs(b, X, i, j): # b matrix, X string, starts from bottom right
    if i == 0 or j == 0:
        return()
    if b[i][j] == "\\": # diag left
        print_lcs(b, X, i-1, j-1)
        print(X[i-1])
    elif b[i][j] == "^": # up
        print_lcs(b, X, i-1, j)
    else:
        print_lcs(b, X, i, j-1)

def parse_str(file_name):
    lines = []
    with open(file_name, 'r') as line:
        text = line.read()
        text = text.split('\n')
        str1 = text[0]
        str2 = text[1]
    return(str1, str2)

def naive_string_matching(T,P):
    n = len(T)
    m = len(P)
    for s in range(n-m):
        return


def main():
    if sys.argv[1]:
        text_file = sys.argv[1]
        str1, str2 = parse_str(text_file)
        c, b = lcs_length(str1, str2)
        indx1 = len(str1) 
        indx2 = len(str2)
        breakpoint()
        print("Length of LCS is: ", (c[indx1][indx2]))
        print_lcs(b, str1, indx1, indx2)

if __name__ == "__main__":
    main()
