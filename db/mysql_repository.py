from db.repository import Repository
import mysql.connector
from mysql.connector import Error
import time
import os
from model.common_enums import Family, Script, Branch
from model.language import Language_Obj


class MysqlRepository(Repository):
    def __init__(self):
            super().__init__()
            import os

            config = {
                'user': os.getenv("MYSQL_USER", "root"),
                'password': os.getenv("MYSQL_PASSWORD", "strongpassword"),
                'host': os.getenv("MYSQL_HOST", "db"),
                'port': int(os.getenv("MYSQL_PORT", 3306)),
                'database': os.getenv("MYSQL_DATABASE", "languages"),
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
            "Kra-Dai": Family.KRA_DAI,
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
        sql = 'SELECT * FROM language ORDER BY name'
        self.cursor.execute(sql)
        languages = []
        for (lang_id, name, iso_code, family, branch, speakers, countries) in self.cursor.fetchall():
            script_cursor = self.connection.cursor()
            script_cursor.execute(
                'SELECT script FROM scripts WHERE lang_id = %s', (lang_id,))
            scripts = [row[0] for row in script_cursor.fetchall()]
            script_cursor.close()
            entry = {
                'lang_id': lang_id,
                'name': name,
                'iso_code': iso_code,
                'family': family,
                'branch': branch,
                'speakers': speakers,
                'countries': countries,
                'scripts': scripts
            }
            languages.append(self.mapper(entry))
        return languages




    def languages_by_name(self, query: str) -> list[Language_Obj]:
        sql = 'SELECT * FROM language WHERE name =  %s ORDER BY name'
        self.cursor.execute(sql, (query,))
        languages = []
        for (lang_id, name, iso_code, family, branch, speakers, countries) in self.cursor.fetchall():
            script_cursor = self.connection.cursor()
            script_cursor.execute(
                'SELECT script FROM scripts WHERE lang_id = %s', (lang_id,))
            scripts = [row[0] for row in script_cursor.fetchall()]
            entry = {
                'lang_id': lang_id,
                'name': name,
                'iso_code': iso_code,
                'family': family,
                'branch': branch,
                'speakers': speakers,
                'countries': countries,
                'scripts': scripts
            }
            languages.append(self.mapper(entry))
        return languages

    def languages_by_family(self, query: str) -> list[Language_Obj]:
        sql = 'SELECT * FROM language WHERE family = %s ORDER BY name'
        self.cursor.execute(sql, (query,))
        languages = []
        for (lang_id, name, iso_code, family, branch, speakers, countries) in self.cursor.fetchall():
            script_cursor = self.connection.cursor()
            script_cursor.execute(
                'SELECT script FROM scripts WHERE lang_id = %s', (lang_id,))
            scripts = [row[0] for row in script_cursor.fetchall()]
            script_cursor.close()
            entry = {
                'lang_id': lang_id,
                'name': name,
                'iso_code': iso_code,
                'family': family,
                'branch': branch,
                'speakers': speakers,
                'countries': countries,
                'scripts': scripts
            }
            languages.append(self.mapper(entry))

        return languages

    def languages_by_branch(self, query: str) -> list[Language_Obj]:
        sql = 'SELECT * FROM language WHERE branch = %s ORDER BY name'
        self.cursor.execute(sql, (query,))
        languages = []
        for (lang_id, name, iso_code, family, branch, speakers, countries) in self.cursor.fetchall():
            script_cursor = self.connection.cursor()
            script_cursor.execute(
                'SELECT script FROM scripts WHERE lang_id = %s', (lang_id,))
            scripts = [row[0] for row in script_cursor.fetchall()]
            script_cursor.close()
            entry = {
                'lang_id': lang_id,
                'name': name,
                'iso_code': iso_code,
                'family': family,
                'branch': branch,
                'speakers': speakers,
                'countries': countries,
                'scripts': scripts
            }
            languages.append(self.mapper(entry))

        return languages
    def languages_by_speakers(self, min: int, max: int):
        sql = 'SELECT * FROM language WHERE speakers BETWEEN %s AND %s ORDER BY name'
        self.cursor.execute(sql, (min, max))
        languages = []
        for (lang_id, name, iso_code, family, branch, speakers, countries) in self.cursor.fetchall():
            script_cursor = self.connection.cursor()
            script_cursor.execute(
                'SELECT script FROM scripts WHERE lang_id = %s', (lang_id,))
            scripts = [row[0] for row in script_cursor.fetchall()]
            script_cursor.close()
            entry = {
                'lang_id': lang_id,
                'name': name,
                'iso_code': iso_code,
                'family': family,
                'branch': branch,
                'speakers': speakers,
                'countries': countries,
                'scripts': scripts
            }
            languages.append(self.mapper(entry))

        return languages
    def languages_by_countries(self, min: int, max: int):
        sql = 'SELECT * FROM language WHERE countries BETWEEN %s AND %s ORDER BY name'
        self.cursor.execute(sql, (min, max))
        languages = []
        for (lang_id, name, iso_code, family, branch, speakers, countries) in self.cursor.fetchall():
            script_cursor = self.connection.cursor()
            script_cursor.execute(
                'SELECT script FROM scripts WHERE lang_id = %s', (lang_id,))
            scripts = [row[0] for row in script_cursor.fetchall()]
            script_cursor.close()
            entry = {
                'lang_id': lang_id,
                'name': name,
                'iso_code': iso_code,
                'family': family,
                'branch': branch,
                'speakers': speakers,
                'countries': countries,
                'scripts': scripts
            }
            languages.append(self.mapper(entry))
        return languages
    def languages_by_scripts(self, query: str):
        sql = "SELECT l.lang_id, l.name, l.iso_code, l.family, l.branch, l.speakers, l.countries FROM language l INNER JOIN scripts s ON l.lang_id = s.lang_id WHERE s.script = %s ORDER BY l.name"
        self.cursor.execute(sql, (query,))
        languages = []
        for (lang_id, name, iso_code, family, branch, speakers, countries) in self.cursor.fetchall():
            script_cursor = self.connection.cursor()
            script_cursor.execute(
                'SELECT script FROM scripts WHERE lang_id = %s', (lang_id,))
            scripts = [row[0] for row in script_cursor.fetchall()]
            script_cursor.close()
            entry = {
                'lang_id': lang_id,
                'name': name,
                'iso_code': iso_code,
                'family': family,
                'branch': branch,
                'speakers': speakers,
                'countries': countries,
                'scripts': scripts
            }
            languages.append(self.mapper(entry))
        return languages
