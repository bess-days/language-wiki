import db.mysql_repository
from model.language import *
from db.mysql_repository import *
class Services:
    def __init__(self):
        self.repo = db.mysql_repository.MysqlRepository()
    # Use case one to search for a language
    def search_lang(self, query: str):
        res = self.repo.query_language(query)
        return [r.get_json() for r in res]
    # Use case 2 to search by family
    def search_family(self, query: str):
        res = self.repo.query_family(query)
        return [r.get_json() for r in res]
    # Use case 3 to search by branch
    def search_branch(self, query: str):
        res = self.repo.query_branch(query)
        return [r.get_json() for r in res]
    # Use case 4 to search by speakers
    def search_speakers(self, min: int, max: int):
        if min < 52:
            min = 52
        if max > 1528:
            max = 1528
        res = self.repo.query_speakers(min, max)
        return [r.get_json() for r in res]
    # Use case 5 to search by countries
    def search_countries(self, min: int, max: int):
        if min < 1:
            min = 1
        if max > 74:
            max = 74
        res = self.repo.query_countries(min, max)
        return [r.get_json() for r in res]
    # Use case 6 to search by script
    def search_scripts(self, query: str):
        res = self.repo.query_scripts(query)
        return [r.get_json() for r in res]





