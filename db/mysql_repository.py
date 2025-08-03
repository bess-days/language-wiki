from db.repository import Repository
import mysql.connector
from model.common_enums import Family, Script, Branch
from model.language import Language_Obj
import os


class MysqlRepository(Repository):
    def __init__(self):
        super().__init__()
        import os

        config = {
            'user': os.getenv('MYSQL_USER', 'root'),
            'password': os.getenv('MYSQL_PASSWORD', 'strongpassword'),
            'host': os.getenv('MYSQL_HOST', 'localhost'),
            'port': int(os.getenv('MYSQL_PORT', 32000)),  # 32000 default for local Docker setup
            'database': os.getenv('MYSQL_DB', 'languages'),
        }

        self.connection = mysql.connector.connect(**config)
        self.cursor = self.connection.cursor()
    def map_families(self, entry: dict) -> Family:
        family_switcher = {
            "Indo-European": Family.Indo_European,
            "Sino-Tibetan": Family.Sino_Tibetan,
            "Afro-Asiatic": Family.Afro_Asiatic,
            "Austronesian": Family.Austronesian,
            "Japonic": Family.Japonic,
            "Austroasiatic": Family.Austroasiatic,
            "Dravidian": Family.Dravidian,
            "Turkic": Family.Turkic,
            "Niger-Congo": Family.Niger_Congo,
            "Koreanic": Family.Koreanic,
            "KRA_DAI": Family.Kra_Dai,
        }
        family = family_switcher.get(entry["family"])
        return family
    def map_branch(self,  entry: dict):
        branch_switcher = {
            "Balto-Slavic": Branch.Balto_Slavic,
            "Bantu": Branch.Bantu,
            "Chadic": Branch.Chadic,
            "Germanic": Branch.Germanic,
            "Indo-Aryan": Branch.Indo_Aryan,
            "Iranian": Branch.Iranian,
            "Krio": Branch.Krio,
            "Malayo-Polynesian": Branch.Malayo_Polynesian,
            "Oghuz": Branch.Oghuz,
            "Romance": Branch.Romance,
            "Semitic": Branch.Semitic,
            "Sinitic": Branch.Sinitic,
            "South": Branch.South,
            "South-Central": Branch.South_Central,
            "Vietic": Branch.Vietic,
            "Zhuang-Tai": Branch.Zhuang_Tai,
        }
        branch = branch_switcher.get(entry["branch"])
        return branch

    def script_helper(self, scripts: list):
        language_switcher = dict({
            "Chinese": Script.Chinese,
            "Arabic": Script.Arabic,
            "Gurmukhi": Script.Gurmukhi,
            "Javanese": Script.Javanese,
            "Syriac": Script.Syriac,
            "Bengali": Script.Bengali,
            "Baybayin": Script.Baybayin,
            "Devanagari": Script.Devanagari,
            "Kana": Script.Kana,
            "Latin": Script.Latin,
            "Cyrillic": Script.Cyrillic,
            "Gujarati": Script.Gujarati,
            "Hangul": Script.Hangul,
            "Kannada": Script.Kannada,
            "Saba": Script.Saba,
            "Tamil": Script.Tamil,
            "Telugu": Script.Telugu,
            "Thai": Script.Thai
        })
        results = []
        for s in scripts:
            results.append(language_switcher[s])
        return results
    def map_scripts(self, entry: dict):
        return  self.script_helper(entry["scripts"])
    def mapper(self, entry: dict) -> Language_Obj:
        language_obj = Language_Obj(
            name=entry.get('name'),
            iso_code =entry.get('iso_code'),
            family=self.map_families(entry),
            branch=self.map_branch(entry),
            speakers=entry.get('speakers'),
            countries=entry.get('countries'),
            scripts=self.map_scripts(entry),
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
        sql2 = 'SELECT lang_id, script FROM scripts'
        self.cursor.execute(sql2)
        entries_dict = {entry['lang_id']: entry for entry in entries}
        for lang_id, script in self.cursor:
            if lang_id in entries_dict:
                entries_dict[lang_id]['scripts'].append(script)
        language_repo = [self.mapper(entry) for entry in entries_dict.values()]
        return language_repo