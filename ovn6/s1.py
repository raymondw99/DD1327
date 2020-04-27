# coding: utf-8
def dna():          # uppgift 1
    return "^[ATGC]+$"

def sorted():       # uppgift 2
    return "^9*8*7*6*5*4*3*2*1*0*$"

def hidden1(x):     # uppgift 3
# Input x är strängen som vi vill söka efter.
    return "^.*" + x + ".*$"

def hidden2(x):     # uppgift 4
# Input x är strängen som vi vill söka efter.
    return "^.*" + ".*".join(x) + ".*$"

def equation():     # uppgift 5
    return "^[-+]?[0-9]+([-+*/][0-9]+)*(=[+-]?[0-9]+([-+*/][0-9]+)*)?$"

def parentheses():  # uppgift 6
    return ("^(\((\((\((\((\(\))*\))*\))*\))*\))+$")

def sorted3():      # uppgift 7
    return ("^[0-9]*(01[2-9]|[0-1]2[3-9]|[0-2]3[4-9]|[0-3]4[5-9]|[0-4]5[6-9]|[0-5]6[7-9]|[0-6]7[8-9]|[0-7]89)[0-9]*$")

from sys import stdin
import re

def main():
    def hidden1_test(): return hidden1('progp')
    def hidden2_test(): return hidden2('progp')
    tasks = [dna, sorted, hidden1_test, hidden2_test, equation, parentheses, sorted3]
    print('Skriv in teststrängar:')
    while True:
        line = stdin.readline().rstrip('\r\n')
        if line == '': break
        for task in tasks:
            result = '' if re.search(task(), line) else 'INTE ' 
            print('%s(): "%s" matchar %suttrycket "%s"' % (task.__name__, line, result, task()))
    

if __name__ == '__main__':
    main()
