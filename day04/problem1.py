import io

def check_passport(passport_map):
  # cid is technically a field, but we don't care about it
  required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
  valid = True
  for field in required_fields:
    valid = valid and passport_map.__contains__(field)
  return valid

def solve(rows):
  num_valid = 0

  passport_batches = list()
  current_batch = list()

  # First separate all of the lines into separate passports
  for row in rows:
    if row == "":
      passport_batches.append(current_batch)
      current_batch = list()
    else:
      current_batch.append(row)

  if len(current_batch) != 0:
    passport_batches.append(current_batch)
  
  # Second convert each batch into a map and then pass to check_passport
  for batch in passport_batches:
    passport_map = dict()
    for row in batch:
      k_v_pairs = row.split(' ')
      for k_v_pair in k_v_pairs:
        colon_pos = 0
        while k_v_pair[colon_pos] != ':':
          colon_pos += 1
        passport_map[k_v_pair[:colon_pos]] = k_v_pair[colon_pos + 1:]
    print(passport_map)
    num_valid += check_passport(passport_map)

  return num_valid

if __name__ == "__main__":
  input_file = open("input.txt", "r", encoding="utf-8")
  rows = input_file.readlines()
  trimmed_rows = list()
  for row in rows:
    trimmed_rows.append(row[:-1])
  print("Number of valid passports: {}".format(solve(trimmed_rows)))
