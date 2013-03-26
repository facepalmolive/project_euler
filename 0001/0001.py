import sys

"""
Multiples of 3 and 5
Problem 1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we
get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

N = 1000

def sum(interval):
  """
  Calculates (interval + 2*interval + 3*interval + ...) up until N (exclusive)

  Uses the formula (1 + 2 + 3 + ... + a) = a * (a + 1) / 2
  """

  # do not include the last element if N is a multiple of interval
  num_addends = int((N - 1) / interval)
  return interval * (num_addends * (num_addends + 1) / 2)


def main(argv=None):
  if argv is None:
    argv = sys.argv

  total_sum = sum(3)
  total_sum += sum(5)
  total_sum -= sum(15)   # we counted multiples of 15 twice

  print total_sum



if __name__ == '__main__':
  sys.exit(main())
