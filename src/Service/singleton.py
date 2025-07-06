from typing import Type


class SingletonMeta(Type):
    __instance = {}

    def __call__(cls, *args, **kwargs):

        if cls not in cls.__instance:
            cls.__instance[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
            return cls.__instance[cls]
        else:
            return cls.__instance[cls]
