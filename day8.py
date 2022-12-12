import numpy as np
# --- first part functions

def max_line_right(row,col)->int:
    max_line=-1
    while col+1<m:
        if max_line<grid[row,col+1]:
            max_line=grid[row,col+1]
        col+=1
    return int(max_line)

def max_col_up(row,col)->int:
    max_col=-1
    while row-1>=0:
        if max_col<grid[row-1,col]:
            max_col=grid[row-1,col]
        row-=1
    return int(max_col)
    
def max_line_left(row,col)->int:
    max_line=-1
    while col-1>=0:
        if max_line<grid[row,col-1]:
            max_line=grid[row,col-1]
        col-=1
    return int(max_line)

def max_col_down(row,col)->int:
    max_col=-1
    while row+1<n:
        if max_col<grid[row+1,col]:
            max_col=grid[row+1,col]
        row+=1
    return int(max_col)

# --- second part function

def part2_func(dir,row,col,h)->int:
    count=0
    if dir=='up':
        while row-1>=0:
            if grid[row-1,col]<h:
                count=count+1
            else:
                count=count+1
                return count
            row-=1
    elif dir=='down':
        while row+1<n:
            if grid[row+1,col]<h:
                count=count+1
            else:
                count=count+1
                return count
            row+=1
    elif dir=='right':
        while col+1<m:
            if grid[row,col+1]<h:
                count=count+1
            else:
                count=count+1
                return count
            col+=1
    elif dir=='left':
        while col-1>=0:
            if grid[row,col-1]<h:
                count=count+1
            else:
                count=count+1
                return count
            col-=1
    return count

n=99
m=99
grid=np.zeros((n,m))
with open('.\\txt files\\day8.txt','r') as f:
    row=0
    for i in f:
        cont=0
        i=i.strip()
        for cont in range(99):
            grid[row , cont] = int(i[cont])
        row+=1
    
    count=0
    max_score=-1

    for i in range(n):
        for j in range(m):
            h=int(grid[i,j])
            if i==0 or max_line_right(i,j)<h or max_line_left(i,j)<h or max_col_up(i,j)<h or max_col_down(i,j)<h or j==0:
                count+=1
                score=part2_func('up',i,j,h)*part2_func('down',i,j,h)*part2_func('left',i,j,h)*part2_func('right',i,j,h)
            if score>max_score:
                max_score=score
                
    print(count)
    print(max_score)
    f.close()
