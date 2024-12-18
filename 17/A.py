

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
            #print(f"Outputting: {operand % 8}")
            return operand % 8
        case 6:
            registers[1] = registers[0] // 2 ** operand
        case 7:
            registers[2] = registers[0] // 2 ** operand                                               


def run(registers, opcodes, operands):

    
    i = 0
    ls = []
    while registers[3] < len(opcodes):

        A, B, C, i = registers
        
        item = 0
        opcode = opcodes[i]
        operand = operands[i]
        
        if opcode not in (1, 3):
            match operand:
                case 4:
                    operand = A
                case 5:
                    operand = B
                case 6:
                    operand = C

        item = apply(registers, opcode, operand)
        # 
        # print()
        # input()
        if item is not None:
            ls.append(item)
        registers[3] += 1


    return ls
        

def main():
    data = []
    opcodes=[]
    operands = []
    with open('sample.txt', 'r') as file:
        lines = file.readlines()

        A = int(lines[0].strip()[12:])
        B = int(lines[1].strip()[12:])
        C = int(lines[2].strip()[12:])
        registers = [A, B, C, 0]
        ls = [int(x) for x in lines[-1].strip()[9:].split(',')]
    
        opcodes = [ls[i] for i in range(len(ls ))if i % 2 == 0]
        operands = [ls[i] for i in range(len(ls ))if i % 2 == 1]
        #(opcodes)
        #print(operands)


    run(registers, opcodes, operands)

if __name__ == "__main__":
    main()