import random

class War:
    def __init__(self, name):  # Тепер тільки ім'я, а hepe і sula — випадкові
        self.name = name
        self.hepe = random.randint(60, 100)  # Здоров'я від 60 до 100
        self.sula = random.randint(10, 30)   # Сила від 10 до 30

    def is_alive(self):
        return self.hepe > 0

    def attack(self, other):
        if self.is_alive():
            damage = random.randint(1, self.sula)
            other.hepe -= damage
            print(f"{self.name} атакує {other.name} і завдає {damage} шкоди! (Залишилось HP: {other.hepe})")
            if not other.is_alive():
                print(f"{other.name} загинув!")

# Створення воїнів
w_1 = War('Predator')
w_2 = War('Alien')

# Показати початкові параметри
print(f"{w_1.name} — HP: {w_1.hepe}, Сила: {w_1.sula}")
print(f"{w_2.name} — HP: {w_2.hepe}, Сила: {w_2.sula}")

round_counter = 1

while w_1.is_alive() and w_2.is_alive():
    if round_counter in [1, 2, 10, 14]:
        print(f"\n=== Раунд {round_counter} ===")
    
    w_1.attack(w_2)
    if w_2.is_alive():
        w_2.attack(w_1)
    
    round_counter += 1

if w_1.is_alive():
    print(f"\n{w_1.name} переміг!")
else:
    print(f"\n{w_2.name} переміг!")

