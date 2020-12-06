import io

def solve(numbers, seek_num, ignore_index):
  num_dict = dict()
  pos = 0
  for num in numbers:
    if pos != ignore_index:
      num_dict[num] = True
    pos += 1
  pos = 0
  for num in numbers:
    if pos != ignore_index:
      needed_num = seek_num - num
      if num_dict.__contains__(needed_num):
        return needed_num * num
    pos += 1

def problem02(numbers):
  pos = 0
  for num in numbers:
    result = solve(numbers, 2020 - num, pos)
    print("{}: {}".format(pos, result))
    if result != None:
      return result * num
    pos += 1

if __name__ == '__main__':
  # import the input
  input_file = open("input.txt", "r", encoding="utf-8")
  numbers = input_file.readlines()
  int_numbers = list()
  for num in numbers:
    int_numbers.append(int(num))
  print("Solution: {}".format(problem02(int_numbers)))
