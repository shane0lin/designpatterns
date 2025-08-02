from abc import ABC, abstractmethod


class EuropeanPlug:
    def connect(self):
        print("European plug connected.")


class USPlug(ABC):
    @abstractmethod
    def connect(self):
        pass


class Adapter(USPlug):
    def __init__(self, euro_plug):
        self.plug = euro_plug
    
    def connect(self):
        self.plug.connect()


if __name__ == "__main__":
    euro_plug = EuropeanPlug()
    adapter = Adapter(euro_plug)
    adapter.connect()