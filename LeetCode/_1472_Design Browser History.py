class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.index = 0

    def visit(self, url: str) -> None:
        self.history = self.history[:self.index+1]
        self.history.append(url)
        self.index += 1

    def back(self, steps: int) -> str:
        if self.index - steps >= 0:
            self.index = self.index - steps
            return self.history[self.index]
        else:
            self.index = 0
            return self.history[0]

    def forward(self, steps: int) -> str:
        if self.index + steps < len(self.history):
            self.index = self.index + steps
        else:
            self.index = len(self.history) - 1
        return self.history[self.index]



def main():
    obj = BrowserHistory('zav.com')
    obj.visit('kni.com')
    param_2 = obj.back(7)
    param_2 = obj.back(7)
    obj.visit('facebook.com')
    obj.visit('youtube.com')
    param_2 = obj.back(1)
    param_3 = obj.forward(5)
    obj.visit('leetcode.com')
    param_3 = obj.forward(1)
    param_3 = obj.back(20)
    print(param_2, param_3, obj.history)


if __name__ == '__main__':
    main()
