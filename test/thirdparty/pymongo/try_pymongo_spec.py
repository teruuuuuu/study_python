import __init__
import unittest
import thirdparty.pymongo.try_pymongo as T

class TryPymongoSpec(unittest.TestCase):
    def test_insert_user_index(self):
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
        T.many_insert_user_index(user_index_bulk_array)
        insert_result = T.select_user_index_by_group_id(1)
        answer = [{"user_id": 1, "index": 9},
                  {"user_id": 2, "index": 4},
                  {"user_id": 3, "index": 9},
                  {"user_id": 4, "index": 5},
                  {"user_id": 5, "index": 6}]
        self.assertTrue(insert_result == answer)
        # for user in insert_result:
        #     print(user)


def __delete_data():
    T.all_delete_user_index()
    T.all_delete_content_log()

if __name__ == '__main__':
    __delete_data()
    unittest.main()