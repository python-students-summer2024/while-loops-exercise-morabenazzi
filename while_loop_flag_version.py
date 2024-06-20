def sing(num_bottles):
    bottles = num_bottles
    singing = True
    while singing:
        if bottles > 2:
            print(str(bottles)+" bottles of beer on the wall, "+str(bottles)+" bottles of beer.\nTake one down, pass it around, "+str(bottles - 1)+" bottles of beer on the wall.\n")
        elif bottles == 2:
            print(str(bottles)+" bottles of beer on the wall, "+str(bottles)+" bottles of beer.\nTake one down, pass it around, "+str(bottles - 1)+" bottle of beer on the wall.\n")
        else:
            print(str(bottles)+" bottle of beer on the wall, "+str(bottles)+" bottle of beer.\nTake it down, pass it around, no more bottles of beer on the wall!\n")
            singing = False
        bottles -=1