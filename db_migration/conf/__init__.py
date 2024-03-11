# -*- coding: utf-8 -*-
# @Author: zhangpanpan
# @Time: 2024/3/11
from oslo_config import cfg
from db_migration.conf import database


CONF = cfg.CONF

database.register_opts(CONF)
