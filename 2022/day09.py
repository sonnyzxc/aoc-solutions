from utils.parse_input import get_input_2d_str_int

data = get_input_2d_str_int("09")

# start both H and T at (0, 0)
H_x = H_y = 0
T_x = T_y = 0
visited = {(0, 0)}

for instr, n in data:
    for _ in range(n):
        match instr:
            case "R":
                H_x += 1
            case "U":
                H_y += 1
            case "L":
                H_x -= 1
            case "D":
                H_y -= 1

        dx = H_x - T_x
        dy = H_y - T_y

        if abs(dx) > 1 or abs(dy) > 1:
            if dx != 0:
                T_x += 1 if dx > 0 else -1
            if dy != 0:
                T_y += 1 if dy > 0 else -1

        visited.add((T_x, T_y))

# part 1
print(len(visited))
