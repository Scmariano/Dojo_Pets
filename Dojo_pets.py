
from Ninja import Ninja
from Pets import Pet   

Keamon = Pet("keamon", "Dog", "play_dead", "Bowowow")
Stephen = Ninja("Stephen", "Mariano", "bones", "Meat", Keamon)

print(Keamon.health)
Stephen.feed().walk().bathe()
print(Keamon.health)
