# Use Cases
## 1. Search a language
A user can input a language and it returns basic information in a table about that language

Input: French

Output:

| Category        | Info          |
|-----------------|---------------|
| Name | French        |
| Language Family | Indo-European |
| Family Branch | Romance       |
| Script          | Latin         |
| Total Speakers  | 310 million   |
| Countries       | 51 countries  |


## 2.  Language Family
A user can select a language family and it returns the languages and their info

Input: "Afro-Asiatic"

Output:

| Languages                       |
|---------------------------------| 
| Amharic {info from test case 1} |
| Arabic {info from test case 1}  |
| Hausa {info from test case 1} |

## 3. Family Branch
A user can select  a language branch and returns the languages and their info

Input: Romance

Output:

| Languages                          |
|------------------------------------| 
| French {info from test case 1}     |
| Italian {info from test case 1}    |
| Portuguese {info from test case 1} |
| Spanish {info from test case 1}    |

## 4. Search by Script:
Search by scripts and returns the info and languages with that script

Input: Arabic

Output:

| Languages                        |
|----------------------------------| 
| Arabic {info from test case 1}   |
| Hausa {info from test case 1}    |
| Javanese {info from test case 1} |
| Persian {info from test case 1}  |
| Punjabi {info from test case 1}  |
| Swahili {info from test case 1}  |
| Urdu {info from test case 1}     |




## 5. Search by Speakers
A user inputs and min and max for speakers in millions and it outputs the languages with speakers between those two variables and the info

Input: min: 50, max: 70

| Languages                        |
|----------------------------------| 
| Amharic {info from test case 1}  |
| Bhojpuri {info from test case 1} |
| Gujarati {info from test case 1} |
| Italian {info from test case 1}  |
| Javanese {info from test case 1} |
| Kannada {info from test case 1}  |

## 5. Search by Countries
A user inputs and min and max for number of countries where the language is spoken  and it outputs the languages with speakers between those two variables and the info

Input: min 30, max 80

Output:

| Languages                        |
|----------------------------------| 
| Arabic {info from test case 1}   |
| English {info from test case 1}  |
| French {info from test case 1}   |
| Spanish {info from test case 1}  |
