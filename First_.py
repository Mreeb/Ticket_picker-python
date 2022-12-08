import random
mary = int(input('Enter tickets for Mary: '))
joe = int(input('Enter tickets for Joe: '))
nate = int(input('Enter tickets for Nate: '))
total = mary+joe+nate
choice = input('D to Draw ticket or q to exit: ').upper()
std_list = [mary, joe, nate]
names = ["marry", "joe", "nate"]
while choice == 'D':
    draw = random.randint(1,total)
    start = 0
    stop = 0
    for i in range(len(std_list)):
        stop += std_list[i]
        if draw in range(start, stop):
            print("{} Wins!!!".format(names[i]))
            start = stop

    choice = input('Draw again or q to exit: ').upper()