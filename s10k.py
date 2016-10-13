#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import yaml, subprocess


if __name__ == '__main__':
#    f_yaml = open("/tmp/salt-conf/Repofile", "r")
#    data = yaml.load_all(f_yaml)
#    f_yaml.close
#
#    for doc in data:
#        for k,v in doc.items():
#            print("{} -> {}".format(k, v))
#
    with open('Repofile') as info:
      info_dict = yaml.load(info)
    print(info_dict['modules'])
    #for var in info_dict['modules']['branch']:
    for var in info_dict['modules']:
        print(info_dict['mothbe/puppet-collectd'])
        #for k,v in var.items():
        #    print("{} -> {}".format(k, v))
    #print(info_dict['modules'])
