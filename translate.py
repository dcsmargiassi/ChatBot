import googletrans
from googletrans import Translator

# Running the library
translator = Translator()

# Get the language codes
def lang_code(language):
    language = language.lower()
    lang_dict = googletrans.LANGUAGES
    
    for key in lang_dict.keys():
        if language == lang_dict[key]:
            return key
    return 'None'

def translator_func(msg, language='english'):
    lc = lang_code(language)
    
    if lc == 'none':
        return 'Sorry, language not found'
    
    return language + ": " + translator.translate(text=msg, dest=lc).text
    