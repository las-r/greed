# GREED

**GREED** is an esoteric programming language with only 6 commands. It uses a stack tape made of single-bit values and also has a separate memory for storing 1 bit.

It's heavily inspired by [Brainfuck](https://esolangs.org/wiki/Brainfuck). However, it has many differences, especially in the loop behavior.

An interpreter can be found [here](https://github.com/las-r/greed/blob/main/greed.py).

## Aliases

General aliases used for values:

- **STK**: Stack tape  
- **PTR**: Stack pointer  
- **CUR**: `STK[PTR]`  
- **MEM**: 1-bit memory  
- **PC**: Program counter  

## Commands

Instructions used in programs:

- **FLIP** (Flip `CUR`): `*`  
- **TAKE** (Set `MEM` to `CUR`): `(`  
- **GIVE** (Set `CUR` to `MEM`): `)`  
- **FORWARD** (Move `PTR` forward): `>`  
- **BACKWARD** (Move `PTR` backward): `<`  
- **JUMP** (Set `PC` to `CUR` if `MEM` is 1): `!`  

## Examples

### Hello World (ASCII)

Sets `STK` to `"Hello, world!"`:

```
>*>>>*>>>>>*>*>>>*>>*>>*>*>>*>*>>>>*>*>>*>*>>>>*>*>>*>*>*>*>>>*>>*>*>>>>>*>>>>>>>*>*>*>>*>*>*>>*>*>>*>*>*>*>>*>*>*>>>*>>>*>*>>*>*>>>>*>*>>>*>>>>>*>>>>>*>
```