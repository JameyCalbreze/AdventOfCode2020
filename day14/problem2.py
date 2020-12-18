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
    # print("-" * 42)
    # print("Mask: {}".format("".join(self.mask)))
    # print("Bits: {}".format("".join(bits)))
    for i in range(len(self.mask)):
      if self.mask[i] != '0':
        bits[i] = self.mask[i]
    # print("Aftr: {}".format("".join(bits)))

    return bits

  def enumerate_addrs(self, bits):
    enumeration = list()
    bits_stack = list()
    bits_stack.append(bits.copy())
    while len(bits_stack) != 0:
      cur_bits = bits_stack.pop()
      cur_bits_string = "".join(cur_bits)
      x_loc = cur_bits_string.find('X')
      if x_loc != -1:
        zero = cur_bits.copy()
        zero[x_loc] = '0'
        cur_bits[x_loc] = '1'
        bits_stack.append(zero)
        bits_stack.append(cur_bits)
      else:
        enumeration.append(cur_bits_string)

    return enumeration

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
      location = int(row[loc_start:loc_end])
      addresses = cur_mask.enumerate_addrs(cur_mask.apply_mask_to_int(location))
      for address in addresses:
        memory[address] = int(row[loc_end+4:])

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
