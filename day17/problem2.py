import io

def enumerate_coordinates(source):
  x, y, z, w = source
  locations = set()
  for x_change in range(-1,2):
    for y_change in range(-1,2):
      for z_change in range(-1,2):
        for w_change in range(-1,2):
          locations.add((x+x_change,y+y_change,z+z_change,w+w_change))
  locations.remove(source)
  return locations

def solve(rows):
  # Parse initial state
  cur_state = set()
  y = 0
  for row in rows:
    x = 0
    for char in row:
      if char == '#':
        cur_state.add((x,y,0,0))
      x += 1
    y -= 1

  iteration_count = 6
  for _ in range(iteration_count):
    next_state = set()
    locations_to_update = list()
    for location in cur_state:
      locations_to_update.append(location)
    checked = cur_state.copy()
    while len(locations_to_update) != 0:
      # Create variables for comparison
      location = locations_to_update.pop()
      surroundings = enumerate_coordinates(location)
      num_active_in_surroundings = len(surroundings.intersection(cur_state))
      active = location in cur_state

      # Check if location should go into the next state
      if active and num_active_in_surroundings >= 2 and num_active_in_surroundings <= 3:
        next_state.add(location)
      elif not active and num_active_in_surroundings == 3:
        next_state.add(location)

      # Add surrounding locations to locations_to_update
      if active:
        surroundings.difference_update(checked)
        for unchecked_location in surroundings:
          locations_to_update.append(unchecked_location)
          checked.add(unchecked_location)

    cur_state = next_state

  return len(cur_state)


if __name__ == "__main__":
  input_file = open("input.txt", "r")
  rows = input_file.readlines()
  trimmed_rows = list()
  for row in rows:
    trimmed_rows.append(row[:-1])
  print("Num active locations: {}".format(solve(trimmed_rows)))
