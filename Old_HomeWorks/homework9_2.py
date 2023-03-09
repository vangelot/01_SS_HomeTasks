class TextProcessor():
    def __init__(self, str=''):
        self.__str = str
    def get_clean_string(self):
        res_str = ''
        for i in range(len(self.__str)):
            if self.__is_punctuation(self.__str[i]):
                continue
            res_str += self.__str[i]
        return res_str

    def __is_punctuation(self, letter):
        if letter in ".,!?:;/'-_()[]":
            return True
        else:
            return False

class TextLoader():
    def __init__(self, text_processor, clean_string=''):
        self.__text_processor = text_processor
        self.__clean_string = clean_string

    def set_clean_text(self):
        self.__clean_string = self.__text_processor.get_clean_string()

    @property
    def clean_string(self):
        print('Output text is clean')

    def get_string(self):
        return self.__clean_string

#
a = TextProcessor("asdfa!!&*?_aa ! b")
# print(a.get_clean_string())

b = TextLoader(a, "aaa,,!!!aaa")

b.set_clean_text()
print(b.get_string())
