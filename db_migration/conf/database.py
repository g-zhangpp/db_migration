# -*- coding: utf-8 -*-
# @Author: zhangpanpan
# @Time: 2024/3/11
from oslo_config import cfg
from oslo_db import options


database_group = cfg.OptGroup(name='database',
                              title='Options for Magnum Database')

sql_opts = [
    cfg.StrOpt('mysql_engine',
               default='InnoDB',
               help='MySQL engine to use.')
]


def register_opts(conf):
    conf.register_group(database_group)
    conf.register_opts(sql_opts, group=database_group)
    options.set_defaults(conf)


def list_opts():
    return {
        database_group: sql_opts
    }
