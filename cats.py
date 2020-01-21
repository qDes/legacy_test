from animals import Animal


class Cat(Animal):
    @property
    def run_energy(self):
        return 5


class Tiger(Animal):
    def __init__(self, name, energy=200, init_parameters=dict()):
        Animal.__init__(self, name, energy, init_parameters)

    @property
    def run_energy(self):
        return 20

    @property
    def swim_energy(self):
        return 40
