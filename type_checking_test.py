# Sample functions to try typechecking in python.

def int_sum(a: int, b: int) -> int:
  for i in range(a):
    b += 1
  return b
