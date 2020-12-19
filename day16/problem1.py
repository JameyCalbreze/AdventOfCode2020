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

def solve(rows):
  attribute_info = rows[:20]

  my_ticket = rows[22]

  nearby_tickets = rows[25:]

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

  error_rate = 0
  for ticket in nearby_tickets:
    ticket_values = ticket.split(',')
    for ticket_value in ticket_values:
      accepted = False
      for ticket_field in ticket_fields.values():
        accepted = accepted or ticket_field.is_accepted(int(ticket_value))
      if not accepted:
        error_rate += int(ticket_value)

  return error_rate


if __name__ == "__main__":
  input_file = open("input.txt", "r")
  rows = input_file.readlines()
  trimmed_rows = list()
  for row in rows:
    trimmed_rows.append(row[:-1])
  print("Error rate: {}".format(solve(trimmed_rows)))
