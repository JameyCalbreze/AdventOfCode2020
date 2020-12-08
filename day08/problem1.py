import io

def solve(rows):
  instructions = list()
  for row in rows:
    temp = row.split(' ')
    instructions.append((temp[0], int(temp[1])))
  
  executed = set()

  acc = 0
  ip = 0
  while ip not in executed:
    executed.add(ip)
    instr = instructions[ip]
    if instr[0] == "acc":
      acc += instr[1]
      ip += 1
    elif instr[0] == "jmp":
      ip += instr[1]
    else:
      ip += 1
  
  return acc

if __name__ == "__main__":
  input_file = open("input.txt","r")
  rows = input_file.readlines()
  trimmed_rows = list()
  for row in rows:
    trimmed_rows.append(row[:-1])
  print("Acc: {}".format(solve(trimmed_rows)))
