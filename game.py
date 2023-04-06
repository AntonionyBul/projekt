import random
from turtle import update
import keyboard  # pip install keyboard
import os

start_deck = list("""
---------------------
|    |    |    |    |
---------------------
|    |    |    |    |
---------------------
|    |    |    |    |
---------------------
|    |    |    |    |
---------------------
""")

deck = start_deck

nums = [[0 for _ in range(4)] for _ in range(4)]

def list_rat90(data, times=1):
    if times==0:
        return data
    rat_data = []
    for t in range(times):
        m = len(data)
        n = len(data[0])
        rev_data = data[:: -1]
        rat_data = [[rev_data[j][i] for j in range(m)]
                    for i in range(n)]
        data = rat_data
    return rat_data

def write_nums():
    global deck 
    
    deck = start_deck[:]
    for row in range(4):
        for col in range(4):
            if nums[row][col]:
                for i in range(len(str(nums[row][col]))):
                    deck[22 + (row * (22 *2)) + 1 + col * 5 + i] = str(nums[row][col])[i]

def add_num():
    global nums,deck
    if all([0 not in i for i in nums]):
        print("Game over")
        print(f"Your score is: {max(max(i) for i in nums)}")
    else:
        while True:
            row = random.choice(range(4))
            col = random.choice(range(4))
            if nums[row][col] == 0:
                nums[row][col] = random.choice([2,4])
                break

def move_row(row):
    new_row = []
    for i in row:
        if i!=0:
            new_row.append(i)
        row = new_row[:]
        last_num = -1
    for i in range(len(row)):
        if row[i] == last_num:
            row[i-1] = row[i] * 2
            row[i] = 0
            last_num = row[i]
        new_row = []
        for i in row :
            if i != 0:
                new_row.append(i)
    return new_row
    
def move(side):
    global c
    global nums
    global write_nums
    rot = {'w':[3,1],'d':[2,2],'s':[1,3],'a':[0,0]}
    nums = list_rat90(nums, rot[side][0])
    for col in range (len(nums)):
        c = move_row(nums[col]) + \
            [0 for _ in range(4 - len(move_row(nums[col])))]
        nums[col] = c
    nums = list_rat90(nums, rot[side][1])

def w():
    move("w")
    update()


    
def a():
    move("a")
    update()

    
def s():
    move("s")
    update()


def d():
    move("d")
    update()


def update():
    os.system("cls")
    add_num()
    write_nums()
    print()
    print("".join(deck))

keyboard.add_hotkey("w",w)
keyboard.add_hotkey("a",a)
keyboard.add_hotkey("s",s)
keyboard.add_hotkey("d",d)

update()
while True:
    input()