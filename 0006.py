
import sys
import math, operator

"""
Sum square difference
Problem 6
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025  385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

---

Intuition:

(a + b + ... + n)^2 = a^2 + b^2 + ... + n^2 +
                      2ab + 2ac + ... + 2bc + ... + 2an + 2bn
So, the difference that we want is simply finding all pairs of a through n,
multiplying these pairs together, and finding twice the sum of all these pairs.
"""

N = 100


def main(argv=None):
  if argv is None:
    argv = sys.argv

  print 2 * sum([i * j for i in xrange(1, N+1)
                       for j in xrange(1, N+1) if i < j])


if __name__ == '__main__':
  sys.exit(main())
