

with open('2_1.input') as f:
    lines = f.readlines()
    count = 0
    total = 0
    for line in lines:
        # init
        max_red = 0
        max_green = 0
        max_blue = 0

        game = line.strip().split(':')[1]
        count += 1
        draws = game.strip().split(";")
        for draw in draws:
            cubes = draw.strip().split(",")
            for cube in cubes:
                cube_split = cube.strip().split(" ")
                #print (cube_split)
                cube_count = int(cube_split[0])
                color = cube_split[1]
                #print(color, cube_count, max_red)
                if color == "red" and cube_count > max_red:
                    max_red = cube_count
                if color == "green" and cube_count > max_green:
                    max_green = cube_count
                if color == "blue" and cube_count > max_blue:
                    max_blue = cube_count
        print (count, " max red: ", max_red, " max green: ", max_green, " max blue: ", max_blue)
        total += max_red*max_green*max_blue

print(total)



