# -*- coding: utf-8 -*-
from os import path


class Config(object):
    DEBUG = False
    TESTING = False
    ROOT_DIR = path.abspath(path.dirname(path.join(__file__)))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///%s/test.db" % (ROOT_DIR)
    SECRET_KEY = "\x62\x27\x25\x5c\x78\x61\x38\x73\x5c\x78\x38\x65\x5c\x78\x38\x33\x3b\x7c\x5c\x78\x61\x31\x68\x5c\x78\x65\x38\x53\x68\x6f\x5c\x78\x66\x31\x5c\x78\x30\x33\x7a\x5c\x78\x63\x32\x5c\x78\x39\x31\x5a\x5f\x5c\x78\x62\x35\x4e\x5c\x78\x31\x37\x5c\x78\x61\x30\x27"


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = "mysql://user:password@localhost/foo"
    SQLALCHEMY_POOL_SIZE = 100
    SQLALCHEMY_POOL_RECYCLE = 280
    SQLALCHEMY_NATIVE_UNICODE = True
