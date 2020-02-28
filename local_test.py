import functions

board_arr=[4,4,4,4,4,4,0,4,4,4,4,4,4,0]
player_num=1
move=functions.minmax(player_num,board_arr)
print(move)