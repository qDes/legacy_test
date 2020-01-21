from animals import Animal


class Duck(Animal):
    @property
    def swim_energy(self):
        return 10

    @property
    def fly_energy(self):
        return 30
