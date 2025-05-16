import sys

# GREED made by las_r on github
# version 1.0

# how to use:
# put program in 'prog' variable
# run python file

# notes:
# c means center

# program
prog = "*<*<<*"

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

# output
sstk = ""
for ind, s in enumerate(stk):
  if ind - init == 0:
    sstk += "c"
  
  if s:
    sstk += "1"
  else:
    sstk += "0"
print(f"STACK: {sstk}")
print(f"MEM: {mem}")
print(f"Pointer: {ptr - init}")
