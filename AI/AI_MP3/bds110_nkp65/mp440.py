import copy
flipList = []
'''
Compute the value brought by a given move by placing a new token for player
at (row, column). The value is the number of opponent pieces getting flipped
by the move. 

A move is valid if for the player, the location specified by (row, column) is
(1) empty and (2) will cause some pieces from the other player to flip. The
return value for the function should be the number of pieces hat will be moved.
If the move is not valid, then the value 0 (zero) should be returned. Note
here that row and column both start with index 0. 
'''
def get_move_value(state, player, row, column):
    flipped = 0
    temp = []
    global flipList
    flipList = []
    #it is p1's turn
    if player == 'B':
        p1 = 'B'
        p2 = 'W'
    else:
        p1 = 'W'
        p2 = 'B'
    size = len(state)
    if row>=size or column>=size or state[row][column] != ' ':
        return flipped
    
    count = 0
    #down the col
    for i in range(row+1, size):
        if state[i][column] == p2:
            count+=1
            temp.append([i,column])
        elif state[i][column] == p1:
            flipped+=count
            flipList.extend(temp)
            break
        else:
            break
    #print flipped
    
    temp = []
    count = 0
    #up the col
    for i in range(row-1, -1, -1):
        if state[i][column] == p2:
            count+=1
            temp.append([i,column])
        elif state[i][column] == p1:
            flipped+=count
            flipList.extend(temp)
            break
        else:
            break
    #print flipped
    
    temp = [] 
    count = 0
    #rightward in row
    for i in range(column+1, size):
        if state[row][i] == p2:
            count+=1
            temp.append([row,i])
        elif state[row][i] == p1:
            flipped+=count
            flipList.extend(temp)
            break
        else:
            break
    #print flipped
    
    temp = []
    count = 0
    #leftward in row
    for i in range(column-1, -1, -1):
        if state[row][i] == p2:
            count+=1
            temp.append([row,i])
        elif state[row][i] == p1:
            flipped+=count
            flipList.extend(temp)
            break
        else:
            break
    #print flipped
    
    temp = []
    count = 0
    #top-left diag
    x = row-1
    y = column-1
    while x>=0 and y>=0:
        if state[x][y] == p2:
            count+=1
            temp.append([x,y])
            x-=1
            y-=1
        elif state[x][y] == p1:
            flipped+=count
            flipList.extend(temp)
            break
        else:
            break
    #print flipped
    
    temp = []
    count = 0
    #top-right diag
    x = row-1
    y = column+1
    while x>=0 and y<size:
        if state[x][y] == p2:
            count+=1
            temp.append([x,y])
            x-=1
            y+=1
        elif state[x][y] == p1:
            flipped+=count
            flipList.extend(temp)
            break
        else:
            break
    #print flipped
    
    temp = []    
    count = 0
    #bottom-right diag
    x = row+1
    y = column+1
    while x<size and y<size:
        if state[x][y] == p2:
            count+=1
            temp.append([x,y])
            x+=1
            y+=1
        elif state[x][y] == p1:
            flipped+=count
            flipList.extend(temp)
            break
        else:
            break
    #print flipped
    
    temp = []
    count = 0
    #bottom-left diag
    x = row+1
    y = column-1
    while x<size and y>=0:
        if state[x][y] == p2:
            count+=1
            temp.append([x,y])
            x+=1
            y-=1
        elif state[x][y] == p1:
            flipped+=count
            flipList.extend(temp)
            break
        else:
            break
    #print flipped

    return flipped


'''
Execute a move that updates the state. A new state should be crated. The move
must be valid. Note that the new state should be a clone of the old state and
in particular, should not share memory with the old state. 
'''
def execute_move(state, player, row, column):
	 new_state = None
	 global flipList
	 if get_move_value(state, player, row, column) != 0:
	 	new_state = copy.deepcopy(state)
	 	new_state[row][column] = player
	 	#print('THIS IS THE FLIPLIST FOR NEWSTATE: ', flipList)
	 	for element in flipList:
	 		new_state[element[0]][element[1]] = 'B' if new_state[element[0]][element[1]]=='W' else 'W'
	 else:
	 	print ('INVALID ATTEMPT OF EXECUTE MOVE')
	 return new_state

'''
A method for counting the pieces owned by the two players for a given state. The
return value should be two tuple in the format of (blackpeices, white pieces), e.g.,

    return (4, 3)

'''
def count_pieces(state):
    blackpieces = 0
    whitepieces = 0
    size = len(state) 
    for i in range(0, size):
        for j in range(0, size):
            if state[i][j] == 'B':
                blackpieces+=1
            elif state[i][j] == 'W':
                whitepieces+=1
            else:
                continue
    return (blackpieces, whitepieces)

'''
Check whether a state is a terminal state. 
'''
def is_terminal_state(state, state_list = None):
    terminal = True
    size = len(state)
    for i in range(0, size):
        for j in range(0, size):
            if get_move_value(state, 'B', i, j) != 0 or get_move_value(state, 'W', i, j) != 0:
                terminal = False
            else:
                continue
    return terminal

'''
The minimax algorithm. Your implementation should return the best value for the
given state and player, as well as the next immediate move to take for the player. 
'''
def minimax(state, player):
	value = 0
	row = -1
	column = -1

	if( is_terminal_state(state) ):
		#global term_count
		#term_count+=1
		tup = count_pieces(state)
		paths.append( [(player, row, column)] )
		return (tup[0]-tup[1],row,column)

	moves = []
	for i in range(0,len(state)):
		for j in range(0,len(state)):
			if(get_move_value(state,player,i,j)>0):
				moves.append((i,j))
	if(len(moves)==0):
		if player=='B':
			next_move = minimax(state,'W')
		elif player=='W':
			next_move = minimax(state,'B')
		value = next_move[0]
		return (value, row, column)
	value = -10000000 if player=='B' else 10000000
	
	for mv_tup in moves:
		new_state = execute_move(state,player, mv_tup[0], mv_tup[1])
		if player=='B':
			next_move = minimax(new_state,'W')
			new_value = max(value, next_move[0])
			if new_value>value:
				if value!=-10000000:
					paths.pop(len(paths)-2)
				row, column = mv_tup
				value = new_value
			else:
				paths.pop()
		elif player=='W':
			next_move = minimax(new_state,'B')
			new_value = min(value, next_move[0])
			if new_value<value:
				if value!=10000000:
					paths.pop(len(paths)-2)
				row, column = mv_tup
				value = new_value
			else:
				paths.pop()
	paths[len(paths)-1].append((player, row, column))
	return (value, row, column)

'''
This method should call the minimax algorithm to compute an optimal move sequence
that leads to an end game. 
'''
paths = []
def full_minimax(state, player):
	value = 0
	move_sequence = []
	del paths[:]
	tup = minimax(state,player)
	value = tup[0]
	paths[0].reverse()
	#make_report(state)
	return (value, paths[0])

#term_count =0
#ab_truncate_count =0
def make_report(state):
	print "Optimal Terminal State"
	new_state = state
	for move in paths[0]:
		#for i in range(0, len(new_state)):
		#	print new_state[i]
		#print
		if(get_move_value(new_state,move[0],move[1],move[2])>0):
			new_state = execute_move(new_state,move[0],move[1],move[2])
	for i in range(0, len(new_state)):
		print new_state[i]
	print "Terminal states visited: " +str(term_count)
	print "Truncations: " +str(ab_truncate_count)

'''
The minimax algorithm with alpha-beta pruning. Your implementation should return the
best value for the given state and player, as well as the next immediate move to take
for the player. 
'''
def minimax_ab(state, player, alpha = -10000000, beta = 10000000):
	value = 0
	row = -1
	column = -1
	if( is_terminal_state(state) ):
		#global term_count
		#term_count+=1
		tup = count_pieces(state)
		paths.append( [(player, row, column)] )
		return (tup[0]-tup[1], row, column)

	moves = []
	for i in range(0,len(state)):
		for j in range(0,len(state)):
			if(get_move_value(state,player,i,j)>0):
				moves.append((i,j))
	if(len(moves)==0):
		if player=='B':
			next_move = minimax_ab(state,'W',alpha,beta)
		elif player=='W':
			next_move = minimax_ab(state,'B',alpha,beta)
		value = next_move[0]
		return (value, row, column)
	value = -10000000 if player=='B' else 10000000
	
	for mv_tup in moves:
		new_state = execute_move(state,player, mv_tup[0], mv_tup[1])
		#global ab_truncate_count
		if player=='B':
			next_move = minimax_ab(new_state,'W',alpha,beta)
			new_value = max(value, next_move[0])
			if not (new_value<beta):
				#ab_truncate_count+=1
				if value!=-10000000:
					paths.pop()
				value = max(value,new_value)
				return (value,row,column)
			alpha = max(alpha,new_value)
			if new_value>value:
				if value!=-10000000:
					paths.pop(len(paths)-2)
				row, column = mv_tup
				value = new_value
			else:
				paths.pop()
		elif player=='W':
			next_move = minimax_ab(new_state,'B',alpha,beta)
			new_value = min(value, next_move[0])
			if not(new_value>alpha):
				#ab_truncate_count+=1
				if value!=10000000:
					paths.pop()
				value = min(value,new_value)
				return (value,row,column)
			beta = min(beta,new_value)
			if new_value<value:
				if value!=10000000:
					paths.pop(len(paths)-2)
				row, column = mv_tup
				value = new_value
			else:
				paths.pop()

	paths[len(paths)-1].append((player, row, column))	
	return (value, row, column)

'''
This method should call the minimax_ab algorithm to compute an optimal move sequence
that leads to an end game, using alpha-beta pruning.
'''
def full_minimax_ab(state, player):
	value = 0
	move_sequence = []
	del paths[:]
	tup = minimax_ab(state,player)
	value = tup[0]
	paths[0].reverse()
	#make_report(state)
	return (value, paths[0])
