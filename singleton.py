def singleton(cls):
    class_instance = dict()
    def warpper(*args, **kwargs):
        if cls not in class_instance:
            class_instance[cls] = cls(*args, **kwargs)
        return class_instance[cls]
    return warpper

@singleton
class A:
    def __init__(self):
        pass

ins1 = A()
ins2 = A()

assert ins1 is ins2


class B:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(B, cls).__new__(cls)
        return cls.instance
        
    def __init__(self):
        pass


ins3 = B()
ins4 = B()

assert ins3 is ins4

# using module
# file1.py
class C:
  pass
insC = C()

# file2.py
# from file1 import insC
