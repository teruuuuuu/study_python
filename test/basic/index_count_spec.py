import __init__
import unittest
from basic.index_count import IndexCount
import thirdparty.pymongo.try_pymongo as T

class IndexCountSpec(unittest.TestCase):
    def test_index_count(self):
        target_group_id = 1
        i = IndexCount()
        user_index_list = i.count_user_index(target_group_id)
        # for index in user_index_list:
        #     print(index)
        answer = [{'user_id': 1, 'count': 0},
                  {'user_id': 2, 'count': 5},
                  {'user_id': 3, 'count': 0},
                  {'user_id': 4, 'count': 4},
                  {'user_id': 5, 'count': 0}]
        self.assertTrue(user_index_list == answer)

def __init_data():
    __delete_data()
    user_index_bulk_array = [
        {"user_id": 1, "group_id": 1, "index": 9, "count": 0},
        {"user_id": 2, "group_id": 1, "index": 4, "count": 3},
        {"user_id": 3, "group_id": 1, "index": 9, "count": 0},
        {"user_id": 4, "group_id": 1, "index": 5, "count": 2},
        {"user_id": 5, "group_id": 1, "index": 6, "count": 1},
        {"user_id": 1, "group_id": 2, "index": 3, "count": 0},
        {"user_id": 2, "group_id": 2, "index": 4, "count": 0},
        {"user_id": 3, "group_id": 2, "index": 3, "count": 0},
        {"user_id": 4, "group_id": 2, "index": 5, "count": 0},
        {"user_id": 5, "group_id": 2, "index": 8, "count": 0}]
    content_log_bulk_array = [
        {"group_id": 1, "index": 1, "del_flg": 0, "content": "abcdefg"},
        {"group_id": 1, "index": 2, "del_flg": 1, "content": "abcdefg"},
        {"group_id": 1, "index": 3, "del_flg": 0, "content": "abcdefg"},
        {"group_id": 1, "index": 4, "del_flg": 0, "content": "abcdefg"},
        {"group_id": 1, "index": 5, "del_flg": 0, "content": "abcdefg"},
        {"group_id": 1, "index": 6, "del_flg": 1, "content": "abcdefg"},
        {"group_id": 1, "index": 7, "del_flg": 0, "content": "abcdefg"},
        {"group_id": 1, "index": 8, "del_flg": 0, "content": "abcdefg"},
        {"group_id": 1, "index": 9, "del_flg": 1, "content": "abcdefg"},
        {"group_id": 1, "index": 10, "del_flg": 0, "content": "abcdefg"},
        {"group_id": 1, "index": 11, "del_flg": 0, "content": "abcdefg"},
        {"group_id": 2, "index": 1, "del_flg": 0, "content": "abcdefg"},
        {"group_id": 2, "index": 2, "del_flg": 0, "content": "abcdefg"},
        {"group_id": 2, "index": 3, "del_flg": 0, "content": "abcdefg"},
        {"group_id": 2, "index": 4, "del_flg": 1, "content": "abcdefg"},
        {"group_id": 2, "index": 5, "del_flg": 0, "content": "abcdefg"},
        {"group_id": 2, "index": 6, "del_flg": 0, "content": "abcdefg"},
        {"group_id": 2, "index": 7, "del_flg": 0, "content": "abcdefg"},
        {"group_id": 2, "index": 8, "del_flg": 1, "content": "abcdefg"},
        {"group_id": 2, "index": 9, "del_flg": 0, "content": "abcdefg"},
        {"group_id": 2, "index": 10, "del_flg": 1, "content": "abcdefg"}]
    T.many_insert_user_index(user_index_bulk_array)
    T.many_insert_content_log(content_log_bulk_array)

def __delete_data():
    T.all_delete_user_index()
    T.all_delete_content_log()

if __name__ == '__main__':
    __init_data()
    unittest.main()
    __delete_data()