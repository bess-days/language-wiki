from model.common_enums import *
import re
class Language_Obj:
    def __init__(self, name: str, iso_code: str,  family:Family, branch: Branch, countries: int, speakers: int, scripts: list[Script]):
        self.languageName = name
        self.iso_code = iso_code
        self.languageFamily = family
        self.languageBranch = branch
        self.countriesSpoken = countries
        self.languageSpeakers = speakers
        self.languageScripts = scripts
    def get_json(self):
        return {"Name": self.languageName, "ISO-Code": self.iso_code, "Family": self.languageFamily.value[1],"Branch":self.languageBranch.value[1]  if self.languageBranch else None,  "Speakers": self.languageSpeakers, "Countries": self.countriesSpoken,"Scripts": [s.value[1] for s in self.languageScripts] }

    def __str__(self):
        return f"{self.languageName, self.languageFamily, self.languageBranch, self.languageSpeakers, self.countriesSpoken, self.languageScripts}"
