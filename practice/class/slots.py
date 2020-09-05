#スロット

class Abc:
    __slots__ = ["a", "b"]
    def __init__(self):
        self.a = 1

i = Abc()#インスタンス作成
print(i.a)#1が出力される

i.b = 2
print(i.b)#2が出力される

i.c = 3#エラーになる
#slotsでアトリビュートはa,bのみ定義しているので、cというアトリビュートは定義できない
