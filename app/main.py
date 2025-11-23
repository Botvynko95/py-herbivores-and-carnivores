from __future__ import annotations


class Animal:
    alive = []

    def __init__(
            self: "Animal",
            name: str,
            health: int = 100,
    ) -> None:
        self.name = name
        self._health = health
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self: "Animal") -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")

    @property
    def health(self: "Animal") -> int:
        return self._health

    @health.setter
    def health(
        self: "Animal",
        value: int,
    ) -> None:
        self._health = max(0, value)
        if self._health == 0 and self in Animal.alive:
            Animal.alive.remove(self)


class Herbivore(Animal):
    def hide(self: "Herbivore") -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(
            self: "Carnivore",
            other: Herbivore,
    ) -> None:
        if not isinstance(other, Herbivore):
            return
        if other.hidden:
            return
        other.health = other.health - 50
