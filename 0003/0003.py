import math
import sys

"""
Largest prime factor
Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

N = 600851475143

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


def find_next_prime(primes):
  """
  Find the next prime bigger than the largest element of primes.
  """
  n = primes[-1] + 1
  while not is_prime(n, primes):
    n += 1

  return n


def main(argv=None):
  if argv is None:
    argv = sys.argv

  # list of prime numbers that we build incrementally
  primes = [2]

  # largest prime factor of N we've seen so far
  largest_prime_factor = 1

  # The target number that we're trying to factor. This gets continuously
  # whittled down because if p | N (i.e., N = mp), then any additional factors
  # must be found in m
  target = N

  # We keep finding primes and adding them to the list.
  # We can stop when target < biggest prime in list, because we've guaranteed
  # to have divided out any smaller prime factors in earlier iterations
  while target > primes[-1]:
    p = find_next_prime(primes)
    primes.append(p)

    # Divide out as many p's out of target as possible
    while target % p == 0:
      largest_prime_factor = p
      target /= p

  print largest_prime_factor


if __name__ == '__main__':
  sys.exit(main())
