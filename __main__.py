import unittest
import sys

from animals import Animal
from cats import Cat, Tiger
from dogs import Dog
from ducks import Duck
from fishSimple import Fish_Simple
from fishCanFly import Fish_Can_Fly
from io import StringIO


class TestAnimal(unittest.TestCase):
    def setUp(self):
        self.name = "test_animal"
        self.animal = Animal(self.name)
    
    def test_animal_constructor(self):
        animal_test = Animal("test")
        self.assertEqual("test", animal_test.name,
                         "simple constructor naming test")
        self.assertEqual(100, animal_test.get_energy(),
                         "simple constructor energy test")
        animal_test = Animal("test", init_parameters={"name": "changed",
                                                      "energy": 500})
        self.assertEqual("changed", animal_test.name,
                         "init parameters naming test")
        self.assertEqual(500, animal_test.get_energy(),
                         "init parameters energy test")
        self.assertEqual(self.name, self.animal.name,
                        "setup class test")
    
    def test_animal_saying(self):
        captured = StringIO()
        sys.stdout = captured
        self.animal.say()
        sys.stdout = sys.__stdout__
        captured_value = captured.getvalue()
        self.assertEqual("Hello, I'm Animal and my name is test_animal.\n", 
                         captured_value, "Animal saying test")

    def test_animal_actions(self):
        self.animal.fly()
        self.animal.swim()
        self.animal.run()
        self.assertEqual(100, self.animal.get_energy(),
                         "Animal energy should not change")


class TestCat(unittest.TestCase):
    
    def setUp(self):
        self.name = "test_cat"
        self.cat = Cat(self.name)
    
    def test_cat_actions(self):
        self.cat.fly()
        self.cat.swim()
        self.assertEqual(100, self.cat.get_energy(),
                         "Cat energy after fly/swim should not change")
        self.cat.run()
        self.assertEqual(95, self.cat.get_energy(),
                        "Cat energy after 1 run should be 95")
        for _ in range(19):
            self.cat.run()
        self.assertEqual(0, self.cat.get_energy(),
                         "Cat energy after 20 run should be 0")
        for _ in range(20):
            self.cat.run()
        self.assertEqual(-100, self.cat.get_energy(),
                         "Cat energy after 40 run should be -100")


class TestTiger(unittest.TestCase):
    
    def setUp(self):
        self.name = "Barsik"
        self.tiger = Tiger(self.name)
    
    def test_tiger_saying(self):
        captured = StringIO()
        sys.stdout = captured
        self.tiger.say()
        sys.stdout = sys.__stdout__
        captured_value = captured.getvalue()
        self.assertEqual("Hello, I'm Tiger and my name is Barsik.\n", 
                         captured_value, "Tiger saying test.")
   
    def test_tiger_constructor(self):
        self.assertEqual(200, self.tiger.get_energy(),
                         "Tiger init energy should be 200")

    def test_tiger_actions(self):
        self.tiger.fly()
        self.assertEqual(200, self.tiger.get_energy(),
                         "Tiger energy after fly should not change")
        self.tiger.run()
        self.assertEqual(180, self.tiger.get_energy(),
                        "Tiger energy after 1 run should be 180")
        for _ in range(4):
            self.tiger.run()
        self.assertEqual(100, self.tiger.get_energy(),
                         "Tiger energy after 5 run should be 100")
        for _ in range(2):
            self.tiger.swim()
        self.assertEqual(20, self.tiger.get_energy(),
                         "Tiger energy after 2 swim should be 20")


class TestDog(unittest.TestCase):
    
    def setUp(self):
        self.name = "Bobik"
        self.dog = Dog(self.name)

    def test_dog_actions(self):
        self.dog.fly()
        self.assertEqual(100, self.dog.get_energy(),
                         "Dog energy after fly should not change")
        self.dog.run()
        self.assertEqual(90, self.dog.get_energy(),
                        "Dog energy after 1 run should be 90")
        self.dog.swim()
        self.assertEqual(60, self.dog.get_energy(),
                         "Dog energy after 1 swim should be 60")

class TestDuck(unittest.TestCase):
    
    def setUp(self):
        self.name = "duck test"
        self.duck = Duck(self.name)

    def test_duck_actions(self):
        self.duck.run()
        self.assertEqual(100, self.duck.get_energy(),
                         "Duck energy after run should not change")
        self.duck.fly()
        self.assertEqual(70, self.duck.get_energy(),
                        "Duck energy after 1 fly should be 70")
        self.duck.swim()
        self.assertEqual(60, self.duck.get_energy(),
                         "Duck energy after 1 swim and fly should be 60")



class TestFishSimple(unittest.TestCase):
    
    def setUp(self):
        self.name = "fish test"
        self.fish = Fish_Simple(self.name)

    def test_fish_simple_actions(self):
        self.fish.fly()
        self.fish.run()
        self.assertEqual(100, self.fish.get_energy(),
                         "Simple fish energy after run/fly should not change")
        self.fish.swim()
        self.assertEqual(95, self.fish.get_energy(),
                         "Fish energy after 1 swim should be 95")
        for _ in range(19):
            self.fish.swim()
        self.assertEqual(0, self.fish.get_energy(),
                         "Fish energy after 20 swim should be 0")

class TestFlyingFish(unittest.TestCase):
    
    def setUp(self):
        self.name = "fish fly"
        self.flying_fish = Fish_Can_Fly(self.name)

    def test_flying_fish_actions(self):
        self.flying_fish.run()
        self.assertEqual(100, self.flying_fish.get_energy(),
                         "Flyin fish energy after run/fly should not change")
        self.flying_fish.swim()
        self.flying_fish.swim()
        self.assertEqual(90, self.flying_fish.get_energy(),
                         "Fish energy after 2 swim should be 90")
        self.flying_fish.fly()
        self.assertEqual(70, self.flying_fish.get_energy(),
                         "Fish energy after 2 swim and 1 fly should be 70")


if __name__ == "__main__":
    unittest.main()
