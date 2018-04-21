#!/usr/bin/env python

from __future__ import print_function

for i in range(5):
  for j in range(5 - i):
    print("*", end="")
  print("")
