# Language Wiki
This is an interactive webpage that can allow you to find languages that match queries related to things like name, language family, and script for languages with over 50 million speakers. I've always loved learning about languages, even if I don't speak them.
#### Utilizes
- Object Oriented programming and Test Driven Development
- Python
- Web Scraping
- SQL DB management
- Docker container
- Flask API
- HTML and CSS
## Table of Contents
- [Installation](#installation)
- [Directory](#directory-set-up)
- [Usage](#usage)
- [Sources](#sources)

# Installation
## Prerequisites
- Python  3.9
- Docker
- Browser
## Installation
1. Clone the repository:
   2. `git clone https://github.com/bess-days/language-wiki.git`
   3. `cd language-wiki`
   4. Open in a IDE

2. Run docker
`docker-compose up --build`
Make sure it is running
3. Open `web/wiki.html`





## Directory set up
The repository is organized into several directories, each serving a specific purpose:

```app/```: Contains the main application code.

```data/```: Holds datasets and webscraping files.

```db/```: Includes database-related scripts and configurations.

```doc/```: Provides documentation and guides.

```model/```: Establishes objects.

```tests/```: Holds unit tests and test data.

```web/``` Includes the website html and css.
## Usage
## Queries
- [Search By Language](#Language)
- [Search by Language Family](#family)
- [Search by Language Branch](#branch)
- [Search by Speakers (Millions)](#speakers)
- [Search by Number of Countries Spoken](#countries)
### Language
##### Web Page
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
##### Curl
You can interact with the API with the parameter and the lang you want to search
```commandline
curl -G -d "lang=French"  http://localhost:5000/search_lang
```

---
### Family
##### Webpage
In the next entry box is a drop down with different language families, select an option to see the languages and their information.

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
##### Curl
You can interact with the API with the parameter and the family you want to search
```commandline
curl -G -d "family=Dravidian"  http://localhost:5000/search_family
```
---
### Branch
##### Webpage
In the next entry box is a drop down with different language branches, select an option to see the languages and their information.

Input: `Germanic`

Output:
```json
[
  {
    "English": {
      "Branch": "Germanic",
      "Countries": 74,
      "Family": "Indo-European",
      "ISO-Code": "en",
      "Scripts": [
        "Latin"
      ],
      "Speakers": 1528
    }
  },
  {
    "German": {
      "Branch": "Germanic",
      "Countries": 20,
      "Family": "Indo-European",
      "ISO-Code": "de",
      "Scripts": [
        "Latin"
      ],
      "Speakers": 134
    }
  }
]
```
##### Curl
You can interact with the API with the parameter and the branch you want to search
```commandline
curl -G -d "branch=Germanic"  http://localhost:5000/search_branch
```

---
### Script
##### Webpage
In the next entry box is a drop down with different language families, select an option to see the languages with the selected script and their information.

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
##### Curl
You can interact with the API with the parameter and the script you want to search
```commandline
curl -G -d "script=Devanagari"  http://localhost:5000/search_script
```
---
### Speakers
##### Webpage
In the next entry box there is a box for a min and max that will serve as the range of speakers to query along with their information.

Input for min: `50`

Input for max: `60`


Output:
```json
[
  {
    "Amharic": {
      "Branch": "Semitic",
      "Countries": 7,
      "Family": "Afro-Asiatic",
      "ISO-Code": "am",
      "Scripts": [
        "Saba"
      ],
      "Speakers": 60
    }
  },
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
  }
]

```
##### Curl
You can interact with the API with the parameter and the range of speakers you want to query
```commandline
curl -G -d "min=50" -d "max=60"   http://localhost:5000/search_speakers
```

---
### Countries
##### Webpage
In the next entry box there is a box for a min and max that will serve as the range of countries in which a language is spoken.

Input for min: `10`

Input for max: `13`


Output:
```json
[
  {
    "Swahili": {
      "Branch": "Bantu",
      "Countries": 13,
      "Family": "Niger-Congo",
      "ISO-Code": "sw",
      "Scripts": [
        "Arabic",
        "Latin"
      ],
      "Speakers": 87
    }
  },
  {
    "Tagalog": {
      "Branch": "Malayo-Polynesian",
      "Countries": 11,
      "Family": "Austronesian",
      "ISO-Code": "tl",
      "Scripts": [
        "Baybayin",
        "Latin"
      ],
      "Speakers": 87
    }
  },
  {
    "Thai": {
      "Branch": "Zhuang-Tai",
      "Countries": 13,
      "Family": "Kra-Dai",
      "ISO-Code": "th",
      "Scripts": [
        "Thai"
      ],
      "Speakers": 71
    }
  }
]
```
##### Curl
You can interact with the API with the parameter and the mix and max you want to search
```commandline
curl -G -d "min1=10" -d "max1=13"   http://localhost:5000/search_countries
```
# Sources
I want to thank Professor Eric Jackson and Jeff Berry for the course material. Thank you for the sources I used in the webscraping and using AI to troubleshoot issues I ran into. 