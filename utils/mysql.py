import mysql.connector
from utils.bloom_filter import BloomFilter,read_bf
import os
import configparser


class Mysql_with_bloom:
    def __init__(self):
        parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
        config_path = os.path.join(parent_dir, 'config.ini')
        config = configparser.ConfigParser()
        config.read(config_path)

        self.bf = read_bf()
        self.conn = mysql.connector.connect(
        host=config['mysql']['host'],
        user=config['mysql']['user'],
        password=config['mysql']['password'],
        database=config['mysql']['database'],
    )
        print(f"{config['mysql']['database']} is connected.")

    def show_user(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        if not rows:
            print("No users in the table.")
        else:
            for row in rows:
                print(row)
        cursor.close()
        return rows

    def check_user(self, name):
        ## bf 判断错，直接返回。
        if not self.bf.check(name):
            print(f"bloom:{name} is not in the table.")
            return False
        ## bloom_filter 判断对，仍可能存在假正例，需要继续在数据库里查找。
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT * FROM users WHERE name = %s",(name,))
        rows = cursor.fetchall()
        if not rows:
            print(f"select:{name} is not in the table.")
            cursor.close()
            return False
        else :
            print(f"{name} is in the table, his information is :")
            for row in rows:
                print(row)
            cursor.close()
            return True

    def add_user(self,name,age):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO users (name, age) VALUES (%s, %s)", (name, age))
        cursor.close()

        self.bf.add(name)

    def delete_user(self,name):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM users WHERE name = %s", (name,))
        cursor.close()

    def clear_user(self):
        cursor = self.conn.cursor()
        cursor.execute("TRUNCATE TABLE users")
        cursor.close()

        self.bf.bit_array.setall(0)
        self.bf.save()


    def commit(self):
        self.conn.commit()
        self.bf.save()

    def close(self):
        self.conn.close()






