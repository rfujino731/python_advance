#プライベートクラス変数
#objectは書かなくてもpython3なら動作する
#python2の名残で書くことが多い
class Person(object):
    def __init__(self, name):
        self.name = name
        self.value = "通常の変数"
        self.__secret = "プライベート変数"
        print(self.name)

    def say_something(self):
        print("hello")
        print("I am {}.".format(self.name))

    def __say_secret(self):
        print("bye")

#インスタンスを作成
person = Person("ema")

#クラスメソッドを呼び出す(通常の方法)
print(person.say_something())

#プライベートメソッドを呼び出す
print(person._Person__say_secret())
