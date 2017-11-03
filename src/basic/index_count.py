import __init__
import thirdparty.pymongo.try_pymongo as T
from operator import itemgetter

class IndexCount:
    def count_user_index(self, target_group_id):
        user_index_list = T.select_user_index_by_group_id(target_group_id)
        content_index_list = T.select_content_log_by_group_id(target_group_id)
        return self.__count_index(user_index_list, content_index_list)

    def __count_index(self, user_index_list, content_index_list):
        count = len(content_index_list)
        last_index = content_index_list[count - 1]
        for user in user_index_list:
            # if(content_index_list.has_key(user['index'])): python2系
            if (user['index'] in content_index_list):
                user['count'] = count - content_index_list[user['index']]
            else:
                user['count'] = 0
                for i in range(user['index'], last_index):
                    # if(content_index_list.has_key(i)): python 2系
                    if (i in content_index_list):
                        cach_index_count = content_index_list[i] - 1
                        user['count'] = count - cach_index_count
                        for j in range(user['index'], i):
                            content_index_list[j] = cach_index_count
                        break
        ret = []
        for new_index in sorted(user_index_list, key=itemgetter('user_id'), reverse=False):
            ret.append({'user_id': new_index['user_id'], 'count': new_index['count']})
        return ret
        # return user_index_list

if __name__ == '__main__':
    print("Start IndexCount")
    print("End IndexCount")