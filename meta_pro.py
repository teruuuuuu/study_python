## -*- coding: utf-8 -*-

from proto import *

########################################################################
# メタプログラミングsample
def _create_function(name, doc=""):
    """ Create a function for aggregator by name"""
    def _():
        return 1
    _.__name__ = name
    _.__doc__ = doc
    return _

name = "one"
globals()["one"] = (_create_function(name, ""))


one()
########################################################################

def main():
    prot = Prototype()
    prot.x = 7
    first = TestClass() # オブジェクトを作る
    first.prototype = prot
    prot2 = Prototype()
    prot2.x = 9
    second = TestClass() # firstと同じTextClassからインスタンスを作る
    # print(second.x) # first.xと同じオブジェクトを指しているので7になる
    # print first.x # これは7でなく9を返す
    del first.x # インスタンスのアトリビュートを消去
    #  print first.x # prototype.xの返す7になるはず


def main2():
    proc = DynamicPropery("hoge")
    proc.title()

if __name__ == "__main__":
    main()
    # main2()



