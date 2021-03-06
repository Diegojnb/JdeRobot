#!/usr/bin/env python
# -*- coding: utf-8 -*-

import kurt
import os

# get current working directory
path = os.getcwd()
path = path[:path.rfind('src')] + 'data/'

# load the scratch project
p = kurt.Project.load(path + 'test_scratch2.sb2')

# show the blocks included
for scriptable in p.sprites + [p.stage]:
    for script in scriptable.scripts:
        s = script

# change number of steps for the move block
s.blocks[1].args = [20]

# save modifications
p.save(path + 'test_scratch2_modified.sb2')
