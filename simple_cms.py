#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import kokemomo

argc = len(sys.argv)
port = None
if argc > 1:
    argv_list = sys.argv
    for index, value in enumerate(argv_list):
        if value == '-p':
            port = argv_list[index+1]

# Application launch point.
kokemomo.app_run(port)
