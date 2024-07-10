from utils.mysql import Mysql_with_bloom
import utils.mysql
import os
from utils.bloom_filter import BloomFilter
import time
import os



## connect
mysql = Mysql_with_bloom()
mysql.clear_user()
mysql.add_user("robb",18)
print("------------------after add user -------------------")
mysql.show_user()
print("-----------------check user exist------------------")
mysql.check_user("robb")
print("---------------check user doesn't exist---------------")
mysql.check_user("miya")
mysql.commit()  ## save to the disk
mysql.close()

## reconnect
print("-----------------reconnect------------------")
mysql = Mysql_with_bloom()
mysql.check_user("robb")
mysql.check_user("miya")
mysql.clear_user()
mysql.close()

print("-----------------reconnect------------------")
mysql = Mysql_with_bloom()
mysql.check_user("robb")
mysql.check_user("miya")
mysql.clear_user()
mysql.close()











