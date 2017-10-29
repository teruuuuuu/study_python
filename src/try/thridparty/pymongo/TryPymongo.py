#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pymongo import MongoClient

import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

mongo_client = MongoClient(os.environ.get("PYMONGO_HOST"))
db=mongo_client[os.environ.get("PYMONGO_DB")]


def init_data():
    db.user_index.delete_many({})
    db.content_log.delete_many({})
    user_index_bulk_array = [
        {"user_id":1, "group_id":1, "index":9, "count": 0}
        ,{"user_id":2, "group_id":1, "index":4, "count": 3}
        ,{"user_id":3, "group_id":1, "index":9, "count": 0}
        ,{"user_id":4, "group_id":1, "index":5, "count": 2}
        ,{"user_id":5, "group_id":1, "index":6, "count": 1}]
    db.user_index.insert_many(user_index_bulk_array).inserted_ids
    content_log_bulk_array = [
        {"group_id":1, "index":1, "del_flg": 0, "content": "abcdefg"}
        ,{"group_id":1, "index":2, "del_flg": 1, "content": "abcdefg"}
        ,{"group_id":1, "index":3, "del_flg": 0, "content": "abcdefg"}
        ,{"group_id":1, "index":4, "del_flg": 0, "content": "abcdefg"}
        ,{"group_id":1, "index":5, "del_flg": 0, "content": "abcdefg"}
        ,{"group_id":1, "index":6, "del_flg": 1, "content": "abcdefg"}
        ,{"group_id":1, "index":7, "del_flg": 0, "content": "abcdefg"}
        ,{"group_id":1, "index":8, "del_flg": 0, "content": "abcdefg"}
        ,{"group_id":1, "index":9, "del_flg": 1, "content": "abcdefg"}
        ,{"group_id":1, "index":10, "del_flg": 0, "content": "abcdefg"}
        ,{"group_id":1, "index":11, "del_flg": 0, "content": "abcdefg"}]
    db.content_log.insert_many(content_log_bulk_array).inserted_ids

def select_data():
    target_group_id = 1
    user_index_array = db.user_index.find({'group_id': target_group_id}, {'_id':0, 'user_id':1, 'index':1}).sort('index', 1)
    user_list = []
    for user in user_index_array:
        user_list.append(user)
        print(user)
    print(len(user_list))

if __name__ == '__main__':
    init_data()
    select_data()
    print("TryPymongoEnd")
