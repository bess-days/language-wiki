import model.language
import model.common_enums
from app.services import *
REPO = Services()
def test_language():
    l_test = REPO.search_by_lang("French")
    assert len(l_test) == 1
    assert type(l_test[0]) == model.language.Language_Obj
    assert l_test[0].languageName == "French"
    assert l_test[0].languageFamily == Family.INDO_EUROPEAN
    assert l_test[0].iso_code == "fr"
    assert l_test[0].languageBranch == Branch.ROMANCE
    assert l_test[0].languageSpeakers == 312
    assert l_test[0].countriesSpoken == 51


    assert type(l_test) == list
def test_family():
    f_test = REPO.search_by_family("Dravidian")
    assert len(f_test) == 3
    for lang in f_test:
        assert type(lang) == Language_Obj
    assert [lang.languageName for lang in f_test]  == [ "Kannada", "Tamil", "Thai"]
def test_branch():
    b_test = REPO.search_by_branch("Germanic")
    assert type(b_test) == list
    for lang in b_test:
        assert type(lang) == Language_Obj
    assert len(b_test) == 4
    assert [lang.languageName for lang in b_test]  == [ "English", "German"]
def test_speakers():
    s_test = REPO.search_by_speakers(50, 60)
    assert type(s_test) == list
    for lang in s_test:
        assert type(lang) == Language_Obj
    assert (len(s_test) == 6)
    assert [lang.languageName for lang in s_test] == ["Amharic", "Bhojpuri", "Kannada"]
def test_countries():
    c_test = REPO.search_by_countries(1, 13)
    assert type(c_test) == list
    for lang in c_test:
        assert type(lang) == Language_Obj
    assert (len(c_test) == 4)
    assert [lang.languageName for lang in c_test]  ==  ["Swahili", "Tagalog", "Thai"]
def test_script():
    s_test = REPO.search_by_scripts("Devanagari")
    assert type(s_test) == list
    for lang in s_test:
        assert type(lang) == Language_Obj
    assert (len(s_test) == 7)
    assert [lang.languageName for lang in s_test]  == ['Bhojpuri', 'Hindi', 'Marathi']





