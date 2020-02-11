#!/usr/bin/env python3

from constraint import *

class Gear:
  def __init__(self):
    self.id = 1
    self.teeth = 10
  
  def __str__(self):
    return str(self.teeth)

class Arbor:
  def __init__(self):
    self.wheels = []
    self.rate = 0
  
  def __str__(self):
    return "wheels: [" + ", ".join(map(str, barrel.wheels)) + "] rate: " + str(self.rate)

class Train:
  def __init__(self):
    self.arbors = []
    self.gears = []
    self.links = []

def rate_constraint(links):
  constant = 1
  for pair in links:
    constant *= -1 * pair[1]
    constant /= pair[0]
  return constant

if __name__ == "__main__":
  # barrel = Arbor()
  # barrel.wheels.append(Gear())
  # barrel.wheels.append(Gear())
  # print(barrel)

  problem = Problem()

  r2 = 1/60
  r4 = 1

  problem.addVariables(["p2", "p3", "p4"], range(1,10))
  problem.addVariables(["w2", "w3"], range(10,60))

  # Fix the number of pinion leaves
  problem.addConstraint(lambda p: p == 6, ("p2",))
  problem.addConstraint(lambda p: p == 6, ("p3",))
  problem.addConstraint(lambda p: p == 6, ("p4",))

  # problem.addConstraint(lambda w2, p3, w3, p4: r4 * p4 / w3 == r2 * w2 / p3, ("w2", "p3", "w3", "p4"))
  problem.addConstraint(lambda w2, p3, w3, p4: r2 == r4 * rate_constraint([(w2, p3), (w3, p4)]), ("w2", "p3", "w3", "p4"));

  solutions = problem.getSolutions()
  print(solutions)


