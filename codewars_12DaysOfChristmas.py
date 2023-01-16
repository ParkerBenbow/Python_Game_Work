def song_sorter(lines):
    order = []
    number = 9
    x = 2
    while len(lines) > 0:
        for line in lines:
            if type(line[0]) == int:
                if line[0] == "1":
                    if line[1] == str(x):
                        order.append(line)
                        x = x - 1
                        lines.remove(line)
                elif line[0] == str(number):
                    order.append(line)
                    number = number - 1  
                    lines.remove(line)       
            elif line[0] == "O":
                order.insert(0,line)
                lines.remove(line)
            elif line[0] == "a":
                order.append(line)
                lines.remove(line)
    print(order)

lines = [ 
        "On the 12th day of Christmas my true love gave to me",
        "12 drummers drumming,",
        "11 pipers piping,",
        "10 lords a leaping,",
        "6 geese a laying,", 
        "9 ladies dancing,",
        "8 maids a milking,",
        "7 swans a swimming,", 
        "5 golden rings,", 
        "4 calling birds,",
        "3 French hens,", 
        "2 turtle doves and", 
        "a partridge in a pear tree." ] 

song_sorter(lines)
"""
Recieving the jumbled lines of the 12 Days of Christmas song, I need to return them in order
correct output should be:

On the 12th day of Christmas my true love gave to me
12 drummers drumming,
11 pipers piping, 
10 lords a leaping, 
9 ladies dancing, 
8 maids a milking,
7 swans a swimming, 
6 geese a laying, 
5 golden rings, 
4 calling birds,
3 French hens, 
2 turtle doves and 
a partridge in a pear tree.

"""