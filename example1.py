import sandbox

timeout = 5

sandboxA = sandbox.sandbox(timeout)

# Add two numbers.
print sandboxA.run(sandbox.add,4,5)

# Factoral of 5.
print sandboxA.run(sandbox.factorial, 5)

# The 10th fibonacci number.
print sandboxA.run(sandbox.fibonacci,10)
 
# Use_defined function.
def tripleSum(a,b,c):
  return sandbox.add(sandbox.add(a,b),c)

print sandboxA.run(tripleSum,1,2,3)

# Detect the indefinite loop.  
def forever():
  while True:
    pass

print sandboxA.run(forever)
