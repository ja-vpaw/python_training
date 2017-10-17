# -*- coding: utf-8 -*-
from model.group import Group
import pytest
import random
import string


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
    for i in range(5)
]

@pytest.mark.parametrize("group_add", testdata, ids=[repr (x) for x in testdata])
def test_add_new_group(app, group_add):
    old_groups = app.group.get_group_list()
    app.group.create(group_add)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group_add)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
