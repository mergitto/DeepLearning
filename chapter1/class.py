class Hoge:
    def __init__(self, name):
        self.name = name
        print("初期化しました")

    def hello(self):
        print("Hello " + self.name + "!")

    def goodbye(self):
        print("Good Bye " + self.name + "!")

m = Hoge("Hoge")
m.hello()
m.goodbye()
