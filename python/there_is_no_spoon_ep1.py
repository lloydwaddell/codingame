# https://www.codingame.com/training/medium/there-is-no-spoon-episode-1
width, height, search_value = [int(raw_input())] + [int(raw_input())] + ["0"]
grid = [raw_input() for _ in range(height)]

for row_id, row in enumerate(grid):
    if(search_value in row): # skip rows without search values
        next_col_id = grid[row_id].index(search_value) # first index
        while(next_col_id != -1): # Use next right most index or continue
            # Check Right
            right_col,right_row = (-1,-1)
            if(search_value in grid[row_id][next_col_id + 1:]):
                right_col,right_row = (next_col_id + grid[row_id][next_col_id + 1:].index(search_value) + 1,row_id)
                
            ## Check Bottom
            bottom_col,bottom_row = (-1,-1)
            if search_value in [ a[next_col_id] for a in grid[row_id + 1:] ]:
                bottom_col, bottom_row = (next_col_id, row_id + [a[next_col_id] for a in grid[row_id + 1:]].index(search_value) + 1)
            
            print next_col_id,row_id,right_col,right_row,bottom_col,bottom_row
            next_col_id = right_col
