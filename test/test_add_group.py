# -*- coding: utf-8 -*-
#import pytest
from model.group import Group
# from data.groups import testdata
# from data.add_group import constant as testdata


# @pytest.mark.parametrize("group_add", testdata, ids=[repr (x) for x in testdata])
def test_add_new_group(app, json_groups):
    group_add = json_groups
    old_groups = app.group.get_group_list()
    app.group.create(group_add)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group_add)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
