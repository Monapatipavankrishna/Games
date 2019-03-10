def print_array(grid):
    for i in range(9):
        for j in range(9):
            print (grid[i][j],end='  ')
        print("\n") 



def row_(grid,row,num):
    for i in range(9):
        if grid[row][i]==num:
            return True
    return False
def col_(grid,col,num):
    for i in range(9):
        if grid[i][col]==num:
            return True
    return False
def box_(grid,row,col,num):
    for i in range(3):
        for j in range(3):
            if grid[i+row][j+col]==num:
                return True
        return False
def check_pos(grid,row,col,num):
    return not row_(grid,row,num) and not col_(grid,col,num) and not box_(grid,row-row%3,col-col%3,num)
def empty_space(grid,l):
    for row in range(9):
        for col in range(9):
            if grid[row][col]==0:
                l[0]=row
                l[1]=col
                return True
    return False
def sudoku_pro(grid):
    l=[0,0]
    if not empty_space(grid,l):
        return True
    row=l[0]
    col=l[1]
    for num in range(1,10):
        if check_pos(grid,row,col,num):
            grid[row][col]=num
            if sudoku_pro(grid):
                return True
            grid[row][col]=0
    return False


            
    
grid=[[0 for i in range(9)]for j in range(9)]
for i in range(9):
    for j in range(9):
        grid[i][j]=int(input())
for i in range(9):
    for j in range(9):
        print(grid[i][j],end='  ')
    print ("\n")
print(" ")
print(" ")    

if sudoku_pro(grid):
    print_array(grid)
else:
    print("solution does not exist:")
    
