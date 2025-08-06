import db.mysql_repository
from model.language import *
from db.mysql_repository import *
class Services:
    def __init__(self):
        self.repo = db.mysql_repository.MysqlRepository()
    def search_lang(self, query: str):
        res = self.repo.query_language(query)
        results = []
        for r in res:
            results.append(r.get_json())
        return results
    def search_family(self, query: str):
        res = self.repo.query_family(query)
        results = []
        for r in res:
            results.append(r.get_json())
        return results
    def search_branch(self, query: str):
        res = self.repo.query_branch(query)
        results = []
        for r in res:
            results.append(r.get_json())
        return results
    def search_speakers(self, min: int, max: int):
        results = []
        if min < 52:
            min = 52
        if max > 1528:
            max = 1528
        res = self.repo.query_speakers(min, max)
        for r in res:
            results.append(r.get_json())
        return results

    def search_countries(self, min: int, max: int):
        results = []
        if min < 1:
            min = 1
        if max > 74:
            max = 74
        res = self.repo.query_countries(min, max)
        for r in res:
            results.append(r.get_json())
        return results
    def search_scripts(self, query: str):
        results = []
        languages  = self.repo.load_languages()
        for lang in languages:
            if query in lang.get_json()["Scripts"]:
                results.append(lang.get_json())
        return results





