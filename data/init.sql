CREATE DATABASE languages;
ALTER DATABASE languages CHARACTER SET utf8 COLLATE utf8_unicode_ci;
use languages;
CREATE TABLE language_2 (
    lang_id SMALLINT UNSIGNED AUTO_INCREMENT,
    name NVARCHAR(30),
    iso NVARCHAR(3),
    family ENUM('Indo-European', 'Afro-Asiatic', 'Sino-Tibetan', 'Austronesian', 'Japonic', 'Austroasiatic', 'Kra-Dai','Dravidian', 'Turkic', 'Niger-Congo', 'Koreanic' ),
    branch NVARCHAR(20),
    speakers SMALLINT,
    countries TINYINT,
    CONSTRAINT pk_lang PRIMARY KEY (lang_id)
);
CREATE TABLE scripts (
    lang_id SMALLINT UNSIGNED,
    script NVARCHAR(20),
    CONSTRAINT pk_scripts PRIMARY KEY (lang_id, script),
    CONSTRAINT fk_lang_script_lang_id FOREIGN KEY (lang_id)
    REFERENCES language_2 (lang_id)
);
INSERT INTO language_2 (lang_id,name, iso, family, branch, speakers, countries)
VALUES
    (null, 'English', 'en', 'Indo-European', 'Germanic', 1528, 74),
    (null, 'Chinese', 'zh', 'Sino-Tibetan', 'Sinitic', 1184, 27 ),
    (null, 'Hindi', 'hi', 'Indo-European', 'Indo-Aryan', 609, 9),
    (null, 'Spanish', 'es', 'Indo-European', 'Romance', 558, 36),
    (null, 'Arabic', 'ar', 'Afro-Asiatic', 'Semitic', 335, 35),
    (null, 'French', 'fr', 'Indo-European', 'Romance', 312, 51),
    (null, 'Bengali', 'bn', 'Indo-European', 'Indo-Aryan', 284, 4),
    (null, 'Portuguese', 'pt', 'Indo-European', 'Romance', 267, 18 ),
    (null, 'Russian', 'ru', 'Indo-European', 'Balto-Slavic', 253, 22),
    (null, 'Indonesian', 'id', 'Austronesian', 'Malayo-Polynesian', 252, 4),
    (null, 'Urdu', 'ur', 'Indo-European', 'Indo-Aryan', 246, 6),
    (null, 'German', 'de', 'Indo-European', 'Germanic', 134, 20),
    (null, 'Japanese', 'ja', 'Japonic', null, 126, 4),
    (null, 'Marathi', 'mr', 'Indo-European', 'Indo-Aryan', 99, 1),
    (null, 'Vietnamese', 'vi', 'Austroasiatic', 'Vietic', 97, 4),
    (null, 'Telugu', 'te',  'Dravidian', 'South-Central', 96, 1),
    (null, 'Hausa', 'ha', 'Afro-Asiatic', 'Chadic', 94, 3),
    (null, 'Turkish', 'tr', 'Turkic', 'Oghuz', 91, 14 ),
    (null, 'Punjabi', 'pa', 'Indo-European', 'Indo-Aryan', 90, 4),
    (null, 'Swahili', 'sw', 'Niger-Congo', 'Bantu', 87, 13),
    (null, 'Tagalog', 'tl', 'Austronesian', 'Malayo-Polynesian', 87,11),
    (null, 'Tamil', 'ta', 'Dravidian', 'South', 86, 6),
    (null, 'Persian', 'fa', 'Indo-European', 'Iranian', 83, 6),
    (null, 'Korean', 'ko', 'Koreanic', null, 82, 7),
    (null, 'Thai', 'th', 'Kra-Dai', 'Zhuang-Tai', 71, 13),
    (null, 'Javanese', 'jv', 'Austronesian', 'Malayo-Polynesian', 69, 1),
    (null, 'Italian', 'it', 'Indo-European', 'Romance', 66, 16),
    (null, 'Gujarati', 'gu', 'Indo-European', 'Indo-Aryan', 62, 3),
    (null, 'Amharic', 'am', 'Afro-Asiatic', 'Semitic', 60, 7),
    (null, 'Kannada', 'kn', 'Dravidian','South', 59, 1),
    (null, 'Bhojpuri', 'bho', 'Indo-European', 'Indo-Aryan', 53, 3 )





