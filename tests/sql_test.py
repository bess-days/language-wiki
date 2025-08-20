from db.mysql_repository import *
repo = MysqlRepository()
arabic = {
    'lang_id': 5,
    'name': 'Arabic',
    'iso_code': 'ar',
    'family': 'Afro-Asiatic',
    'branch': 'Semitic',
    'speakers': 335,
    'countries': 35,
    'scripts': ['Arabic', 'Syriac']

}
korean = {
    'lang_id': 24,
    'name': 'Korean',
    'iso_code': 'ko',
    'family': 'Koreanic',
    'branch': None,
    'speakers': 82,
    'countries': 7,
    'scripts': ['Hangul']
}
def test_map_families():
     arabic_fam = repo.map_families(arabic)
     korean_fam = repo.map_families(korean)
     assert arabic_fam == Family.AFRO_ASIATIC
     assert korean_fam == Family.KOREANIC
def test_map_branch():
    arabic_branch = repo.map_branch(arabic)
    korean_branch = repo.map_branch(korean)
    assert arabic_branch == Branch.SEMITIC
    assert korean_branch is None

def test_map_scripts():
    arabic_scripts = repo.map_scripts(arabic)
    korean_scripts = repo.map_scripts(korean)
    assert arabic_scripts[0] == Script.ARABIC
    assert  arabic_scripts[1] == Script.SYRIAC
    assert korean_scripts[0] == Script.HANGUL
def test_mapper():
    ar = repo.mapper(arabic)
    assert ar.languageName == "Arabic"
    assert ar.iso_code == "ar"
    assert ar.languageFamily == Family.AFRO_ASIATIC
    assert ar.languageBranch == Branch.SEMITIC
    assert ar.languageSpeakers == 335
    assert ar.countriesSpoken == 35
    assert ar.languageScripts == [Script.ARABIC, Script.SYRIAC]
    ko = repo.mapper(korean)
    assert ko.languageName == "Korean"
    assert ko.iso_code == "ko"
    assert ko.languageFamily == Family.KOREANIC
    assert ko.languageBranch is None
    assert ko.languageSpeakers == 82
    assert ko.countriesSpoken == 7
    assert ko.languageScripts == [Script.HANGUL]
def test_load_languages():
    languages = repo.load_languages()
    assert type(languages) == list
    for lang in languages:
        assert type(lang) == Language_Obj
    assert len(languages) == 31
