## -*- coding: utf-8 -*-

class PrototypeStore(dict):
    """ x.prototype.XXXの値を保存するためのクラス """
    def __setattr__(self, name, value):
        self[name] = value

    def __getattr__(self, name):
        return self[name]

class PrototypeMeta(type):
    """ Prototypeメタクラス(クラス生成時に呼ばれる) """
    def __new__(metacls, cls_name, bases, attrs):
        cls = type.__new__(metacls, cls_name, bases, attrs)
        cls.prototype = PrototypeStore()
        return cls

class Prototype(object):
    __metaclass__ = PrototypeMeta

    def __getattr__(self, name):
        if name == 'prototype':
            getattr(self.__class__, name)
        else:
            try:
                getattr(object, name)
            except AttributeError:
                return self.__class__.prototype[name]

class TestClass(Prototype):
    def __init__(self):
        pass


class DynamicPropery(object):
    def __init__(self, value):
        self._value = value

    def __getattr__(self, name):
        return getattr(self._value, name)


