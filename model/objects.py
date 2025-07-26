class Language:
    def __init__(self, name: str, iso_code: str,  family:str, branch: str, scripts: list, countries: int, speakers: int):
        self.languageName = name
        self.iso_code = iso_code
        self.languageFamily = family
        self.languageBranch = branch
        self.languageScripts = scripts
        self.countriesSpoken = countries
        self.languageSpeakers = speakers
class LanguageRepository:
    def __init__(self):
        self.languages = []
    def add_language(self, language: Language):
        self.languages.append(language)
    def get_languages(self):
        return self.languages
class Search:
    def __init__(self, language_repository: LanguageRepository):
        self.language_repository = language_repository
    def search_language(self, query: str):
        for language in self.language_repository.get_languages():
            if language.languageName == query:
                return language
        return None
    def search_family(self, query: str):
        results = []
        for language in self.language_repository.get_languages():
            if language.languageFamily == query:
                results.append(language)
        return results
    def search_branch(self, query: str):
        results = []
        for language in self.language_repository.get_languages():
            if language.languageBranch == query:
                results.append(language)
        return results
    def search_script(self, query:str):
        results = []
        for language in self.language_repository.get_languages():
            if query in language.languageScripts:
                results.append(language)
        return results

    def search_countries(self, query: str):
        results = []
        for language in self.language_repository.get_languages():
            if query == "1" and language.countriesSpoken < 2:
                results.append(language)
            if query == "2-10" and 2<= language.countriesSpoken<=10:
                results.append(language)
            if query == "11-20" and 11 <= language.countriesSpoken <= 20:
                results.append(language)
            if query == "21-30" and 21 <= language.countriesSpoken <= 30:
                results.append(language)
            if query == "31-50" and 31 <= language.countriesSpoken <= 50:
                results.append(language)
            if query == "Over 50 countries" and language.countriesSpoken >= 50:
                results.append(language)
        return results
    def search_speakers(self, query: str):
        results = []
        for language in self.language_repository.get_languages():
            if query == "50 - 75" and 50 <= language.languageSpeakers <= 75:
                results.append(language)
            if query == "76 - 100" and 76 <= language.languageSpeakers <= 100:
                results.append(language)
            if query == "101 - 200" and 101 <= language.languageSpeakers <= 200:
                results.append(language)
            if query == "201 - 300" and 201 <= language.languageSpeakers <= 300:
                results.append(language)
            if query == "300 - 700" and 300 <= language.languageSpeakers <= 700:
                results.append(language)
            if query == "More than a billion" and language.languageSpeakers >= 1000:
                results.append(language)
        return results





