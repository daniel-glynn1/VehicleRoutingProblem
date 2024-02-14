import sys

loads = []

class Point:
  def __init__(self, x, y):
    self.x = x  # Float
    self.y = y  # Float

class Load:
  def __init__(self, id, pickup, dropoff):
    self.id = id            # Int
    self.pickup = pickup    # Point
    self.dropoff = dropoff  # Point

# process input functions
def inputStringToPoint(s):
  s = s.replace("(", "")
  s = s.replace(")", "")
  nums = s.split(",")
  return Point(float(nums[0]), float(nums[1]))

def inputLineToLoad(line):
  strings = line.split(" ")
  return Load(int(strings[0]), inputStringToPoint(strings[1]), inputStringToPoint(strings[2]))


f = open(sys.argv[1], "r")
f.readline()
for line in f:
  loads.append(inputLineToLoad(line))

for load in loads:
  print(load.pickup.x, load.pickup.y, load.dropoff.x, load.dropoff.y)

f.close()

