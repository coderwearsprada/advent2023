import re

def find_first_word(input_string):
    # Define the list of words to search for
    target_words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    print(input_string)
    # Use regular expression to find the first matching word
    #match = re.search(r'\b(?:' + '|'.join(target_words) + r')\b', input_string, flags=re.IGNORECASE)
    first_pos = len(input_string) + 1
    first_number = 0
    last_pos = 0
    last_number = 0
    for x in range(1,10):
         word = target_words[x-1]
         matches = list(re.finditer(word, input_string, flags=re.IGNORECASE))
         if matches:
             first = min(match.span()[0] for match in matches)
             last = max(match.span()[0] for match in matches)
             if first_pos > first:
                 first_pos = first
                 first_number = x
             if last_pos < last:
                 last_pos = last
                 last_number = x

    return [first_number, first_pos, last_number, last_pos]

# Example usage
with open('1_2.input') as f:
    lines = f.readlines()
    first = 0
    second = 0
    total = 0

    for line in lines:
        [first_alpha_number, first_alpha_pos, last_alpha_number, last_alpha_pos] = find_first_word(line.strip())
        print([first_alpha_number, first_alpha_pos, last_alpha_number, last_alpha_pos])
        line = line.strip()
        l = list(line)
        print(l)
        first_digit_pos = 0
        first_digit_number = 0
        last_digit_pos = len(line)-1
        last_digit_number = 0
        for char in l:
            if char.isdigit():
                first_digit_number = int(char)
                break
            first_digit_pos+=1

        for char in l[::-1]:
            if char.isdigit():
                last_digit_number = int(char)
                break
            last_digit_pos-=1
        print([first_digit_number, first_digit_pos, last_digit_number, last_digit_pos])
        if (first_alpha_pos < first_digit_pos):
            first = first_alpha_number
        else:
            first = first_digit_number

        if (last_alpha_pos > last_digit_pos):
            second = last_alpha_number
        else:
            second = last_digit_number

        n = first * 10 + second
        total += n
        print(first, "  ", second, "  ", n)

print (total)
