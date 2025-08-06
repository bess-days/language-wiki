from app.services import *
REPO = Services()
def test_language():
    l_test = REPO.search_lang("French")
    assert len(l_test) == 1
    for lang in l_test:
        assert lang.get("Name") == "French"
        assert lang.get("ISO-Code") == "fr"
        assert lang.get("Family") == "Indo-European"
        assert lang.get("Branch") == "Romance"
        assert lang.get("Speakers") == 312
        assert lang.get("Countries") == 51
        assert lang.get("Scripts") == ["Latin"]
        assert type(lang) == dict
def test_family():
    names = []
    f_test = REPO.search_family("Afro-Asiatic")
    assert len(f_test) == 3
    for lang in f_test:
        assert lang.get("Family") == "Afro-Asiatic"
        names.append(lang.get("Name"))
    assert names == [ "Amharic", "Arabic", "Hausa"]
def test_branch():
    names = []
    b_test = REPO.search_branch("Romance")
    assert len(b_test) == 4
    for lang in b_test:
        assert lang.get("Branch") == "Romance"
        names.append(lang.get("Name"))
    assert names == [ "French", "Italian", "Portuguese", "Spanish"]
def test_speakers():
    names = []
    s_test = REPO.search_speakers(50, 70)
    assert (len(s_test) == 6)
    for lang in s_test:
        names.append(lang.get("Name"))
    assert names == ["Amharic", "Bhojpuri", "Gujarati", "Italian", "Javanese", "Kannada"]
def test_countries():
    names = []
    c_test = REPO.search_countries(30, 80)
    assert (len(c_test) == 4)
    for lang in c_test:
        names.append(lang.get("Name"))
    assert names == ["Arabic", "English", "French", "Spanish"]
def test_script():
    names = []
    s_test = REPO.search_scripts("Arabic")
    assert (len(s_test) == 7)
    for lang in s_test:
        names.append(lang.get("Name"))
    assert names == ['Arabic', 'Hausa', 'Javanese', 'Persian', 'Punjabi', 'Swahili', 'Urdu']





