word = "algorithmie"
result = ""

for char in word:
    result = char + result

print(result)

print("=" * 25)

grid = [
    [0, 1, 0, 1],
    [1, 1, 0, 0],
    [0, 0, 1, 0],
]

# count_all(grid)
# count_row(grid, row)

def count_all(grid):
    count = 0
    for row in grid:
        for value in row:
            if value == 1:
                count += 1
    return count

def count_row(grid, row):
    count = 0
    for value in grid[row]:
        if value == 1:
            count += 1
    return count

assert count_all(grid) == 5
assert count_row(grid, 0) == 2
assert count_row(grid, 1) == 2
assert count_row(grid, 2) == 1

print("="*25)

print(list(range(-1, 2)))

def count_neighbor(grid, row, col):
    count = 0
    
    for row_offset in range(-1, 2):
        for col_offset in range(-1, 2):
            print(row_offset, col_offset)
            
            is_center = row_offset == 0 and col_offset == 0
            
            if not is_center:
                neighbor_row = row + row_offset
                neighbor_col = col + col_offset
                
                row_is_valid = (
                    neighbor_row >= 0
                    and neighbor_row < len(grid)
                )
                
                col_is_valid = (
                    neighbor_col >= 0
                    and neighbor_col < len(grid)
                )
                
                if row_is_valid and col_is_valid:
                    count += grid[neighbor_row][neighbor_col]
    
    return count
                
res = count_neighbor(grid, 1, 2)
print(res)

assert count_neighbor(grid, 1, 1) == 3
assert count_neighbor(grid, 0, 0) == 3
assert count_neighbor(grid, 3, 3) == 10