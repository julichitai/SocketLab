import re
import operator

class WordsCounter:
    def __init__(self, text):
        self.text = text

    def get_words(self):
        return re.findall(r"(\w+)", self.text)

    def count_words(self):
        result_dict = {}
        result = ''
        words = self.get_words()
        for word in words:
            result_dict[word] = result_dict.get(word, 0) + 1
        sorted_result = sorted(result_dict.items(), key = lambda x: x[1], reverse=True)
        for word, count in sorted_result:
            result += f'{word}: {count}\n'
        return result
