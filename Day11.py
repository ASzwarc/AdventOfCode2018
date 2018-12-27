
def solver(grid_serial_number):
    grid = [[0 for _ in range(300)] for _ in range(300)]

    def calculate_power_lvl(row, col):
        # because coordinates in challenge start from 1
        row += 1
        col += 1
        rackId = col + 10
        pwr_lvl_start = rackId * row
        pwr_lvl = pwr_lvl_start + grid_serial_number
        pwr_lvl *= rackId
        if pwr_lvl < 100:
            hundreds_digit = 0
        else:
            hundreds_digit = int(str(pwr_lvl)[-3])
        return hundreds_digit - 5

    GRID_SIZE = 300
    # calculating values
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            grid[row][col] = calculate_power_lvl(row, col)

    biggest_val = -100
    biggest_x = 0
    biggest_y = 0
    biggest_size = 0
    for size in range(1, GRID_SIZE + 1):
        if size % 10 == 0:
            print("Checking size {}".format(size))
        search_range = GRID_SIZE - size - 1
        for row in range(search_range):
            for col in range(search_range):
                val = sum(sum(grid[x][col:col + size]) for x in range(row, row + size) )
                if val > biggest_val:
                    biggest_val = val
                    biggest_x = col + 1
                    biggest_y = row + 1
                    biggest_size = size
    return biggest_x, biggest_y, biggest_size, biggest_val

if __name__ == "__main__":
    print(solver(9221))