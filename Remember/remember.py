import sys
import os

def rememberer(thing):
    with open('database.txt', 'a') as file:
        file.write(thing + '\n')
        
def show():
    with open('database.txt') as file:
        for line in file:
            print(line)
            
def clear():
    with open('database.txt', 'w') as file:
        file.truncate()
        print('All clear')
    
if __name__ == '__main__':
    while True:
        choice = (input('What shall I do(r: add to list; l: show list; c: clear list; q: quit): '))
        if choice == 'r'.lower().strip():
            rememberer(input('What shoul I remember? '))
        if choice == 'l'.lower().strip():
            show()
        if choice == 'c'.lower().strip():
            clear()
        if choice == 'q':
            break
