import signal
import __builtin__

class SandboxError(Exception):
  pass

class TimeoutError(SandboxError):
  pass


def make_secure():
  """ Clear the unsafe builtins. Reference: https://isisblogs.poly.edu/2012/10/26/escaping-python-sandboxes/ """

  UNSAFE = ['open',
            'file',
            'execfile',
            'compile',
            'reload',
            '__import__',
            'eval',
            'input',
            '__debug__',
            'raw_input',
            'intern',
            'quit',
            'BaseException',
            'SystemExit']
  for func in UNSAFE:
    try:
      del __builtin__.__dict__[func]
    except KeyError:
      continue

def checkType(value):
  """Ensure all arguments passed in belongs to the safe types""" 
  safeType = (bool, int, long, float)
  if not isinstance(value, safeType):
      raise SandboxError(value + " is not a safe type!")


def add(a,b):
  """Safe addition function. before operation is executed, checks inputs  
     format"""
  checkType(a)
  checkType(b)
  number = (int, long, float)
  if isinstance(a, number) and isinstance(b,number):
    try:
      c = a + b
    except Exception, e:
      raise SandboxError(str(e))
  else:
    raise SandboxError("Can not add bool values!")

  return c


def sub(a,b):

  """safe subtraction function. before operation is executed, checks
     inputs format"""

  checkType(a)
  checkType(b)
  number = (int, long, float)
  if isinstance(a, number) and isinstance(b,number):
    try:
      c = a - b
    except Exception, e:
      raise SandboxError(str(e))
  else:
    raise SandboxError("Can not subtract bool values!")

  return c


def mul(a,b):

  """safe multiplication function. before operation is executed, checks
     inputs format"""

  checkType(a)
  checkType(b)
  number = (int, long, float)
  if isinstance(a, number) and isinstance(b,number):
    try:
      c = a * b
    except Exception, e:
      raise SandboxError(str(e))
  else:
    raise SandboxError("Can not multiply bool values!")
    
  return c


def div(a,b):

  """safe division function. before operation is executed, checks
     inputs format"""

  checkType(a)
  checkType(b)
  number = (int, long, float)
  if isinstance(a, number) and isinstance(b,number):
    try:
      c = a / b
    except Exception, e:
      raise SandboxError(str(e))
  else:
    raise SandboxError("Can not multiply bool values!")
    
  return c


def fibonacci(n):

  """Calculates the nth fibonacci number"""
  checkType(n)
  if not isinstance(n, int):
    raise SandboxError("Only integer has fibonacci!")
  elif n < 0:
    raise SandboxError("Index of fibonacci must be positive!")
  else:
    if n <= 1:
      return 1
    else:
      return add(fibonacci(n-1), fibonacci(n-2))


def counter(n):

  """Counts and proints all numbers from n to 1"""

  checkType(n)
  if not isinstance(n, int):
    raise SandboxError("Only integer has fibonacci!")
  elif n < 0:
    raise SandboxError("Index of fibonacci must be positive!")
  else:
    while n >= 1:
      print n 
      sub(n,1)
    return 1

def factorial(n):

  """calculates factoral of n."""

  checkType(n)

  if not isinstance(n, int):
    raise SandboxError("Only integer has factoral!")
  elif n < 0:
    raise SandboxError("Number must be positive!")
  elif( n <= 1 ):
    return 1
  else:
    return( n * factorial(n-1) )


def gcd(m,n):

  """This function calculates the Greatest common divisor"""

  checkType(n)
  checkType(m)
  if not isinstance(n, int) or not isinstance (m, int):
    raise SandboxError("Only integer has gcd!")
  elif n < 1 or m < 1:
    raise SandboxError("Numbers must be positive!")
  while n > 0:
    temp = div(m,n)
    rem = sub(m, mul(temp, n))
    m = n
    n = rem

  return m 


class sandbox(object):
  def __init__(self, seconds):
    self.sig = signal.SIGALRM
    make_secure()
    self.seconds = seconds

  def safe(self):
    make_secure()

  def _handle_timeout(self,signum,frame):
    raise TimeoutError("Time is up!")

  def run(self, func, *args, **kws):
    """A container to run the code."""
    for arg in args:
      checkType(arg)
    for kw in kws:
      checkType(kw)

    signal.signal(self.sig, self._handle_timeout)
    signal.alarm(self.seconds)

    try:
      output = func(*args, **kws)
    except Exception,e:
      raise SandboxError(str(e)) 
    finally:
      signal.alarm(0)

    return output
    
