class WordsFinder:
    def __init__(self, *files):
        self.file_names = list(files)
        self.all_words = {}

    def get_all_words(self):
        if not self.all_words:
            for file_name in self.file_names:
                words = []
                with open(file_name, 'r', encoding='utf-8') as file:
                    for line in file:
                        clean_line = line.lower().replace(',', '').replace('.', '').replace('=', '').replace('!', '').replace('?', '').replace(';', '').replace(':', '').replace(' - ', ' ')
                        words.extend(clean_line.split())
                self.all_words[file_name] = words
        return self.all_words
    def find(self, word):
        result = {}
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            if word in words:
                result[file_name] = words.index(word) + 1  # Словарей индексируются с 1
        return result

    def count(self, word):
        result = {}
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            result[file_name] = words.count(word)
        return result




finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего


