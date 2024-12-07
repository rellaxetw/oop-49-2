#                                                  04.12.2024
# Наследование -  Полиморфизм

class Hero:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def paralyzed(self):
        return f"{self.name} порализован-на "


    def rest(self):
        self.hp += 10
        return f"{self.name}, востанавливает hp: {self.hp}"

    def action(self):
        return f"{self.name}, делает базовое действия"

    def status(self):
        return f"Имя: {self.name}, Здоровье: {self.hp}"


class Warrior(Hero):
    def __init__(self, name, hp, st):
        super().__init__(name, hp)
        self.st = st


    def rest(self):
        self.hp += 5
        self.st += 20
        return f"{self.name} отдыхает, 5hp: здоровье восстановлено  {self.hp}, 20-стамина востановлены {self.st}."

    def action(self):
        self.st >= 20
        return f"{self.name} махает мечом  {self.st}."

    def charge(self):
        if self.st - 20:
            self.hp + 50
            return f"{self.name} востановливает hp и теряет стамину: {self.st}"


class Mage(Hero):
    def __init__(self, name, hp, mana):
        super().__init__(name, hp)
        self.mana = mana

    def rest(self):
        self.hp += 5
        self.mana += 20
        return f"{self.name} отдыхает, 5hp: здоровье восстановлено  {self.hp}, 20: мана увеличена до {self.mana}."

    def action(self):
        if self.mana >= 10:
            self.mana -= 10
            return f"{self.name} использует заклинание, мана уменьшена до {self.mana}."
        else:
            return f"{self.name} пытается кастовать заклинание, но недостаточно маны!"


    def teleport(self):
        if self.mana - 30:
            self.mana <= 30
            return f"{self.name} телепортируется и -30маана: {self.mana}"
        else:
            return f"{self.name} пытается телепортироваться но не хватает мааны!"

class Archer(Hero):
    def __init__(self, name, hp, arrows, precision):
        super().__init__(name, hp)
        self.arrows = arrows
        self.precision = precision


    def attack(self):
        if self.arrows > 0:
            self.arrows -= 1
            return f"{self.name} стреляет из лука, стрел осталось: {self.arrows}."
        else:
            return f"{self.name} пытается выстрелить, но у него нет стрел!"

    def rest(self):
        self.arrows += 5
        return f" У {self.name} восстановлен 5-cтрел: {self.arrows}"




def check_hero_instance(obj):
    if isinstance(obj, Hero):
        print(f"{obj.name} является экземпляром класса Hero или его подкласса.")
    else:
        print(f"{obj.name} не является экземпляром класса Hero или его подкласса.")


hero = Hero("Itachi", 100)
warrior = Warrior("Naruto", 120, 50)
mage = Mage("Мерлин", 100, 30)
archer = Archer("Djiraya", 100, 50, 75)


check_hero_instance(hero)
check_hero_instance(warrior)
check_hero_instance(mage)
check_hero_instance(archer)


class Villain:
    def __init__(self, name):
        self.name = name

villain = Villain("Локи")
check_hero_instance(villain)
