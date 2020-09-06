class Car(object):
    def __init__(self, model = None):
        self.model = model
    def run(self):
        print("run")

class ToyotaCar(Car):
    def run(self):
        print("fast")

class TeslaCar(Car):
    def __init__(self, model = "Model S", enable_auto_run = False):
        super().__init__(model)
        self.enable_auto_run = enable_auto_run

    @property
    def enable_auto_run(self):
        return self._enable_auto_run

    @enable_auto_run.setter
    def enable_auto_run(self, is_enable):
        self._enable_auto_run = is_enable

    def run(self):
        print("suoer fast")
    def auto_run(self):
        print("auto_run")

teslacar = TeslaCar("Model S")
#16～18行をコメントアウトするとTrueを呼び出せる
#20～22行のsetterを使用しても呼び出せる
teslacar.enable_auto_run = True
print(teslacar.enable_auto_run)
