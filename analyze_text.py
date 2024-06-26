import nltk
from nltk.tokenize import word_tokenize
from nltk.stem.snowball import SnowballStemmer

# nltk.download('popular')
# nltk.download('stopwords')
# nltk.download('punkt')

stemmer = SnowballStemmer("russian")
text = '''
Вашему вниманию предлагаем однокомнатную/малогабаритную квартиру в Центральном районе г. Комсомольска-на-Амуре.
Площадь квартиры 23,2 м², комната объединена с кухней (10,8м²+5,9м²) , окна выходят на одну сторону. Душевая комната и санузел раздельные.
Квартира в простом состоянии.
Очень удачное расположение дома, в шаговой доступности находятся:
- Детские сады  104, 71.
- Общеобразовательные школы  1, 18.
- Строительный колледж.
- Магазины и ТЦ.
- Остановки общественного транспорта.
Представленную квартиру можно приобрести по действующим ипотечным программам.
А также с использованием субсидированных программ предоставляемых банками партнёрами для наших клиентов:
по ставке от 0,01% на вторичное жильё на первые ДВА года ипотеки,
по ставке от 10,5% на вторичное жилье на весь срок ипотеки.
Квартира подходит под любой расчёт: военная ипотека, обычная ипотека, различные сертификаты, наличный расчёт.
Приглашаем Вас оценить квартиру лично.
Звоните сейчас!
'''
tokens = word_tokenize(text)
stemmed_words = [stemmer.stem(word) for word in tokens]
print(stemmed_words.index('центральн'))
print(stemmed_words[6-1], stemmed_words[6], stemmed_words[6+1])
print(stemmer.stem("центральное"))