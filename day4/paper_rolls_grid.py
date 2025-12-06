from dataclasses import dataclass

from typing import Literal

with open("input.txt", "r") as f:
    input_list = f.readlines()


paper_roll_grid = []
for row in input_list:
    paper_roll_grid.append(list(row.replace("\n", "")))


print(paper_roll_grid)

def is_paper_present(paper_roll_row: list, index: int) -> bool:
    # print(f"index: {index}")
    # print(f"paper_roll_row: {paper_roll_row}")
    if index < 0:
        return False
    try:
        if paper_roll_row[index] == "@":
            # print("True")
            return True
    except IndexError:
        return False
    return False

forklift_fit = 0

for row in range(0, len(paper_roll_grid)):
    # print(paper_roll_grid[row])
    for roll in range(0, len(paper_roll_grid[row])):
        # print(paper_roll_grid[row][roll])
        if paper_roll_grid[row][roll] == "@":
            rolls_as_neigbours = 0
            if row - 1 >= 0:
                if is_paper_present(paper_roll_grid[row -1], roll - 1):
                    rolls_as_neigbours += 1
                if is_paper_present(paper_roll_grid[row -1], roll):
                    rolls_as_neigbours += 1
                    
                if is_paper_present(paper_roll_grid[row -1], roll +1 ):
                    rolls_as_neigbours += 1
                    

            if is_paper_present(paper_roll_grid[row], roll - 1):
                    rolls_as_neigbours += 1
                    
            if is_paper_present(paper_roll_grid[row], roll + 1):
                    rolls_as_neigbours += 1
                    

            if row + 1 < len(paper_roll_grid):
                if is_paper_present(paper_roll_grid[row + 1], roll - 1):
                    rolls_as_neigbours += 1
                    
                if is_paper_present(paper_roll_grid[row + 1], roll):
                    rolls_as_neigbours += 1
                    
                if is_paper_present(paper_roll_grid[row + 1], roll + 1):
                    rolls_as_neigbours += 1
                    
            
            if rolls_as_neigbours < 4:
                forklift_fit += 1

print(forklift_fit)
                
