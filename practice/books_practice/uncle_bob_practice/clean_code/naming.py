"""
Page 19.
In this example he shows that naming can make the code reviel it's puropse by clear naming.
"""
# this naming is bad because it is implicit, I don't know what is "Them" and what is in "list1" etc.
# wtf is theList? this is too fucked
theList = [1,2,3,4,5,6,7,8,1]

def getThem():
    list1 = []
    for x in theList:
        if x == 4:
            list1.append(x)
    return list1

# this is good naming. I can derive a lot of informatino from names here.
game_board = [1,2,3,4,5,5]  # some cells here are "flagged" according to the book

def get_flagged_cells():
    flagged_cells = []
    for cell in game_board:
        if cell == 4:
            flagged_cells.append(x)
    return flagged_cells
