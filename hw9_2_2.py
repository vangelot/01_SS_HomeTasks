class TextProcessor:
    def get_clean_string(self, str):
        res_str = ''
        for i in range(len(str)):
            if self.__is_punctuation(str[i]):
                continue
            res_str += str[i]
        return res_str

    def __is_punctuation(self, letter):
        if letter in ".,!?:;/'-_()[]":
            return True
        else:
            return False


class TextLoader:

    def __init__(self):
        self.__text_processor = TextProcessor()
        self.__clean_string = ''

    def set_clean_text(self, str):
        self.__clean_string = self.__text_processor.get_clean_string(str)

    @property
    def clean_string(self):
        print('Output text is clean')
        return self.__clean_string


class DataInterface:

    def __init__(self):
        self._text_loader = TextLoader()

    def process_texts(self, list_of_string):
        for str in list_of_string:
            self._text_loader.set_clean_text(str)
            print(self._text_loader.clean_string)


list_of_strings = ['1!!,2', 'spri;;ng', 'wi!!!nter']

c = DataInterface()
c.process_texts(list_of_strings)

# a = TextProcessor()
# print(a.get_clean_string('asdf!!!fsd,,'))

# b = TextLoader()
# b.set_clean_text('a!!!a')
# print(b.clean_string)
