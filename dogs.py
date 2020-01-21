from animals import Animal


class Dog(Animal):
    @property
    def run_energy(self):
        return 10

    @property
    def swim_energy(self):
        return 30
