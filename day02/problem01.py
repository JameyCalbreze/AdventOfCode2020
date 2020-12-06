import io

def check_password(min_occur, max_occur, char_to_count, password):
  count = 0
  for character in password:
    if character == char_to_count:
      count += 1
  return (count >= min_occur) and (count <= max_occur)

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
    password = row[sub_start:]

    count += check_password(min_occur, max_occur, char_to_count, password)
    
  return count

if __name__ == "__main__":
  input_file = open("input.txt", "r", encoding="utf-8")
  rows = input_file.readlines()
  print("Number of valid passwords: {}".format(solve(rows)))
