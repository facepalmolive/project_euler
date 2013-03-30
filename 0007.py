import math
import sys

"""
10001st prime
Problem 7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

---

Intuition:

- We brute-force generate a list of primes by checking every integer and seeing
if they're divisible by our current list of known primes.
- This is essentially a subcomponent of my original solution to problem 3,
which made me realize that I way overcomplicated that problem. With the exact
same reasoning as the second half of that problem, I didn't need to generate
primes at all! Guess I'll go revisit that problem after this.
"""

N = 10001

def is_prime(n, primes):
  """
  Given an integer n and a list of all primes smaller than n, test if n is
  prime. We brute-force this by checking n's divisibility against the primes
  list.
  """
  max_factor = math.sqrt(n)
  for p in primes:
    if n % p == 0:
      return False
    if p > max_factor:
      break

  return True


def main(argv=None):
  if argv is None:
    argv = sys.argv

  # list of prime numbers that we build incrementally
  primes = [2]

  while len(primes) < N:
    # Find the next prime bigger than the largest known prime so far.
    n = primes[-1] + 1
    while not is_prime(n, primes):
      n += 1

    primes.append(n)

  print primes[-1]


if __name__ == '__main__':
  sys.exit(main())
