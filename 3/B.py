def run():
    pass

def main():
    
    nums = []

    with open('B_mults.txt', 'r') as file:
    
        enabled = True

        nums = [x for x in [line.strip() for line in file.readlines()]]
        
        new_ls = []
        total = 0
        for num in nums:
            if not enabled:
                if num == "do()":
                    enabled = True
                continue
            if num == "don't()":
                
                enabled = False
                continue
            if num[0] != "m":
                continue
            subNums = [int(x) for x in num[4:-1].split(",")]
            total += subNums[0] * subNums[1]
        print(f"Total: {total}")



if __name__ == "__main__":
    main()