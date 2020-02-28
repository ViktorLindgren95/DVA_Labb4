#Fitness function should be something like #Stones_player - #stones_opponent
#Stones player shoud be depending on what player you are. IF playerturn 1 then you are player one and mancala is [6], else player 2 mancala [13]
import game_state as GS
import copy
def move_choice(board,player):
    if player == 1:
        player_num=1
        player_points=board[6]
        opp_points=board[13]
    else:
        player_num=2
        player_points=board[13]
        opp_points=board[6]


def minmax(player_num,board):
    player_number = player_num
    start_state = GS.game_state(player_num,board)
    start_state.calc_legal()
    #print(start_state.legal_moves)
    m=0
    move_v=-10000
    if len(start_state.legal_moves)>1:
        for move in start_state.legal_moves:
            next_state=copy.deepcopy(start_state)
            v=max_value(next_state.move(move),1,player_num) # Move function totally busted fix this, Its moving in general
            #print("Tested Move is ",move)
            #print("v is ",v)
            if v>move_v:
                m=move
                move_v=v


        start_state.move(m)
        if start_state.extra_turn == True:
            print("Extra Turn")
        m+=1
        print("Move is ",m)
        if m>7:
            m=m-7
        stuff_in_string = f'{m}'
        return stuff_in_string
    else:
        m=start_state.legal_moves[0]
        start_state.move(m)
        # if start_state.extra_turn == True:
        #     print("Extra Turn")
        m+=1
        print("Move is ",m)
        if m>7:
            m=m-7
        stuff_in_string = f'{m}'
        return stuff_in_string



def max_value(state,depth,global_player):
    if global_player == 1:
        state.player_num=1
    else:
        state.player_num=2
    if depth == 3: # this is our default ? use the depth here?
        return state.utility()
    v = -100000
    state.calc_legal()
    #print(state.legal_moves)
    for move in state.legal_moves:
        next_state=copy.deepcopy(state)
        tmp_depth=depth+1 # reduntant
        v=max(v, min_value(next_state.move(move), tmp_depth,global_player))
        #TODO om spelaren får en extra runda måste vi räkna med det också
    return v

def min_value(state,depth,global_player):
    if global_player == 1:
        state.player_num=2
    else:
        state.player_num=1
    if depth==3:
        return state.utility()
    v= 100000
    state.calc_legal()
    #print(state.legal_moves)
    for move in state.legal_moves:
        next_state=copy.deepcopy(state)
        tmp_depth=depth+1
        v=min(v,max_value(next_state.move(move),tmp_depth,global_player))
    return v



