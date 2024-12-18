def isValid(line, failCount, prev, increasing, decreasing, k):
    for i, num in enumerate(line):
        if i == 0:
            continue
        
        num = int(num)
        numSet = False
        if increasing:
            if num <= prev or num > prev + 3:
                
                if i == len(line) - 1:
                    failCount += 1
                    numSet = True
                    
                    if failCount > 1:
                        increasing = False
                    break

                next = int(line[i+1])

                if prev < next and next <= prev + 3:
                    failCount += 1
                    numSet = True

                    if failCount > 1:
                        increasing = False
                        break

                else:
                    twoCheck = False
                    if i >= 2:
                        
                        twoBack = int(line[i-2])
                        if twoBack < num and num <= twoBack + 3:
                            failCount += 1
                            twoCheck = True
                            if failCount > 1:
                                increasing = False
                                break
                    
                    if not twoCheck:
                        increasing = False
                        break
        if decreasing:
            if num >= prev or num < prev - 3:

                if i == len(line) - 1:

                    failCount += 1
                    numSet = True
                    if failCount > 1:
                        decreasing = False
                    break

                next = int(line[i+1])

                if prev > next and next >= prev - 3:
                    failCount += 1
                    numSet = True

                    if failCount > 1:
                        decreasing = False
                        break

                else:
                    twoCheck = False
                    if i >= 2:
                        twoBack = int(line[i-2])
                        if twoBack > num and num >= twoBack - 3:
                            failCount += 1
                            twoCheck = True
                            if failCount > 1:
                                decreasing = False
                                break
                    if not twoCheck:
                        decreasing = False
                        break
        if not numSet:
            prev = num
        

    return increasing or decreasing

def run(data):
    
    count = 0
    for k, line in enumerate(data):

        increasing = False
        decreasing = False
        first  = int(line[0])
        second = int(line[1])
        penult = int(line[-2])
        last   = int(line[-1])

        if first < last:
            increasing = True
        elif first > last:
            decreasing = True

        valid1 = isValid(line, 0, first, increasing, decreasing, k)

        increasing = False
        decreasing = False

        ls_right = line[1:]

        if second < last:
            increasing = True
        elif second > last:
            decreasing = True
        valid2 = isValid(ls_right, 1, second, increasing, decreasing, k)

        increasing = False
        decreasing = False
        
        ls_left = line[:-1]

        if first < penult:
            increasing = True
        elif first > penult:
            decreasing = True
        valid3 = isValid(ls_left, 1, first, increasing, decreasing, k)

        if valid1 or valid2 or valid3:
            count += 1

               
        
    print(count)



def main():
    
    data = []
    with open('levels.txt', 'r') as file:
        lines = file.readlines()

        for line in lines:
            line = line.strip().split()
            data.append(line)        

    run(data)     


if __name__ == "__main__":
    main()