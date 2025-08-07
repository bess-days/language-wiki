import abc
from model.common_enums import *
from model.language import Language_Obj

class Repository(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def load_languages(self) -> list[Language_Obj]:
        raise NotImplementedError

    @abc.abstractmethod
    def languages_by_name(self, query: str) -> list[Language_Obj]:
        raise NotImplementedError

    @abc.abstractmethod
    def languages_by_family(self, query: str) -> list[Language_Obj]:
        raise NotImplementedError

    @abc.abstractmethod
    def languages_by_branch(self, query: str) -> list[Language_Obj]:
        raise NotImplementedError

    @abc.abstractmethod
    def languages_by_speakers(self, min: int, max: int) -> list[Language_Obj]:
        raise NotImplementedError

    @abc.abstractmethod
    def languages_by_countries(self, min: int, max: int) -> list[Language_Obj]:
        raise NotImplementedError

    @abc.abstractmethod
    def languages_by_scripts(self, query: str) -> list[Language_Obj]:
        raise NotImplementedError
