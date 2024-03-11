# db_migration
数据库迁移手脚架

# 使用方式：
## 1.获取代码
    git clone https://github.com/g-zhangpp/db_migration.git
## 2.修改配置文件
    vim db_migration/etc/db_migration/db_migration.conf
## 3.安装该代码包
    cd db_migration
    python setup.py sdist
    python setup.py install
## 4.生成数据库迁移文件(/var/lib/kolla/venv/lib/python3.6/site-packages/db_migration/cmd)
    python db_sync.py revision --autogenerate
## 5.迁移到数据库(/var/lib/kolla/venv/lib/python3.6/site-packages/db_migration/cmd)
    python db_sync.py upgrade --revision head
