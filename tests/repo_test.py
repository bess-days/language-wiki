import pytest
from model.language import *



LANGUAGES = [Language_Obj("French", "fr", Family.Indo_European, Branch.Romance,  51, 312,  [Script.Latin]),
             Language_Obj("Arabic", "ar", Family.Afro_Asiatic, Branch.Semitic,35, 325,  [Script.Arabic, Script.Syriac]),
             Language_Obj("Javanese", "jv", Family.Austronesian, Branch.Malayo_Polynesian,1,  69,  [Script.Javanese, Script.Syriac.Latin]),
             Language_Obj("Spanish", "es", Family.Indo_European, Branch.Romance, 36, 558, [Script.Latin])]


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
    assert LANGUAGES[0].languageFamily == Family.Indo_European
    assert LANGUAGES[1].languageFamily == Family.Afro_Asiatic
    assert LANGUAGES[2].languageFamily == Family.Austronesian
    assert LANGUAGES[3].languageFamily == Family.Indo_European
def test_scripts():
    assert LANGUAGES[0].languageScripts == [Script.Latin]
    assert LANGUAGES[1].languageScripts == [Script.Arabic, Script.Syriac]
    assert LANGUAGES[2].languageScripts ==[Script.Javanese, Script.Syriac.Latin]
    assert LANGUAGES[3].languageScripts == [Script.Latin]

