# 9,12,1,4,17,0,18

def solve():
  spoken = {
    9: 1,
    12: 2,
    1: 3,
    4: 4,
    17: 5,
    0: 6
  }

  cur_num = 18
  next_num = 0
  turn = 7
  while turn != 2020:
    if cur_num in spoken:
      next_num = turn - spoken[cur_num]
    else:
      next_num = 0
    spoken[cur_num] = turn
    turn += 1
    cur_num = next_num

  return cur_num

if __name__ == "__main__":
  print("Last Num: {}".format(solve()))
