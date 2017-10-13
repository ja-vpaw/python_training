# -*- coding: utf-8 -*-
from model.group import Group
from sys import maxsize

def test_add_new_group(app):
    old_groups = app.group.get_group_list()
    group_add = Group("dsfdsf" , header="sdfdsf" , footer="sdfsdfds")
    app.group.create(group_add)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group_add)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

def test_add_empty_group(app):
    old_groups = app.group.get_group_list()
    group_add = Group(name="" , header="" , footer="")
    app.group.create(group_add)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group_add)
    assert sorted(old_groups , key=Group.id_or_max) == sorted(new_groups , key=Group.id_or_max)