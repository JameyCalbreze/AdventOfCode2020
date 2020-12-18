import io

class Mask:
  def __init__(self, mask):
    self.mask = list()
    for char in mask:
      self.mask.append(char)

  def apply_mask_to_int(self, i):
    # convert i to 36 bit base 2
    bits = list()
    while i != 0:
      if i % 2 == 0:
        bits.append('0')
      else:
        bits.append('1')
        i -= 1
      i /= 2

    while len(bits) != len(self.mask):
      bits.append('0')

    # apply mask
    bits.reverse()
    print("-" * 42)
    print("Mask: {}".format("".join(self.mask)))
    print("Bits: {}".format("".join(bits)))
    for i in range(len(self.mask)):
      if self.mask[i] != 'X':
        bits[i] = self.mask[i]
    print("Aftr: {}".format("".join(bits)))
    bits.reverse()

    # convert back to int
    power = 1
    val = 0
    for char in bits:
      if char == '1':
        val += power
      power *= 2

    return val

def solve(rows):
  memory = dict()

  cur_mask = None
  for row in rows:
    if row[:4] == 'mask':
      cur_mask = Mask(row[7:])
    else:
      loc_start = 4
      loc_end = 4
      while row[loc_end] != ']':
        loc_end += 1
      location = row[loc_start:loc_end]
      memory[location] = cur_mask.apply_mask_to_int(int(row[loc_end+4:]))

  s = 0
  for val in memory.values():
    s += val

  return s

if __name__ == "__main__":
  input_file = open("input.txt", "r")
  rows = input_file.readlines()
  trimmed_rows = list()
  for row in rows:
    trimmed_rows.append(row[:-1])
  print("Sum of memory: {}".format(solve(trimmed_rows)))


# 4 / 2 = 2 r 0, 2 / 2 = 1 r 0, 1 / 2 = 0 r 1 --> 100
