import sys

# GREED made by las_r on github
# version 1.6

# how to use:
# put program in 'prog' variable
# run python file

# notes:
# c means center
# 'debug' variable enables tracing

# program
prog = ">*>>>*>>>>>*>*>>>*>>*>>*>*>>*>*>>>>*>*>>*>*>>>>*>*>>*>*>*>*>>>*>>*>*>>>>>*>>>>>>>*>*>*>>*>*>*>>*>*>>*>*>*>*>>*>*>*>>>*>>>*>*>>*>*>>>>*>*>>>*>>>>>*>>>>>*>"
debug = False

# environment
stk = [False]
ptr = 0
init = 0
mem = False

# run program
i = 0
while i < len(prog):
    com = prog[i]
    
    # FLIP
    if com == "*":
        stk[ptr] = not stk[ptr]

        if debug:
            print(f"Flipped ({ptr - init}, {i})")
        
    # TAKE
    elif com == "(":
        mem = stk[ptr]

        if debug:
            print(f"Took ({ptr - init}, {i})")
        
    # GIVE
    elif com == ")":
        stk[ptr] = mem

        if debug:
            print(f"Gave ({ptr - init}, {i})")
        
    # FORWARD
    elif com == ">":
        ptr += 1
        try:
            stk[ptr]
        except IndexError:
            stk.append(False)

        if debug:
            print(f"Moved stack forward ({ptr - 1 - init}, {i})")
            
    # BACKWARD
    elif com == "<":
        ptr -= 1
        if ptr < 0:
            stk.insert(0, False)
            init += 1
            ptr = 0

        if debug:
            print(f"Moved stack forward ({ptr + 1 - init}, {i})")
            
    # REWIND
    elif com == "&":
        if mem:
            i = -1
            ptr = init

            if debug:
                print(f"Rewinding...")
            
    # unknown
    else:
        print(f"`{com}` is not a known command. ({ptr + 1 - init}, {i})")
        sys.exit(1)
    
    i += 1

# binary stack
bstk = ""
for ind, s in enumerate(stk):    
    if s:
        bstk += "1"
    else:
        bstk += "0"

# hex stack
hstk = hex(int(bstk))

# ascii stack
astk = ''.join(chr(int(bstk[i:i+8], 2)) for i in range(0, len(bstk), 8))

# output
print(f"STACK (Binary): 0b{bstk}")
print(f"STACK (Hex): {hstk}")
print(f"STACK (ASCII): {astk}")
print(f"MEM: {mem}")
print(f"Pointer Position: {ptr}")
