
def recur(i, j, map, newMap):

    if i <= 0 or i >= len(map) - 1 or j <= 0 or j >= len(map[0]) - 1:
        return False
    
    tl, tr, bl, br = map[i-1][j-1], map[i-1][j+1], map[i+1][j-1], map[i+1][j+1]

    cross = (tl, tr, bl, br)

    countM = len([x for x in cross if x == "M"])
    countS = len([x for x in cross if x == "S"])

    if countM  < 2 or countS < 2:
        return False
    
    if (tr == tl or tr == br):
        newMap[i-1][j-1] = tl
        newMap[i-1][j+1] = tr
        newMap[i+1][j-1] = bl
        newMap[i+1][j+1] = br
        newMap[i][j] = "A"
        return True
    return False

def run(map):
    
    count = 0
    ls = []
    for line in map:
        new_ls = []
        for item in line:
            new_ls.append(".")
        ls.append(new_ls)

    for i, row in enumerate(map):
        for j, letter in enumerate(row):
            
            if letter == "A":
                count += 1 if recur(i, j, map, ls) else 0
    
    print(f"Total count: {count}")    
def main():

    xmasMap = []
    with open('xmas.txt', 'r') as file:

        xmasMap = [x for x in list(line.strip() for line in file.readlines())]
    
    run(xmasMap)


if __name__ == "__main__":
    main()
    