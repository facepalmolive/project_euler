import math
import sys

"""
Largest prime factor
Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

---

Intuition (take 2!):

- Incrementally try each number and see if it divides into the target number.
  - If so, divide the this number into the target as many time as possible;
  this becomes our new target -- if a | N (i.e., N = ma), then any additional
  factors *must* be found in m.
  - This number is *guaranteed* to be prime. Otherwise, it would have had
  smaller prime factor, and we must have already divided out all smaller primes
  in previous iterations.
  - Do this until the target number is less than our current number. Anything
  bigger can't possibly divide into this target number, and we know that we've
  already accounted for all smaller primes.
"""

N = 600851475143

def main(argv=None):
  if argv is None:
    argv = sys.argv

  # the current candidate that we increment and test for divisibility
  n = 2

  # The target number that we're trying to factor. This gets continuously
  # whittled down because if p | N (i.e., N = mp), then any additional factors
  # must be found in m
  target = N

  # the largest prime factor of N that we've seen so far
  largest_prime_factor = 1

  # Keep finding primes, adding them to list, and seeing if they're a factor
  while target >= n:
    # Divide out as many p's out of target as possible
    while target % n == 0:
      largest_prime_factor = n
      target /= n

    n += 1

  print largest_prime_factor


if __name__ == '__main__':
  sys.exit(main())
