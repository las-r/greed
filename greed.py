import sys

# GREED made by las_r on github
# version 1.1

# how to use:
# put program in 'prog' variable
# run python file

# notes:
# c means center

# program
prog = ">*>>>*>>>>>*>*>>>*>>*>>*>*>>*>*>>>>*>*>>*>*>>>>*>*>>*>*>*>*>>>*>>*>*>>>>>*>>>>>>>*>*>*>>*>*>*>>*>*>>*>*>*>*>>*>*>*>>>*>>>*>*>>*>*>>>>*>*>>>*>>>>>*>>>>>*>"

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
    
  # TAKE
  elif com == "(":
    mem = stk[ptr]
    
  # GIVE
  elif com == ")":
    stk[ptr] = mem
    
  # FORWARD
  elif com == ">":
    ptr += 1
    try:
      stk[ptr]
    except IndexError:
      stk.append(False)
      
  # BACKWARD
  elif com == "<":
    ptr -= 1
    if ptr < 0:
      stk.insert(0, False)
      init += 1
      ptr = 0
      
  # REWIND
  elif com == "&":
    if mem:
      i = 0
      ptr = init
      
  # unknown
  else:
    print(f"`{com}` is not a known command.")
    sys.exit(1)
  
  i += 1

# binary stack
bstk = ""
for ind, s in enumerate(stk):
  if ind - init == 0:
    bstk += "c"
  
  if s:
    bstk += "1"
  else:
    bstk += "0"

# ascii stack
try:
  astk = ''.join(chr(int(bstk.replace("c", "")[i:i+8], 2)) for i in range(0, len(bstk.replace("c", "")), 8))
except:
  astk = None

# output
print(f"STACK: {bstk}")
print(f"STACK (ASCII): {astk}")
print(f"MEM: {mem}")
print(f"Pointer Position: {ptr - init}")
