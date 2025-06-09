# binary to greed converter by las_r on github
# v1.1

# usage:
# input binary into the `binary` variable
# run program in command line
# copy generated greed program which sets the stack to the binary

# binary thing
binary = "01001000011001010110110001101100011011110010110000100000011101110110111101110010011011000110010000100001"

# loop through string and convert
new = ""
for b in binary:
    if int(b):
        new += "*"
    new += ">"

# output program
print(new)
