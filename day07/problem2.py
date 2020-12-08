import io

class Graph:
  '''
  This will contain all of the bag names and the edges which connect them
  Each edge is formatted as source -> list((dest, quantity))
  '''
  def __init__(self, nodes, edges):
    self.nodes = nodes
    self.edges = edges

  # Compact DFS implementation which takes advantage of the call stack
  def find_all_reachable(self, start):
    reachable = set()
    self.find_all_reachable_h(start, reachable)
    return reachable
  
  def find_all_reachable_h(self, start, reachable):
    for edge in self.edges[start]:
      if edge[0] not in reachable:
        reachable.add(edge[0])
        self.find_all_reachable_h(edge[0], reachable)

  # Count the bags within a bag
  def count_bags(self, start):
    count_dict = dict()
    self.count_bags_h(start, count_dict)
    return count_dict[start]

  def count_bags_h(self, start, count_dict):
    count = 0
    for edge in self.edges[start]:
      if edge[0] not in count_dict:
        self.count_bags_h(edge[0], count_dict)
      count += edge[1] + (edge[1] * count_dict[edge[0]])
    count_dict[start] = count

def solve(rows):
  # We have to parse the output
  nodes = set()
  edges = dict()

  for row in rows:
    words = row.split(' ')
    bag_name = words[0] + ' ' + words[1]
    nodes.add(bag_name)
    edges[bag_name] = list()
    i = 4
    if words[i] == 'no':
      continue
    while i != len(words):
      dest_bag_count = int(words[i])
      dest_bag_name = words[i+1] + ' ' + words[i+2]
      edges[bag_name].append((dest_bag_name, dest_bag_count))
      i += 4

  # for edge in edges:
  #   print("{} -> {}".format(edge, edges[edge]))
  g = Graph(nodes, edges)

  return g.count_bags("shiny gold")

if __name__ == "__main__":
  input_file = open("input.txt", "r")
  rows = input_file.readlines()
  trimmed_rows = list()
  for row in rows:
    trimmed_rows.append(row[:-1]) # Remove the newline character
  print("Number of bags within a shiny gold bag: {}".format(solve(trimmed_rows)))
