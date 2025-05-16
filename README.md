# GREED
GREED is an esoteric programming language with only 6 commands. It uses a stack tape *(current bit referred to as STACK)* and also has a separate memory for storing 1 bit *(current bit in memory referred to as MEM)*.

More information can be found [here](https://esolangs.org/wiki/Greed).

## Commands
**FLIP** (Flip STACK): `*`  
**TAKE** (Set MEM to STACK): `(`  
**GIVE** (Set STACK to MEM): `)`  
**FORWARD** (Move stack pointer forward): `>`  
**BACKWARD** (Move stack pointer backward: `<`  
**REWIND** (Set the pointer to index 0 if MEM is 1): `&`

## Examples
### First Bit To 1
```
*
```
### Hello World (ASCII)
```
>*>>>*>>>>>*>*>>>*>>*>>*>*>>*>*>>>>*>*>>*>*>>>>*>*>>*>*>*>*>>>*>>*>*>>>>>*>>>>>>>*>*>*>>*>*>*>>*>*>>*>*>*>*>>*>*>*>>>*>>>*>*>>*>*>>>>*>*>>>*>>>>>*>>>>>*>
```
