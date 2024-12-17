def run():
    pass

def main():
    
    nums = []

    with open('A_mults.txt', 'r') as file:
    
        nums = [tuple([int(y) for y in x[1:-1].split(",")]) for x in [line.strip() for line in file.readlines()]]
        total = 0
        for num in nums:
            total += num[0] * num[1]
        
        print(f"Total: {total}")


if __name__ == "__main__":
    main()