#プライベートクラス変数
class Per:
    def __init__(self, name):
        self.name = "name"
        self.__momney = 20
    def confirm(self, age):
        self.age = age

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

person = Person("ema")

print(person.say_something())
#クラス変数は、インスタンス.変数名で呼び出せる
print(person.value)
#プライベート変数は、インスタンス._クラス名__変数名で呼び出せる
#この方法は推奨されていない
print(person._Person__secret)
