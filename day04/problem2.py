import io
import re

def match_re_to_str(r, string):
  match = re.match(r, string)
  if match != None and match.end() == len(string):
    return True
  else:
    return False

def check_passport(passport_map):
  '''
    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    hgt (Height) - a number followed by either cm or in:
        If cm, the number must be at least 150 and at most 193.
        If in, the number must be at least 59 and at most 76.
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    cid (Country ID) - ignored, missing or not.
  '''
  # cid is technically a field, but we don't care about it
  required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
  valid = True
  pos = 0 
  while valid and pos < len(required_fields):
    field = required_fields[pos]
    pos += 1
    valid = valid and passport_map.__contains__(field)
    if valid:
      value = passport_map[field]
      if field == "byr":
        r = re.compile(r"[0-9]{4}")
        if match_re_to_str(r, value):
          num = int(value)
          valid = (num >= 1920) and (num <= 2002)
        else:
          valid = False
      elif field == "iyr":
        r = re.compile(r"[0-9]{4}")
        if match_re_to_str(r, value):
          num = int(value)
          valid = (num >= 2010) and (num <= 2020)
        else:
          valid = False
      elif field == "eyr":
        r = re.compile(r"[0-9]{4}")
        if match_re_to_str(r, value):
          num = int(value)
          valid = (num >= 2020) and (num <= 2030)
        else:
          valid = False
      elif field == "hgt":
        cm_pat = re.compile(r"[0-9]{3}cm")
        in_pat = re.compile(r"[0-9]{2}in")
        if match_re_to_str(cm_pat, value):
          num = int(value[:3])
          valid = (num >= 150) and (num <= 193)
        elif match_re_to_str(in_pat, value):
          num = int(value[:2])
          valid = (num >= 59) and (num <= 76)
        else:
          valid = False
      elif field == "hcl":
        # The regex string I want here is
        # #[0-9a-f]{6}
        r = re.compile(r"#[0-9a-f]{6}")
        valid = match_re_to_str(r, value)
      elif field == "ecl":
        r = re.compile(r"amb|blu|brn|gry|grn|hzl|oth")
        valid = match_re_to_str(r, value)
      elif field == "pid":
        r = re.compile(r"[0-9]{9}")
        valid = match_re_to_str(r, value)
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
