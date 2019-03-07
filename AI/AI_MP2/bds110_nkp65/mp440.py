import random

''' ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ '''
'''
                For Search Algorithms 
'''
''' ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ '''
queue=[]
'''
BFS add to queue 
'''
def add_to_queue_BFS(node_id, parent_node_id, cost, initialize=False):
    # Your code here
    global queue
    if(initialize):
    	queue = []
    	queue.insert(0,[node_id,parent_node_id])
    else:
    	queue.insert(0,[node_id,parent_node_id])
    return

'''
BFS add to queue 
'''
def is_queue_empty_BFS():
    # Your code here
    global queue
    if(len(queue)>0):
    	return False
    else:
    	return True

'''
BFS pop from queue
'''
def pop_front_BFS():
    # Your code here
    global queue
    (node_id, parent_node_id) = queue.pop()
    return (node_id, parent_node_id)

'''
DFS add to queue 
'''
def add_to_queue_DFS(node_id, parent_node_id, cost, initialize=False):
    # Your code here
    global queue
    if(initialize):
    	queue = []
    	queue.append([node_id,parent_node_id])
    else:
    	queue.append([node_id,parent_node_id])
    return

'''
DFS add to queue 
'''
def is_queue_empty_DFS():
    # Your code here
    global queue
    if(len(queue)>0):
    	return False
    else:
    	return True

'''
DFS pop from queue
'''
def pop_front_DFS():
	global queue
	(node_id, parent_node_id) = queue.pop()
	# Your code here
	return (node_id, parent_node_id)

'''
UC add to queue 
'''
def add_to_queue_UC(node_id, parent_node_id, cost, initialize=False):
    # Your code here
    global queue
    if(initialize):
    	queue = []
    queue.append([node_id,parent_node_id,cost])
    queue.sort(key=lambda x:x[2])
    return

'''
UC add to queue 
'''
def is_queue_empty_UC():
    # Your code here
    global queue
    if(len(queue)>0):
    	return False
    else:
    	return True

'''
UC pop from queue
'''
def pop_front_UC():
	# Your code here
	global queue
	queue=list(reversed(queue))
	(node_id, parent_node_id,cost) = queue.pop()
	return (node_id, parent_node_id)

'''
A* add to queue 
'''
def add_to_queue_ASTAR(node_id, parent_node_id, cost, initialize=False):
    # Your code here
    global queue
    if(initialize):
    	queue = []
    queue.append([node_id,parent_node_id,cost])
    queue.sort(key=lambda x:x[2])
    return

'''
A* add to queue 
'''
def is_queue_empty_ASTAR():
    # Your code here
    global queue
    if(len(queue)>0):
    	return False
    else:
    	return True

'''
A* pop from queue
'''
def pop_front_ASTAR():
   global queue
   queue=list(reversed(queue))
   (node_id, parent_node_id,cost) = queue.pop()
   return (node_id, parent_node_id)

''' ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ '''
'''
                For n-queens problem 
'''
''' ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ '''


'''
Compute a random state 
'''
def get_random_state(n):
    state = []
    for i in range(n):
        state.append(random.randint(1,n)) 
    return state

'''
Compute pairs of queens in conflict 
'''
def compute_attacking_pairs(state):
    number_attacking_pairs = 0
    i = 0
    while i<len(state)-1:
        j = i+1
        while j<len(state):
            if state[i] == state[j]:
                number_attacking_pairs+=1
            x_disp = j-i
            y_disp = abs(state[j] - state[i])
            if x_disp == y_disp:
                number_attacking_pairs+=1
            j+=1
        i+=1
    return number_attacking_pairs

'''
The basic hill-climing algorithm for n queens
'''
def hill_desending_n_queens(state, comp_att_pairs):
    final_state = []
    #board = [][]
    h = comp_att_pairs(state)
    print('this was the state: ',state)
    print('these are the pairs: ',h)
    best_move = 0
    best_move_row = state[0]
    best_move_col = 0
    min_h = h  
    i = 0
    while i<len(state):
        j = 0
        while j<len(state):
            statecopy = state[:]
            statecopy[j] = i+1
            new_h = comp_att_pairs(statecopy)
            if new_h < min_h:
                min_h = new_h
                best_move = 1
                best_move_row = j
                best_move_col = i+1    
            j+=1
        i+=1
    orig_state = state[:]
    if best_move == 1:
        state[best_move_row] = best_move_col 
    final_state = state
    if final_state == orig_state:
        return final_state
    else:
        return hill_desending_n_queens(final_state, comp_att_pairs)

''' 
Hill-climing algorithm for n queens with restart
'''
def n_queens(n, get_rand_st, comp_att_pairs, hill_descending):
    final_state = []
    h = 1
    while h != 0:
        state = get_rand_st(n)
        h = comp_att_pairs(hill_desending_n_queens(state, comp_att_pairs))
    final_state = state
    return final_state






