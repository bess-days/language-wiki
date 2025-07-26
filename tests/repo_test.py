import pytest
from model.objects import *

REPO = LanguageRepository()
REPO.add_language(Language("French", "fr", "Indo-European", "Romance",  ["Latin"],  51, 312))
REPO.add_language(Language("Arabic", "ar", "Afro-Asiatic", "Semitic", ["Arabic", "Syrian"],35, 325))
REPO.add_language(Language("Javanese", "jv", "Austronesian", "Malayo-Polynesian", ["Javanese", "Latin"],1,  69))
REPO.add_language(Language("Spanish", "es", "Indo-European", "Romance", ["Latin"], 36, 558))
def test_languages():
    assert len(REPO.languages) == 4
def test_language_names():
    assert REPO.languages[0].languageName == "French"
    assert REPO.languages[1].languageName == "Arabic"
    assert REPO.languages[2].languageName == "Javanese"
    assert REPO.languages[3].languageName == "Spanish"
def test_language_queries():
    search= Search(REPO)
    assert search.search_language("French").languageName == "French"
def test_family():
    search = Search(REPO)
    assert len(search.search_family("Indo-European")) == 2
def test_branch():
    search = Search(REPO)
    assert len(search.search_branch("Romance")) == 2
    assert len(search.search_branch("Semitic")) == 1
    assert len(search.search_branch("Malayo-Polynesian")) == 1
def test_script():
    search = Search(REPO)
    assert len(search.search_script("Latin")) == 3
    assert len(search.search_script("Arabic")) == 1
    assert len(search.search_script("Javanese")) == 1
def test_speakers():
    search = Search(REPO)
    assert len(search.search_speakers("300 - 700")) == 3
    assert len(search.search_speakers("50 - 75")) == 1
def test_countries():
    search = Search(REPO)
    assert len(search.search_countries("31-50")) == 2
    assert len(search.search_countries("1")) == 1
