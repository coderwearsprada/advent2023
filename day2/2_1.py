max_red = 12
max_green = 13
max_blue = 14

with open('2_1.input') as f:
    lines = f.readlines()
    count = 0
    total = 0
    for line in lines:
        game = line.split(':')[1]
        count += 1
        draws = game.split(";")
        possible = True
        for draw in draws:
            cubes = draw.split(",")
            for cube in cubes:
                cube_split = cube.split(" ")
                #print (cube_split)
                cube_count = int(cube_split[1])
                color = cube_split[2]

                if color == "red" and cube_count > max_red:
                    possible = False
                    break
                if color == "green" and cube_count > max_green:
                    possible = False
                    break
                if color == "blue" and cube_count > max_blue:
                    possible = False
                    break
            if possible == False:
                break
        print (count, " possible? ", possible)
        if possible == True:
            total += count
        possible = True

print(total)



