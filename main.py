import random
import time 

def dead_state(width, height):
	grid = [[0]* width for i in range(height)]

	return grid

def random_grid(grid): 
	val = 0
	for row in range(len(grid)):
		for elem in range(len(grid[row])):
			grid[row][elem] = random.randint(0,1)


def render_output(grid):
	ouput = {
	0 : ' ', 1 : u"\u2588" 
	}

	lines = []
	begin = ''
	end = ''
	for i in range(len(grid)):
		begin += '-'
	lines.append(begin)
	for row in range(len(grid)):
		line = '|'
		for elem in range(len(grid[row])):
			line += ouput[grid[row][elem]]
		line+= '|'
		lines.append(line)

	for i in range(len(grid)):
		end += '-'
	lines.append(end)

	return "\n".join(lines)

def next_state(grid):
	newgrid = dead_state(len(grid),len(grid[0]))
	circle = []
	for row in range(len(grid)):
		for elem in range(len(grid[row])):
			circle = calculate_circle(row,elem)
			numboflive = 0
			for position in circle:
				if grid[position[0]][position[1]]:
			 		numboflive += 1
			# print('row:',row,'elem:',elem)
			# print(numboflive)
			# print(circle)
			newgrid[row][elem]= rule_check(numboflive,grid[row][elem])
	return newgrid

def calculate_circle(row,elem):
	maxheight = len(grid)
	maxwidth = len(grid[0])

	circle = []

	if (row-1)>=0:
		circle.append([row-1,elem])
	if (row-1)>=0 and (elem+1)<maxwidth:
		circle.append([row-1,elem+1])
	if (elem+1) < maxwidth:
		circle.append([row,elem+1])
	if (row+1) < maxheight and (elem+1)<maxwidth:
		circle.append([row+1,elem+1])
	if (row+1) < maxheight:
		circle.append([row+1,elem])
	if (row+1)< maxheight and (elem-1)>=0:
		circle.append([row+1,elem-1])
	if (elem-1) >= 0 :
		circle.append([row,elem-1])
	if (row-1) >=0 and (elem-1)>=0:
		circle.append([row-1,elem-1])

	return circle

def rule_check(numboflive,cell):
	if cell:
		if numboflive <= 1:
			return 0
		elif numboflive >= 2 and numboflive <= 3:
			return 1
		else:
			return 0 
	else:
		if numboflive == 3:
			return 1
		else:
			return 0


#grid = dead_state(2,2)
#grid = [[0,1,0],[0,1,1],[1,1,0]]
grid = [[0,0,0,0,0,0],
[0,0,0,0,0,0],
[0,0,1,1,1,0],
[0,1,1,1,0,0],
[0,0,0,0,0,0],
[0,0,0,0,0,0]]
#random_grid(grid)
print(grid)
while(1):
	grid = next_state(grid)
	#print(grid)
	print(render_output(grid))
	time.sleep(0.03)
