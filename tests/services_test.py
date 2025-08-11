from app.services import *
REPO = Services()
def test_language():
    l_test = REPO.search_by_lang("French")
    assert len(l_test) == 1
    assert type(l_test) == list
    print(l_test)
def test_family():
    f_test = REPO.search_by_family("Afro-Asiatic")
    print(f_test)
    assert type(f_test) == list
    for lang in f_test:
        assert type(lang) == dict
    assert len(f_test) == 3
    assert [key for lang in f_test for key in lang.keys()]  == [ "Amharic", "Arabic", "Hausa"]
def test_branch():
    b_test = REPO.search_by_branch("Romance")
    assert type(b_test) == list
    for lang in b_test:
        assert type(lang) == dict
    assert len(b_test) == 4
    assert [key for lang in b_test for key in lang.keys()]  == [ "French", "Italian", "Portuguese", "Spanish"]
def test_speakers():
    s_test = REPO.search_by_speakers(50, 70)
    assert type(s_test) == list
    for lang in s_test:
        assert type(lang) == dict
    assert (len(s_test) == 6)
    assert [key for lang in s_test for key in lang.keys()]  == ["Amharic", "Bhojpuri", "Gujarati", "Italian", "Javanese", "Kannada"]
def test_countries():
    c_test = REPO.search_by_countries(30, 80)
    assert type(c_test) == list
    for lang in c_test:
        assert type(lang) == dict
    assert (len(c_test) == 4)
    assert [key for lang in c_test for key in lang.keys()]  ==  ["Arabic", "English", "French", "Spanish"]
def test_script():
    s_test = REPO.search_by_scripts("Arabic")
    assert type(s_test) == list
    for lang in s_test:
        assert type(lang) == dict
    assert (len(s_test) == 7)
    assert [key for lang in s_test for key in lang.keys()]  == ['Arabic', 'Hausa', 'Javanese', 'Persian', 'Punjabi', 'Swahili', 'Urdu']





