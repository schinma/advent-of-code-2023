
def get_first_digit(string):
    for c in string:
        try: 
            first = int(c)
            return first
        except ValueError:
            pass
    
with open("input.txt", "r") as file:
    result = 0
    for line in file.readlines():        
        first = get_first_digit(line)
        last = get_first_digit(line[::-1])
        result += int(f"{first}{last}")

print(result)