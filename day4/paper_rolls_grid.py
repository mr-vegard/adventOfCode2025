
with open("input.txt", "r") as f:
    input_list = f.readlines()


paper_roll_grid = []
for row in input_list:
    paper_roll_grid.append(list(row.replace("\n", "")))


def is_paper_present(paper_roll_row: list, index: int) -> bool:
    if index < 0:
        return False
    try:
        if paper_roll_row[index] == "@":
            return True
    except IndexError:
        return False
    return False

forklift_fit = 0

paper_roll_grid_new = paper_roll_grid

new_grid_happening = 0

while True:
    for row in range(0, len(paper_roll_grid)):
        for roll in range(0, len(paper_roll_grid[row])):
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
                    paper_roll_grid_new[row][roll] = "."

    if paper_roll_grid_new == paper_roll_grid:
        new_grid_happening += 1
        print(forklift_fit)
    if new_grid_happening == 100:
        break

print(forklift_fit)
                
