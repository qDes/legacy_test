from animals import Animal


class Fish_Can_Fly(Animal):
    @property
    def swim_energy(self):
        return 5

    @property
    def fly_energy(self):
        return 20
