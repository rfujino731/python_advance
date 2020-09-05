class Prism:
    #コンストラクタ
    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth

    def content(self):
        return self.width * self.height * self.depth

    #デストラクタ
    def __del__(self):
        print("good bye")

pre = Prism(10, 20, 30)
print(pre.content())

#クラス内のアトリビュートを書き換える
pre.height= 100
print(pre.content())

#クラスの継承
class Cubu(Prism):
    def __init__(self, length):
        self.width = self.height = self.depth = length

cubu = Cubu(20)
print(cubu.content)
