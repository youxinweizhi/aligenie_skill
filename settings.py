#这是配置文件

class Base(object):
    xx=123

#正式环境
class Pro(Base):
    DEBUG=False

#开发环境
class Dev(Base):
    DEBUG=True

