

class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
            cls._instance.initialize()
        return cls._instance
    
    def initialize(self):
        self.param = None
        

s1 = Singleton()
s2 = Singleton()

s1.param = "one"
print(s1.param, s2.param)




# Another way to implement Singleton pattern


class SingeltionMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingeltionMeta):
    def __init__(self):
        self.param = None


s1 = Singleton()
s2 = Singleton()
print(s1 is s2)