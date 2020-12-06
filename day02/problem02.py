import io

def check_password(min_occur, max_occur, char_to_count, password):
  pos_one = password[min_occur - 1] == char_to_count
  pos_two = password[max_occur - 1] == char_to_count
  return pos_one ^ pos_two

def solve(rows):
  count = 0
  for row in rows:
    min_occur = 0
    max_occur = 0
    char_to_count = 'a'
    password = ""

    sub_start = 0
    pos = 0
    while row[pos] != '-':
      pos += 1

    min_occur = int(row[sub_start:pos])
    sub_start = pos + 1
    pos = sub_start

    while row[pos] != ' ':
      pos += 1
    
    max_occur = int(row[sub_start:pos])
    char_to_count = row[pos + 1]
    sub_start = pos + 4
    password = row[sub_start:-1]

    count += check_password(min_occur, max_occur, char_to_count, password)
    
  return count

if __name__ == "__main__":
  input_file = open("input.txt", "r", encoding="utf-8")
  rows = input_file.readlines()
  print("Number of valid passwords: {}".format(solve(rows)))
