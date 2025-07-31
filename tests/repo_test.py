import pytest
from model.language import *



LANGUAGES = [Language_Obj("French", "fr", Family.INDO_EUROPEAN, "Romance",  51, 312,  ["Latin"]),
             Language_Obj("Arabic", "ar", Family.AFRO_ASIATIC, "Semitic",35, 325,  ["Arabic", "Syriac"]),
             Language_Obj("Javanese", "jv", Family.AUSTRONESIAN, "Malayo-Polynesian",1,  69,  ["Javanese", "Latin"]),
             Language_Obj("Spanish", "es", Family.INDO_EUROPEAN, "Romance", 36, 558, ["Latin"])]


def test_languages():
    assert len(LANGUAGES) == 4
def test_language_names():
    assert LANGUAGES[0].languageName == "French"
    assert LANGUAGES[1].languageName == "Arabic"
    assert LANGUAGES[2].languageName == "Javanese"
    assert LANGUAGES[3].languageName == "Spanish"
def test_iso_codes():
    assert LANGUAGES[0].iso_code == "fr"
    assert LANGUAGES[1].iso_code == "ar"
    assert LANGUAGES[2].iso_code == "jv"
    assert LANGUAGES[3].iso_code == "es"
def test_families():
    assert LANGUAGES[0].languageFamily == Family.INDO_EUROPEAN
    assert LANGUAGES[1].languageFamily == Family.AFRO_ASIATIC
    assert LANGUAGES[2].languageFamily == Family.AUSTRONESIAN
    assert LANGUAGES[3].languageFamily == Family.INDO_EUROPEAN
def test_scripts():
    assert LANGUAGES[0].languageScripts == ["Latin"]
    assert LANGUAGES[1].languageScripts == ["Arabic", "Syriac"]
    assert LANGUAGES[2].languageScripts == ["Javanese", "Latin"]
    assert LANGUAGES[3].languageScripts == ["Latin"]

