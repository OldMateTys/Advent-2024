import math

def blink(rocks: list) -> None:
    
    rock_memo = {x:1 for x in rocks}
    rock_memo[1] = 0

    for i in range(75):
        memo = rock_memo.copy()
        for key in memo:
            memo[key] = 0

        for rock in rock_memo:
            count = rock_memo[rock]

            if count == 0:
                continue
            if rock == 0:
                memo[1] += count
                continue
            length = math.floor(math.log10(rock)) + 1
            if length % 2 == 0:

                half = length // 2

                numLarge = rock // 10 ** half
                numSmall = rock % 10 ** half

                if numLarge in memo:
                    memo[numLarge] += count
                else:
                    memo[numLarge] = count
                
                if numSmall in memo:
                    memo[numSmall] += count
                else:
                    memo[numSmall] = count
            else:
                num24 = rock * 2024
                if num24 in memo:
                    memo[num24] += count
                else:
                    memo[num24] = count
        rock_memo = memo
    total = 0
    for rock in rock_memo:
        total += rock_memo[rock]

    print(f"Total rocks: {total}")
    


def main():
    rocks = [6, 11, 33023, 4134, 564, 0, 8922422, 688775]
    blink(rocks)

if __name__ == "__main__":
    main()