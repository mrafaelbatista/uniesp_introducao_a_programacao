from deep_translator import GoogleTranslator

trad = GoogleTranslator(source='english', target='portuguese').translate('My darling!')

print(trad)