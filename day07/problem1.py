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

def solve(rows):
  # We have to parse the output
  nodes = set()
  edges = dict()

  reversed_edges = dict()

  for row in rows:
    words = row.split(' ')
    bag_name = words[0] + ' ' + words[1]
    nodes.add(bag_name)
    edges[bag_name] = list()
    if bag_name not in reversed_edges:
      reversed_edges[bag_name] = list()
    i = 4
    if words[i] == 'no':
      continue
    while i != len(words):
      dest_bag_count = int(words[i])
      dest_bag_name = words[i+1] + ' ' + words[i+2]
      edges[bag_name].append((dest_bag_name, dest_bag_count))
      if dest_bag_name not in reversed_edges:
        reversed_edges[dest_bag_name] = list()
      reversed_edges[dest_bag_name].append((bag_name, dest_bag_count))
      i += 4

  # for edge in edges:
  #   print("{} -> {}".format(edge, edges[edge]))
  g = Graph(nodes, reversed_edges)

  return len(g.find_all_reachable("shiny gold"))

if __name__ == "__main__":
  input_file = open("input.txt", "r")
  rows = input_file.readlines()
  trimmed_rows = list()
  for row in rows:
    trimmed_rows.append(row[:-1]) # Remove the newline character
  print("number of bags which contain shiny gold: {}".format(solve(trimmed_rows)))
