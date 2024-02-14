import sys
import math

# classes
class Point:
  def __init__(self, x, y):
    self.x = x #Float
    self.y = y #Float

class Load:
  def __init__(self, id, pickup, dropoff):
    self.id = id #Int
    self.pickup = pickup #Point
    self.dropoff = dropoff #Point

class Driver:
  def __init__(self, id):
    self.id = id #Int
    self.position = Point(0, 0) #Point
    self.depotPosition = Point(0, 0) #Point
    self.driveTime = 0 #Floatt
    self.maxTime = 12*60 #Float
    self.loads = [] #[Load]

  def deliverLoad(self, load):
    if self.enoughDeliveryTime(load):
      self.driveTime += distance(self.position, load.pickup) + distance(load.pickup, load.dropoff)
      self.position = load.dropoff
      self.loads.append(load.id)
      return True
    else:
      return False

  # check if there is enough time to deliver load and get back to depot before 12 total hours
  def enoughDeliveryTime(self, load):
    timeToDeliver = distance(self.position, load.pickup) + distance(load.pickup, load.dropoff) + distance(load.dropoff, self.depotPosition)
    return self.driveTime + timeToDeliver <= self.maxTime 




# input handling functions
def inputStringToPoint(s):
  s = s.replace("(", "")
  s = s.replace(")", "")
  nums = s.split(",")
  return Point(float(nums[0]), float(nums[1]))

def inputLineToLoad(line):
  strings = line.split(" ")
  return Load(int(strings[0]), inputStringToPoint(strings[1]), inputStringToPoint(strings[2]))

def readInput():
  inputLoads = []
  f = open(sys.argv[1], "r")
  f.readline()
  for line in f:
    inputLoads.append(inputLineToLoad(line))
  f.close()

  return inputLoads


# helper functions
def distance(point1, point2):
  return math.sqrt((point2.x - point1.x) ** 2 + (point2.y - point1.y) ** 2)


# main functions

# basic solution: one driver per load
def solution1(loads): 
  drivers = []
  for load in loads:
    newDriver = Driver(len(drivers))
    newDriver.deliverLoad(load)
    drivers.append(newDriver)

  return drivers


# main
# input
loads = readInput()

# calculation
drivers = solution1(loads)


# output
for driver in drivers:
  print(driver.loads)



