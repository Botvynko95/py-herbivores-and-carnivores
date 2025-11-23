class Animal:
    alive = []

    def __init__(self, name, health=100):
        self.name = name
        self._health = health
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self):
        return (f"{{Name: {self.name},"
                f"Health: {self.health},"
                f"Hidden: {self.hidden}}}")

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        self._health = max(0, value)
        if self._health == 0 and self in Animal.alive:
            Animal.alive.remove(self)


class Herbivore(Animal):
    def hide(self):
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, other):
        if not isinstance(other, Herbivore):
            return
        if other.hidden:
            return
        other.health = other.health - 50
