class TextProcessor:
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


class TextLoader:
    def __init__(self, text_processor):
        self.__text_processor = text_processor
        self.__clean_string = ''

    def set_clean_text(self):
        self.__clean_string = self.__text_processor.get_clean_string()

    @property
    def clean_string(self):
        print('Output text is clean')
        return self.__clean_string


class Datainterface:
    def __init__(self, text_loader):
        self.__text_loader = text_loader

    def process_texts(self, list_of_string):
        for str in list_of_string:
            # a = TextProcessor(str)
            # print(a.get_clean_string())
            self.__text_loader.set_clean_text()
            print(self.__text_loader.clean_string)
            # self.__text_loader.set_clean_text()
        pass


list_of_strings = ['1!!,2', 'spri;;ng', 'wi!!!nter']

a = TextProcessor("asdfa!!&*?_aa ! b")
b = TextLoader(a)

b.set_clean_text()

print(b.clean_string)

c = Datainterface(b)
c.process_texts(list_of_strings)
