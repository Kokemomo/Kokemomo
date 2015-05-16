#!/usr/bin/env python
# -*- coding: utf-8 -*-

from kokemomo.plugins.engine.controller.km_engine import *
from kokemomo.plugins.engine.controller.km_login import *
from kokemomo.plugins.engine.controller.km_plugin import create_base_plugin, add_route

__author__ = 'hiroki'


plugin = create_base_plugin()

add_route(plugin, {'rule':'/engine/js/<filename>','method':'GET', 'target':js_static, 'name':'static_js'})
add_route(plugin, {'rule':'/engine/css/<filename>','method':'GET', 'target':css_static, 'name':'static_css'})
add_route(plugin, {'rule':'/engine/img/<filename>','method':'GET', 'target':img_static, 'name':'static_img'})


add_route(plugin, {'rule':'/top','method':'GET', 'target':load})
add_route(plugin, {'rule':'/error','method':'GET', 'target':engine_error})
add_route(plugin, {'rule':'/login','method':'GET', 'target':login})

