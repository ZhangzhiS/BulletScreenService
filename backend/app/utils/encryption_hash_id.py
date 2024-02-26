#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app.core.config import settings
import hashids


class EncryptionHashIds(object):

    @property
    def __hashids(self):
        return hashids.Hashids(salt=settings.HASHID_SALT, min_length=16)

    def encode(self, old_id):
        return self.__hashids.encode(old_id, 6666)

    def decode(self, h):
        try:
            res = self.__hashids.decode(h)
            if res:
                return res[0]
            else:
                return None
        except IndexError:
            return None


encrypt = EncryptionHashIds()


if __name__ == '__main__':
    i = 1
    r = encrypt.encode(i)
    d = encrypt.decode(r)
