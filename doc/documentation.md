# UI
## Search By Language Name
#### Web Page
In the first entry text box, type in a language name (can be capitolized however you want as the program fixes it for you) Click submit or enter.
This should return a list of the languages that match that query (as in theory some languages have the same name.) If it returns [] that means the language does not have over 50 million speakers

Entry: `French`

Output:
```json
[
  {
    "French": {
      "Branch": "Romance",
      "Countries": 51,
      "Family": "Indo-European",
      "ISO-Code": "fr",
      "Scripts": [
        "Latin"
      ],
      "Speakers": 312
    }
  }
]
```
#### Curl
You can interact with the API with the parameter and the lang you want to search
```commandline
curl -G -d "lang=French"  http://localhost:5000/search_lang
```

---
## Search By Language Family
#### Webpage
In the next entry box is a drop down with different language families, select an option to see the languages and their information

Input: `Dravidian`

Output:
```json
[
  {
    "Kannada": {
      "Branch": "South",
      "Countries": 1,
      "Family": "Dravidian",
      "ISO-Code": "kn",
      "Scripts": [
        "Kannada"
      ],
      "Speakers": 59
    }
  },
  {
    "Tamil": {
      "Branch": "South",
      "Countries": 6,
      "Family": "Dravidian",
      "ISO-Code": "ta",
      "Scripts": [
        "Tamil"
      ],
      "Speakers": 86
    }
  },
  {
    "Telugu": {
      "Branch": "South-Central",
      "Countries": 1,
      "Family": "Dravidian",
      "ISO-Code": "te",
      "Scripts": [
        "Telugu"
      ],
      "Speakers": 96
    }
  }
]
```
#### Curl
You can interact with the API with the parameter and the lang you want to search
```commandline
curl -G -d "family=Dravidian"  http://localhost:5000/search_family
```

---
## Search By Script
#### Webpage
In the next entry box is a drop down with different language families, select an option to see the languages with the selected script and their information

Input: `Devanagari`

Output:
```json
[
  {
    "Bhojpuri": {
      "Branch": "Indo-Aryan",
      "Countries": 3,
      "Family": "Indo-European",
      "ISO-Code": "bho",
      "Scripts": [
        "Devanagari"
      ],
      "Speakers": 53
    }
  },
  {
    "Hindi": {
      "Branch": "Indo-Aryan",
      "Countries": 9,
      "Family": "Indo-European",
      "ISO-Code": "hi",
      "Scripts": [
        "Devanagari"
      ],
      "Speakers": 609
    }
  },
  {
    "Marathi": {
      "Branch": "Indo-Aryan",
      "Countries": 1,
      "Family": "Indo-European",
      "ISO-Code": "mr",
      "Scripts": [
        "Devanagari"
      ],
      "Speakers": 99
    }
  }
]
```
#### Curl
You can interact with the API with the parameter and the lang you want to search
```commandline
curl -G -d "script=Devanagari"  http://localhost:5000/search_script
```