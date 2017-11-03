#!/usr/bin/env python
# -*- coding: utf-8 -*-
import __init__
from pymongo import MongoClient

import config.global_config as Config

mongo_client = MongoClient(Config.PYMONGO_HOST)
db = mongo_client[Config.PYMONGO_DB]

def select_user_index_by_group_id(target_group_id):
    user_index_array = db.user_index.find({'group_id': target_group_id}, {'_id':0, 'user_id':1, 'index':1}).sort('user_id', 1)
    user_list = []
    for user in user_index_array:
        user_list.append(user)
    return user_list

def many_insert_user_index(user_index_bulk_array):
    return db.user_index.insert_many(user_index_bulk_array).inserted_ids

def all_delete_user_index():
    db.user_index.delete_many({})

def select_content_log_by_group_id(target_group_id):
    content_log_array = db.content_log.find({'group_id': target_group_id, 'del_flg': 0}, {'_id':0, 'index':1}).sort('index', 1)
    content_index_list = {}
    count = 1
    for index in content_log_array:
        content_index_list[index['index']] = count
        count += 1
    return content_index_list

def many_insert_content_log(content_log_bulk_array):
    db.content_log.insert_many(content_log_bulk_array).inserted_ids

def all_delete_content_log():
    db.content_log.delete_many({})


if __name__ == '__main__':
    print("Start TryPymongo")
    #
    print("End TryPymongo")
