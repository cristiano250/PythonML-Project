from glob import glob

# Załaduj Pozytywne Recenzje
words_count_pos = {}
pos_files = glob('data/aclImdb/train/pos/*.txt')

for file in pos_files:
    with open(file,encoding="utf8") as stream:
        content = stream.read()

    words = content.lower().replace('<br />', ' ').split()

    for word in set(words):
        words_count_pos[word] = words_count_pos.get(word, 0) + 1

# Załaduj Negatywne Recenzje
words_count_neg = {}
neg_files = glob('data/aclImdb/train/neg/*.txt')

for file in neg_files:
    with open(file, encoding="utf8") as stream:
        content = stream.read()

    words = content.lower().replace('<br />', ' ').split()

    for word in set(words):
        words_count_neg[word] = words_count_neg.get(word, 0) + 1

# Pobierz Komentarz
sentence = input('Podaj komentarz: ')
words = sentence.lower().replace('<br />', ' ').split()
sentence_sentiment = 0
for word in words:
    positive = words_count_pos.get(word, 0)
    negative = words_count_neg.get(word, 0)


    # 50 pozytywnych, 50 negatywnych => sentyment = 0.0
    # 100 pozytywnych, 0 negatywnych => sentyment = +1.0
    # 10 pozytywnych, 0 negatywnych => sentment = +1.0
    # 75 pozytywnych, 25 negatywnych => sentyment = +0.5
    # 0 pozytywnych, 100 negatynwych => sentyment = -1.0

    all = positive + negative
    if all == 0:
        sentyment = 0.0
    else:
        sentyment = (positive - negative) / all
    sentence_sentiment += sentyment
    print(word, sentyment)

sentence_sentiment /= len(words)
if sentence_sentiment > 0:
    label = 'pozytywne'
else:
    label = 'negatywne'

print("Twoje zdanie jest", label)
print("Sentyment =", sentence_sentiment)