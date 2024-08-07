import pandas as p

df = p.read_csv("6. IMDB-Movie-Data.csv")
df.info()


#       Вопрос 1: Фильмы с более высоким рейтингом получают больше голосов.
# Гипотезы:
# 1.Каково среднее количество голосов для фильмов с рейтингом выше 7?
# 2.Каково среднее количество голосов для фильмов с рейтингом 7 и ниже?
# 3.Насколько отличается среднее количество голосов между этими двумя группами?
#       Вопрос 2: Фильмы определенных жанров имеют тенденцию получать более высокие рейтинги.
# Гипотезы:
# 1.Какие жанры имеют наивысшие средние рейтинги?
# 2.Какие жанры имеют наинизшие средние рейтинги?
# 3.Насколько отличаются средние рейтинги между жанрами с наивысшими и наинизшими рейтингами?
#       Вопрос 3: Фильмы с известными режиссерами и актерами имеют более высокие рейтинги и доходы.
# Гипотезы:
# 1.Каково среднее значение рейтинга фильмов для топ-10 режиссеров по количеству голосов?
# 2.Каково среднее значение дохода фильмов для топ-10 режиссеров по количеству голосов?
# 3.Каково среднее значение рейтинга и дохода фильмов для топ-10 актеров по количеству голосов?
df = df.dropna()
df.info()
print(df['Revenue (Millions)'].value_counts())