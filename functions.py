import string


class Numbs:

    def __init__(self, text: str):
        self.text = text

    def ten_common_words(self) -> None:
        """Данная функция принемает на вход строку и выводит в консоль 10 наиболее часто встречающихся слов"""
        text = self.text

        for symbol in string.punctuation + '\n':
            if symbol in text:
                text = text.replace(symbol, '')

        up_text = text.upper()
        text = up_text.split(" ")
        dict_words = {}

        for word in text:
            value = text.count(word)
            dict_words[word] = value

        sorted_dict = {}
        sorted_keys = sorted(dict_words, key=dict_words.get, reverse=True)

        for word in sorted_keys:
            sorted_dict[word] = dict_words[word]

        count = 0
        for key in sorted_dict:
            if count == 10: break
            count += 1

            if 2 <= sorted_dict.get(key) <= 4 or 22 <= sorted_dict.get(key) <= 24:
                print(f'Слово "{key}" встречается {sorted_dict.get(key)} раза')
            else:
                print(f'Слово "{key}" встречается {sorted_dict.get(key)} раз')
