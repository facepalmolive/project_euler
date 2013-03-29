
import sys
import math, operator

"""
Smallest multiple
Problem 5
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

---

Intuition:

- To find the LCM of a set of numbers a0, a1, a2, ..., take the prime
factorization of each number, and raise each prime to the max power found in
any of those numbers.
- Since we're including *every* integer from 1 to 20, the max power we'll run
into is p^(floor(log(20, p)) (where log(20, p) is the log base p of 20)
"""

primes = [2, 3, 5, 7, 11, 13, 17, 19]
N = 20

def product(nums):
  """Returns product of a list of nums. Like sum(), except Python doesn't have
  a built-in prod() for some reason."""
  return reduce(operator.mul, nums, 1)


def main(argv=None):
  if argv is None:
    argv = sys.argv

  print product([p ** int(math.log(N, p)) for p in primes])


if __name__ == '__main__':
  sys.exit(main())
