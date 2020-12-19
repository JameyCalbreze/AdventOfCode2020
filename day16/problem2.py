import io

class IntRange:
  def __init__(self, r):
    divider = r.find('-')
    self.lower = int(r[:divider])
    self.upper = int(r[divider+1:])

  def is_accepted(self, i):
    return (i >= self.lower and i <= self.upper)

class TicketField:
  def __init__(self, name):
    self.name = name
    self.accepted_ranges = list()

  def add_accepted_range(self, r):
    self.accepted_ranges.append(IntRange(r))

  def is_accepted(self, i):
    accepted = False
    for r in self.accepted_ranges:
      accepted = accepted or r.is_accepted(i)
    return accepted

def find_unique(list_of_sets, position, values_in_use):
  if position == len(list_of_sets):
    i_do_not_trust_you_python = list()
    return i_do_not_trust_you_python

  cur_set = list_of_sets[position]
  legal_values = cur_set.difference(values_in_use)
  for value in legal_values:
    values_in_use.add(value)
    arrangement = find_unique(list_of_sets, position + 1, values_in_use)
    if arrangement != None:
      arrangement.append(value)
      return arrangement
    values_in_use.remove(value)

def solve(rows):
  attribute_info = rows[:20]

  my_ticket = rows[22]

  nearby_tickets = rows[25:]

  departure_fields = {'departure location', 'departure station', 'departure platform', 'departure track', 'departure date', 'departure time'}

  # Parse ticket fields
  ticket_fields = dict()
  for attribute in attribute_info:
    colon = attribute.find(':')
    name = attribute[:colon]
    range_one_end = attribute.find(' ', colon+2)
    range_two_start = range_one_end + 4
    tf = TicketField(name)
    tf.add_accepted_range(attribute[colon+2:range_one_end])
    tf.add_accepted_range(attribute[range_two_start:])
    ticket_fields[name] = tf

  accepted_fields_by_pos = list()
  field_set = set()
  for field in ticket_fields:
    field_set.add(field)
  for _ in range(20):
    accepted_fields_by_pos.append(field_set.copy())

  for ticket in nearby_tickets:
    ticket_values = (int(v) for v in ticket.split(','))
    bad_ticket = False
    ticket_accepted_fields = list()
    for ticket_value in ticket_values:
      accepted_fields = set()
      for tf_name, tf in ticket_fields.items():
        if tf.is_accepted(ticket_value):
          accepted_fields.add(tf_name)
      if len(accepted_fields) == 0:
        bad_ticket = True
      ticket_accepted_fields.append(accepted_fields)
    if not bad_ticket:
      for field_pos in range(20):
        accepted_fields_by_pos[field_pos] = accepted_fields_by_pos[field_pos].intersection(ticket_accepted_fields[field_pos])

  unique_arrangement = find_unique(accepted_fields_by_pos,0,set())
  unique_arrangement.reverse()
  print(unique_arrangement)
  product = 1
  pos = 0
  for value in (int(v) for v in my_ticket.split(',')):
    if unique_arrangement[pos] in departure_fields:
      product *= value
    pos += 1

  return product


if __name__ == "__main__":
  input_file = open("input.txt", "r")
  rows = input_file.readlines()
  trimmed_rows = list()
  for row in rows:
    trimmed_rows.append(row[:-1])
  print("Product: {}".format(solve(trimmed_rows)))
