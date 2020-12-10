import io

class Node:
  def __init__(self, val):
    self.val = val
    self.n = None

class LimitedLinkedList:
  def __init__(self, max_size):
    self.max_size = max_size
    self.head = None
    self.size = 0

  def append(self, val):
    if self.head == None:
      self.head = Node(val)
    else:
      cur_node = self.head
      while cur_node.n != None:
        cur_node = cur_node.n
      cur_node.n = Node(val)
    
    if self.size == self.max_size:
      self.head = self.head.n
    else:
      self.size += 1

  def toList(self):
    new_list = list()
    cur_node = self.head
    while cur_node != None:
      new_list.append(cur_node.val)
      cur_node = cur_node.n
    new_list.sort()
    return new_list

def test(sorted_numbers, seeked_sum):
  valid = False
  left = 0
  right = len(sorted_numbers) - 1
  while not valid and left != right:
    lr_sum = sorted_numbers[left] + sorted_numbers[right]
    if lr_sum < seeked_sum:
      left += 1
    elif lr_sum > seeked_sum:
      right -= 1
    else:
      valid = True
  return valid

def solve(rows):
  # Load preamble
  p_25 = LimitedLinkedList(25)
  for row in rows[:25]:
    p_25.append(row)

  # Search
  num_to_sum = 0
  pos = 25
  seeking = True
  while seeking:
    num = rows[pos]
    # Test and check
    if not test(p_25.toList(), num):
      num_to_sum = num
      seeking = False
    # Append
    p_25.append(num)
    pos += 1

  # Find consecutive nums to reach num_to_sum
  left = 0
  right = 0
  seeking = True
  while seeking:
    sum_seq = sum(rows[left:right+1])
    if sum_seq < num_to_sum:
      right += 1
    elif sum_seq > num_to_sum:
      left += 1
    else:
      seeking = False
    print("Left: {}, Right: {}".format(left, right))

  section = rows[left:right+1]
  return min(section) + max(section)

if __name__ == "__main__":
  input_file = open("input.txt", "r")
  rows = input_file.readlines()
  trimmed_rows = list()
  for row in rows:
    trimmed_rows.append(int(row))
  print("Encryption Weakness: {}".format(solve(trimmed_rows)))
