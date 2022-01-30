# -*- coding: utf-8 -*-

from textblob import TextBlob
import speech_recognition as sr
import pocketsphinx
import pyttsx3

def speech_to_text_from_mic():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Say something')
        audio = r.listen(source)
    #recognize using Sphinx
    text = ''
    try:
        text = (r.recognize_sphinx(audio))
    except sr.UnknownValueError:
        text = ('SPEECH NOT UNDERSTOOD')
    except sr.RequestError as e:
        text = (e)
    print(text)
    return text
 
engine = pyttsx3.init()
translated = ''       
languages = ['Afrikaans - af','Albanian - sq','Amharic - am','Arabic - ar','Armenian - hy','Azerbaijani - az','Basque - eu','Belarusian - be','Bengali - bn','Bosnian - bs','Bulgarian - bg','Catalan - ca','Cebuano - ceb','Chinese (Simplified) - zh-CN','Chinese (Traditional) - zh-TW','Corsican - co','Croatian - hr','Czech - cs','Danish - da','Dutch - nl','English - en','Esperanto - eo','Estonian - et','Finnish - fi','French - fr','Frisian - fy','Galician - gl','Georgian - ka','German - de','Greek - el','Gujarati - gu','Haitian Creole - ht','Hausa - ha','Hawaiian - haw','Hebrew - he','Hindi - hi','Hmong - hmn','Hungarian - hu','Icelandic - is','Igbo - ig','Indonesian - id','Irish - ga','Italian - it','Japanese - ja','Javanese - jv','Kannada - kn','Kazakh - kk','Khmer - km','Kinyarwanda - rw','Korean - ko','Kurdish - ku','Kyrgyz - ky','Lao - lo','Latin - la','Latvian - lv','Lithuanian - lt','Luxembourgish - lb','Macedonian - mk','Malagasy - mg','Malay - ms','Malayalam - ml','Maltese - mt','Maori - mi','Marathi - mr','Mongolian - mn','Myanmar (Burmese) - my','Nepali - ne','Norwegian - no','Nyanja (Chichewa) - ny','Odia (Oriya) - or','Pashto - ps','Persian - fa','Polish - pl','Portuguese (Portugal, Brazil) - pt','Punjabi - pa','Romanian - ro','Russian - ru','Samoan - sm','Scots Gaelic - gd','Serbian - sr','Sesotho - st','Shona - sn','Sindhi - sd','Sinhala (Sinhalese) - si','Slovak - sk','Slovenian - sl','Somali - so','Spanish - es','Sundanese - su','Swahili - sw','Swedish - sv','Tagalog (Filipino) - tl','Tajik - tg','Tamil - ta','Tatar - tt','Telugu - te','Thai - th','Turkish - tr','Turkmen - tk','Ukrainian - uk','Urdu - ur','Uyghur - ug','Uzbek - uz','Vietnamese - vi','Welsh - cy','Xhosa - xh','Yiddish - yi','Yoruba - yo','Zulu - zu']
language_codes = ['af','sq','am','ar','hy','az','eu','be','bn','bs','bg','ca','ceb','zh-CN','zh-TW','co','hr','cs','da','nl','en','eo','et','fi','fr','fy','gl','ka','de','el','gu','ht','ha','haw','he','hi','hmn','hu','is','ig','id','ga','it','ja','jv','kn','kk','km','rw','ko','ku','ky','lo','la','lv','lt','lb','mk','mg','ms','ml','mt','mi','mr','mn','my','ne','no','ny','or','ps','fa','pl','pt','pa','ro','ru','sm','gd','sr','st','sn','sd','si','sk','sl','so','es','su','sw','sv','tl','tg','ta','tt','te','th','tr','tk','uk','ur','ug','uz','vi','cy','xh','yi','yo','zu']
lang_dict = dict()
for i in range(len(language_codes)):
    lang_dict[language_codes[i]] = languages[i]

print('Select a language code:',languages)
print(':',end=' ')
to = input()
from_text = speech_to_text_from_mic()
blob = TextBlob(from_text)
try:
    translated = blob.translate(to=to)
    print(f'Translation in {lang_dict[to]} is: {translated}')
except:
    translated = 'COULD NOT TRANSLATE'
engine.say(translated)
engine.runAndWait()
