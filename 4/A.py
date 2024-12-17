
def recur(i, j, direction, map, target, word):

    if i < 0 or i >= len(map) or j < 0 or j >= len(map[0]):
        return False
    
    letter = map[i][j]

    if letter != target:
        return False
    
    if letter == "S":
        return True
    
    match direction:
        case 0:
            return recur(i-1, j, direction, map, word[word.index(letter)+1], word)
        case 1:
            return recur(i-1, j+1, direction, map, word[word.index(letter)+1], word)
        case 2:
            return recur(i, j+1, direction, map, word[word.index(letter)+1], word)
        case 3:
            return recur(i+1, j+1, direction, map, word[word.index(letter)+1], word)
        case 4:
            return recur(i+1, j, direction, map, word[word.index(letter)+1], word)
        case 5:
            return recur(i+1, j-1, direction, map, word[word.index(letter)+1], word)
        case 6:
            return recur(i, j-1, direction, map, word[word.index(letter)+1], word)
        case 7:
            return recur(i-1, j-1, direction, map, word[word.index(letter)+1], word)                                                


def run(map):
    
    word = tuple('XMAS')
    print(word)
    count = 0
    for i, row in enumerate(map):
        for j, letter in enumerate(row):
            
            # print(letter)
            count += sum(recur(i, j, r, map, "X", word) for r in range(8))
    print(count)

def main():

    xmasMap = []
    with open('xmas.txt', 'r') as file:

        xmasMap = [x for x in list(line.strip() for line in file.readlines())]
    
    run(xmasMap)


if __name__ == "__main__":
    main()
    