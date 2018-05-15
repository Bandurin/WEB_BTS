# -*- coding: utf-8 -*-

hash = '1234'

def check(passwd,hash):
    if passwd == hash:
        return True
    else:
        return False



print(check('1s234',hash))