import io
import math

# Horrible brute force method
# def solve(rows):
#   buses = rows[1].split(',')

#   for i in range(len(buses)):
#     if buses[i] == 'x':
#       continue
#     buses[i] = int(buses[i])

#   increment = buses[0]
#   pos = 0
#   found = False
#   while not found:
#     print(pos)
#     pos += increment
#     match_delay = True
#     for delay in range(1,len(buses)):
#       if buses[i] == 'x':
#         continue
#       match_delay = match_delay and ((pos+delay) % buses[i]) == 0
#     found = match_delay

#   return pos

def solve(rows):
  buses = rows[1].split(',')

  for i in range(len(buses)):
    if buses[i] == 'x':
      continue
    buses[i] = int(buses[i])

  increment = buses[0]
  pos = 0
  for i in range(1,len(buses)):
    if buses[i] == 'x':
      continue
    found = False
    while not found:
      pos += increment
      found = (pos+i) % buses[i] == 0
    increment *= int(buses[i]/math.gcd(increment,buses[i]))
    pos -= increment
  
  return pos + increment

if __name__ == "__main__":
  input_file = open("input.txt","r")
  rows = input_file.readlines()
  trimmed_rows = list()
  for row in rows:
    trimmed_rows.append(row[:-1])
  print("Solution: {}".format(solve(trimmed_rows)))
