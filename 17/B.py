from A import run as run2


def apply(registers, opcode, operand):
    
    match opcode:
        case 0:
            registers[0] = registers[0] // 2 ** operand
        case 1:
            registers[1] = registers[1] ^ operand
        case 2:
            registers[1] = operand % 8
        case 3:
            if registers[0] == 0:
                return
            
            registers[3] = operand - 1
        case 4:
            registers[1] = registers[1] ^ registers[2]
        case 5:
            return operand % 8
        case 6:
            registers[1] = registers[0] // 2 ** operand
        case 7:
            registers[2] = registers[0] // 2 ** operand                                               


def run(registers, opcodes, operands, backRelos, target_ls):

    
    ls = target_ls # 2,4,1,2,7,5,1,3,4,4,5,5,0,3,3,0
    targetLength = len(ls)

    outputls = []
    repeat = True
    A, B, C = 0, 0, 0
    invalid = False
        
    failed = False


    ls = target_ls.copy()
    

    while len(ls) > 0:
        if len(ls) != len(target_ls):
            A *= 8
        
        invalid = True
        target = ls.pop()

        mod = -1
        cCalc = -1
        combos = set()
        i = 8 if A == 0 else 64
        x = 0
        while True:
            
            B = x % 8
            B = B ^ 2
            C = ((A+x) // 2 ** B) % 8
            B = B ^ 3
            B = B ^ C
            
            if B % 8 == target:
                
                mod = x
                string = run2([A+mod, 0, 0, 0], opcodes, operands)

                if string != [target] + outputls:
                    x += 1
                    continue
                
                outputls.insert(0, B % 8)
                invalid = False
                

            if not invalid:
                A += mod
                break
            x += 1


        

        if mod == -1:
            print("Failed")
            failed = True
            outputls = []
            break

    print(f"Register A: {A}")
    print(f"Register B: {registers[1]}")
    print(f"Register C: {registers[2]}")
    print()
    string = ""
    for item in outputls:
        string += str(item) + ","

    print(f"Program: {string.rstrip(",")}")
        

def main():

    opcodes=[]
    operands = []
    backRelos = {}
    with open('sample.txt', 'r') as file:
        lines = file.readlines()

        A = 0
        B = 0
        C = 0
        
        ls = [int(x) for x in lines[-1].strip()[9:].split(',')]
    
        opcodes = [ls[i] for i in range(len(ls ))if i % 2 == 0]
        operands = [ls[i] for i in range(len(ls ))if i % 2 == 1]


        backRelos = {operands[i]:i for i, x in enumerate(opcodes) if x == 3}

        registers = [A, B, C, len(opcodes) - 1]
        
    run(registers, opcodes, operands, backRelos, ls)

if __name__ == "__main__":
    main()