from db.repository import Repository
import mysql.connector
from mysql import *

from model.common_enums import Family
from model.language import Language_Obj


class MysqlRepository(Repository):
    def __init__(self):
        super().__init__()
        config = {
            'user': 'root',
            'password': 'strongpassword',
            'host': 'localhost',
            'port': 32000,
            'database': 'languages',
        }
        self.connection = mysql.connector.connect(**config)
        self.cursor = self.connection.cursor()
    def map_families(self, entry: dict) -> Family:
        family_switcher = {
            "Indo-European": Family.INDO_EUROPEAN,
            "Sino-Tibetan": Family.SINO_TIBETAN,
            "Afro-Asiatic": Family.AFRO_ASIATIC,
            "Austronesian": Family.AUSTRONESIAN,
            "Japonic": Family.JAPONIC,
            "Austroasiatic": Family.AUSTROASIATIC,
            "Dravidian": Family.DRAVIDIAN,
            "Turkic": Family.TURKIC,
            "Niger-Congo": Family.NIGER_CONGO,
            "Korean": Family.KOREANIC,
            "KRA_DAI": Family.KRA_DAI,
        }
        family = family_switcher.get(entry["family"])
        return family
    def fix_scripts(self,  entry: dict):
        scripts = entry["scripts"].split(",").strip()
        return scripts

    def mapper(self, entry: dict) -> Language_Obj:
        language_obj = Language_Obj(
            name=entry.get('name'),
            iso_code =entry.get('iso_code'),
            family=self.map_families(entry),
            branch=entry.get('branch'),
            speakers=entry.get('speakers'),
            countries=entry.get('countries'),
            scripts=entry.get('scripts'),




        )
        return language_obj
    def load_languages(self) -> list[Language_Obj]:
        sql = 'SELECT * FROM language'
        self.cursor.execute(sql)
        entries = [{
            'lang_id': lang_id,
            'name': name,
            'iso_code': iso_code,
            'family': family,
            'branch': branch,
            'speakers': speakers,
            'countries': countries,
            'scripts': []
        }
        for (lang_id, name, iso_code, family, branch, speakers, countries) in self.cursor]
        self.cursor.execute('SELECT lang_id, script FROM scripts')
        entries_dict = {entry['lang_id']: entry for entry in entries}
        for lang_id, script in self.cursor:
            if lang_id in entries_dict:
                entries_dict[lang_id]['scripts'].append(script)
        language_repo = [self.mapper(entry) for entry in entries_dict.values()]
        return language_repo

repo = MysqlRepository()

for lang in repo.load_languages():
    print(lang)