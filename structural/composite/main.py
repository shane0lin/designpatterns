from abc import ABC, abstractmethod


class Musician(ABC):
    @abstractmethod
    def show_details(self):
        pass


class SoloArtist(Musician):
    def __init__(self, name, instrument):
        self.name = name
        self.instrument = instrument

    def show_details(self):
        print(f"{self.name} plays the {self.instrument}.")


class Band(Musician):
    def __init__(self):
        self.__peoples = []

    def add(self, people):
        self.__peoples.append(people)
        
    def show_details(self):
        for pl in self.__peoples:
            pl.show_details()


solo1 = SoloArtist("John Doe", "guitar")
solo2 = SoloArtist("Jane Smith", "keyboard")

band = Band()
band.add(solo1)
band.add(solo2)

band.show_details()

