import pymysql

import os

DBUSER = 'admin'
DBPW = 'E6156cloud'
DBHOST = 'thumbsup.cqbpyq6u5l7q.us-east-1.rds.amazonaws.com'


class Tables:

    def __int__(self):
        pass

    @staticmethod
    def _get_connection():
        #usr = os.environ.get("DBUSER")
        #pw = os.environ.get("DBPW")
        #h = os.environ.get("DBHOST")
        usr = DBUSER
        pw = DBPW
        h = DBHOST
        conn = pymysql.connect(
            user=usr,
            password=pw,
            host=h,
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )
        return conn

    @staticmethod
    def add_table(cap, indoor):
        # retrieve current max id
        sql = "select max(table_id) from RestaurantTables.RestaurantTables;"
        conn = Tables._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql)
        result = cur.fetchone()
        max_id = result['max(table_id)']
        if max_id is None:
            tid = 0
        else:
            tid = max_id + 1

        # add table
        sql = "insert into RestaurantTables.RestaurantTables(table_id, seat_capacity, indoor) values(%s, %s, %s);"
        res = cur.execute(sql, args=(tid, cap, bool(indoor)))

        # retrieve the added table
        sql = "select * from RestaurantTables.RestaurantTables where table_id = %s;"
        res = cur.execute(sql, args=tid)
        result = cur.fetchone()
        return result

    @staticmethod
    def delete_last_table(cap, indoor):
        # retrieve the last table satisfying cap and indoor
        sql = "select max(table_id) from RestaurantTables.RestaurantTables where seat_capacity = %s and indoor = %s;"
        conn = Tables._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=(cap, indoor))
        result = cur.fetchone()
        max_id = result['max(table_id)']
        print(max_id)
        if max_id is None:
            return  # no table

        # delete the retrieved table
        sql = "Delete from RestaurantTables.RestaurantTables where table_id = %s;"
        conn = Tables._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=max_id)
        result = cur.fetchall()

        # retrieve the rest of tables satisfying cap and indoor
        sql = "select * from RestaurantTables.RestaurantTables where seat_capacity = %s and indoor = %s;"
        res = cur.execute(sql, args=(cap, indoor))
        result = cur.fetchall()

        return result

    @staticmethod
    def get_all():
        # get all tables
        sql = "SELECT * FROM RestaurantTables.RestaurantTables;"
        conn = Tables._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql)
        result = cur.fetchall()

        return result

    @staticmethod
    def get_by_number(num):
        # get tables that has more than num seats
        sql = "SELECT * FROM RestaurantTables.RestaurantTables where seat_capacity >= %s;"
        conn = Tables._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=num)
        result = cur.fetchall()

        return result

    @staticmethod
    def get_indoor(indoor):
        # get tables satisfying indoor/outdoor
        sql = "SELECT * FROM RestaurantTables.RestaurantTables where indoor=%s;"
        conn = Tables._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=indoor)
        result = cur.fetchall()

        return result

    @staticmethod
    def get_num_indoor(cap, indoor):
        sql = "SELECT * FROM RestaurantTables.RestaurantTables " + \
              "where seat_capacity >= %s and indoor=%s" + \
              "order by seat_capacity asc, table_id asc limit 1;"
        conn = Tables._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=(cap, indoor))
        result = cur.fetchall()

        return result