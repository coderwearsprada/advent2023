
with open('1.input') as f:
    lines = f.readlines()
    first = 0
    second = 0
    total = 0
    for line in lines:
        line = line.strip()
        l = list(line)
        print(l)
        for char in l:
            if char.isdigit():
                first = int(char)
                break


        for char in l[::-1]:
            if char.isdigit():
                second = int(char)
                break

        n = first * 10 + second
        total += n
        print(first, "  ", second, "  ", n)

print (total)

