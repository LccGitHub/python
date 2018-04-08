#! /usr/bin/env python

import os
import re

#('uhhshs'----->(&HuhhshsGH

str = "hshsh('1ssjs'0'jjjj'0"

pattern = "\('([^']*)'"

obj = re.search(pattern, str)

rearchstr = obj.group(1)
substr = "(&H" + rearchstr+"&H"
res1 = re.sub(pattern,substr,  str)

print str
print res1
print obj.group()
print obj.group(1)

