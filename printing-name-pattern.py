for row in range(7):
    for col in range(5):
        #the indicated number in the range will be the designated number of characters in the output#
        if ((col==0 or col==4) and row!=0) or (row==0 or row==3) and ((col>0 and col<4)):
        #used conditions to where to put stars (asterisk) in columns and rows in the letter printed 
            print("*",end="")
            #the end string appends after the last value, default a newline because we wouldn't want a new line or empty space
        else:
            print(end=" ")
            #if the initial condition will not satisfy, it can print space then
    print()