import io

def execute(instructions):
  executed = set()
  acc = 0
  ip = 0
  while ip not in executed and ip < len(instructions):
    executed.add(ip)
    instr = instructions[ip]
    if instr[0] == "acc":
      acc += instr[1]
      ip += 1
    elif instr[0] == "jmp":
      ip += instr[1]
    else:
      ip += 1
  return (acc, ip)

def solve(rows):
  instructions = list()
  possible_flips = list()
  pos = 0
  for row in rows:
    temp = row.split(' ')
    if temp[0] == 'jmp' or temp[0] == 'nop':
      possible_flips.append(pos)
    instructions.append((temp[0], int(temp[1])))
    pos += 1

  while len(possible_flips) > 0:
    current_flip_index = possible_flips.pop()

    # Flip
    original = instructions[current_flip_index]
    if original[0] == 'jmp':
      instructions[current_flip_index] = ('nop', original[1])
    else:
      instructions[current_flip_index] = ('jmp', original[1])

    # Execute and check
    result = execute(instructions)
    if result[1] == len(instructions):
      return result[0]

    # Repair
    instructions[current_flip_index] = original
  
  return -1

if __name__ == "__main__":
  input_file = open("input.txt","r")
  rows = input_file.readlines()
  trimmed_rows = list()
  for row in rows:
    trimmed_rows.append(row[:-1])
  print("Acc: {}".format(solve(trimmed_rows)))
