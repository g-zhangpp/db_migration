# db_migration
数据库迁移手脚架

# 使用方式：
## 1.将代码移动到linux平台中。
## 2.将etc/db_migration目录移动到linux的/etc下，并修改配置文件
cp -r db_migration/etc/db_migration /etc/
## 3.将./db_migration移动到python的路径下
cp -r db_migration/db_migration /var/lib/kolla/venv/lib/python3.6/site-packages/
## 4.生成数据库迁移文件(/var/lib/kolla/venv/lib/python3.6/site-packages/db_migration/cmd)
    python db_sync.py revision --autogenerate
## 5.迁移到数据库(/var/lib/kolla/venv/lib/python3.6/site-packages/db_migration/cmd)
    python db_sync.py upgrade --revision head
