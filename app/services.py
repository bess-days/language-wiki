from model.language import *
from db.mysql_repository import *
class Services:
    def __init__(self):
        self.repo = MysqlRepository()

    def load_languages_json(self) -> list[dict]:
        languages = self.repo.load_languages()
        return [lang.get_json() for lang in languages]
    # Use case one to search for a language

    def search_by_lang(self, query: str) -> list[dict]:
        res = self.repo.languages_by_name(query)
        return [r.get_json() for r in res]
    # Use case 2 to search by family
    def search_by_family(self, query: str) -> list[dict]:
        res = self.repo.languages_by_family(query)
        return [r.get_json() for r in res]
    # Use case 3 to search by branch
    def search_by_branch(self, query: str) -> list[dict]:
        res = self.repo.languages_by_branch(query)
        return [r.get_json() for r in res]
    # Use case 4 to search by speakers
    def search_by_speakers(self, min: int, max: int) -> list[dict]:
        if min < 52:
            min = 52
        if max > 1528:
            max = 1528
        res = self.repo.languages_by_speakers(min, max)
        return [r.get_json() for r in res]
    # Use case 5 to search by countries
    def search_by_countries(self, min: int, max: int) -> list[dict]:
        if min < 1:
            min = 1
        if max > 74:
            max = 74
        res = self.repo.languages_by_countries(min, max)
        return [r.get_json() for r in res]
    # Use case 6 to search by script
    def search_by_scripts(self, query: str) -> list[dict]:
        res = self.repo.languages_by_scripts(query)
        return [r.get_json() for r in res]





