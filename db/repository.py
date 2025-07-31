import abc
from model.common_enums import *
from model.language import Language_Obj

class Repository(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def load_languages(self) -> list[Language_Obj]:
        raise NotImplementedError