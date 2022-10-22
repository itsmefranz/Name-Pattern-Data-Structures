def colored_text(r, g, b, text):
    return f"\033[38;2;{r};{g};{b}m{text}\033[0m"

print_d = [[" " for col_pattern in range(5)] for row_pattern in range(7)]
for row in range(7):
    for col in range(5):
        if (col==0) or (col==4 and (row!=0 and row!=6)) or ((row==0 or row==6) and (col>0 and col<4)):
            print_d[row][col] = "*"

print_a = [[" " for col_pattern in range(5)] for row_pattern in range(7)]
for row in range(7):
    for col in range(5):
        #the indicated number in the range will be the designated number of characters in the output#
        if ((col==0 or col==4) and row!=0) or (row==0 or row==3) and ((col>0 and col<4)):
        #used conditions to where to put stars (asterisk) in columns and rows in the letter printed 
            print_a[row][col] = "*"
            #the end string appends after the last value, default a newline because we wouldn't want a new line or empty space
        #else:
            #print(end=" ")
            #if the initial condition will not satisfy, it can print space then

print_n = [[" " for col_pattern in range(6)] for row_pattern in range(7)]
for row in range(7):
    for col in range(6):
        if col==0 or col==5 or (row==col and (col>0 and col<5)):
            print_n[row][col] = "*"

print_i = [[" " for col_pattern in range(5)]for row_pattern in range(7)]
for row in range(7):
    for col in range(5):
        if col == 2 or ((row == 0 or row == 6) and col != 2):
            print_i[row][col] = "*"           