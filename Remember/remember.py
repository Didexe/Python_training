import sys
import os

def rememberer(thing):
    with open('database.txt', 'a') as file:
        file.write(thing + '\n')
        
def show():
    with open('database.txt') as file:
        for line in file:
            print(line)
            

    
if __name__ == '__main__':
    while True:
        choice = (input('What shall I do: '))
        if choice == 'r'.lower().strip():
            rememberer(input('What shoul I remember? '))
        if choice == '--list'.lower().strip():
            show()
        if choice == 'q':
            break