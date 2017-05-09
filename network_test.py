# -*- coding: utf-8 -*-

from request_api.neutron import HeatManger

content = HeatManger.networks_list(param='')
print content
