def digit_stack(commands):
    stack = list()
    suma = 0
    for command in commands:
        if command.startswith("PEEK"):
            suma += stack[-1] if stack else 0
        elif command.startswith("POP"):
            suma += stack[-1] if stack else 0
            stack = stack[:-1]
        elif command.startswith("PUSH"):
            stack.append(int(command[5:]))
    return suma
            
            
        






assert digit_stack(["PUSH 3", "POP", "POP", "PUSH 4", "PEEK", "PUSH 9", "PUSH 0", "PEEK", "POP", "PUSH 1", "PEEK"])
assert digit_stack(["POP", "POP"]) == 0
assert digit_stack(["PUSH 9", "PUSH 9", "POP"]) == 9
assert digit_stack([]) == 0
