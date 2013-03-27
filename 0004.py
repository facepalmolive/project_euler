import math
import sys

"""
Largest palindrome product
Problem 4
A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 99.

Find the largest palindrome made from the product of two 3-digit numbers.
---

Intuition:

Brute force solution.
"""

def is_palindrome(num):
  """Check if a number is a palindrome by comparing it (the string form)
  with its digits reversed."""
  as_string = str(num)
  return as_string == as_string[::-1]


def main(argv=None):
  if argv is None:
    argv = sys.argv

  palindromes = [i * j for i in xrange(999) for j in xrange(i, 999)
                       if is_palindrome(i * j)]

  print max(palindromes)

if __name__ == '__main__':
  sys.exit(main())
