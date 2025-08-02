from db.repository import Repository
import mysql.connector
from model.common_enums import Family, Script, Branch
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
            "Koreanic": Family.KOREANIC,
            "KRA_DAI": Family.KRA_DAI,
        }
        family = family_switcher.get(entry["family"])
        return family
    def map_branch(self,  entry: dict):
        branch_switcher = {
            "Balto-Slavic": Branch.BALTO_SLAVIC,
            "Bantu": Branch.BANTU,
            "Chadic": Branch.CHADIC,
            "Germanic": Branch.GERMANIC,
            "Indo-Aryan": Branch.INDO_ARYAN,
            "Iranian": Branch.IRANIAN,
            "Krio": Branch.KRIO,
            "Malayo-Polynesian": Branch.MALAYO_POLYNESIAN,
            "Oghuz": Branch.OGHUZ,
            "Romance": Branch.ROMANCE,
            "Semitic": Branch.SEMITIC,
            "Sinitic": Branch.SINITIC,
            "South": Branch.SOUTH,
            "South-Central": Branch.SOUTH_CENTRAL,
            "Vietic": Branch.VIETIC,
            "Zhuang-Tai": Branch.ZHUANG_TAI,
        }
        branch = branch_switcher.get(entry["branch"])
        return branch

    def script_helper(self, scripts: list):
        language_switcher = dict({
            "Chinese": Script.CHINESE,
            "Arabic": Script.ARABIC,
            "Gurmukhi": Script.GURMUKHI,
            "Javanese": Script.JAVANESE,
            "Syriac": Script.SYRIAC,
            "Bengali": Script.BENGALI,
            "Baybayin": Script.BAYBAYIN,
            "Devanagari": Script.DEVANAGARI,
            "Kana": Script.KANA,
            "Latin": Script.LATIN,
            "Cyrillic": Script.CYRILLIC,
            "Gujarati": Script.GUJARATI,
            "Hangul": Script.HANGUL,
            "Kannada": Script.KANNADA,
            "Saba": Script.SABA,
            "Tamil": Script.TAMIL,
            "Telugu": Script.TELUGU,
            "Thai": Script.THAI
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