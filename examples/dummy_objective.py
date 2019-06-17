# Example with dummy objective function

from pyomo.contrib.simplemodel import *

# A new problem
prob = SimpleModel()

# Variables
x = prob.var("x", within=Binary)
y = prob.var("y", within=Binary)

# Objective
prob += 1  # dummy

# Constraints
prob += x+y <= 1
prob += x-y >= 1

# Optimize
status = prob.solve("glpk")

# Print the model
prob.pprint()
# Display the model values
prob.display()

# Print the status of the solved LP
print("Status: %s" % status.solver.termination_condition)

# Print the value of the variables at the optimum
print("x = %f" % value(x))
print("y = %f" % value(y))

# Print the value of the objective
print("objective = %f" % value(prob.objective()))

