__author__ = 'ja'

# -*- coding: utf-8 -*-
from model.group import Group
import os.path
import json
import random
import string
import getopt
import sys


# Чтение аргументов из командной строки
try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/groups.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    # symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix+"".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata_matrix = [
    Group(name=name, header=header, footer=footer)
    for name in ["", random_string("name_", 10)]
    for header in ["", random_string("header_", 20)]
    for footer in ["", random_string("footer_", 10)]
]

testdata = [Group(name="", header="", footer="")] + [
    Group(name=random_string("name_", 10), header=random_string("header_", 20), footer=random_string("footer_", 20))
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    out.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))
