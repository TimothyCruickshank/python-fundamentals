# enemy class
class enemy:
    hp = 100
    luck = 5
    attack_damage = 10
    name = "Tiny Blob"
    defense = 20
    reward = 2

    def __init__(self, name, hp, luck, attack_damage, defense, reward): # dunder (double under score)
        self.hp = hp
        self.luck = luck
        self.attack_damage = attack_damage
        self.name = name
        self.defense = defense
        self.reward = reward




    def enemy_attack(self, player): 
        player.hp - self.attack_damage


class player():
    hp = 100
    attack_damage = 20
    name = "Bobby"
    defense = 5
    gold = 50

    def __init__(self, name, hp, luck, attack_damage, defense, gold):
        self.hp = hp
        self.attack_damage = attack_damage
        self.luck = luck
        self.defense = defense
        self.gold = gold

    def playerAttack(self, enemy):
        enemy.hp -= (self.attack_damage - enemy.defense)

        print(f"{self.name} attacked {enemy.name} for {(self.attack_damage - enemy.defense)} damage.")

    def playerDefend(self, enemy):
        pass


    def heal(self, target):
        pass

blobTheBuilder = enemy("Blob the builder", 100, 3, 10, 3, 100)
catelinTheTorturer = enemy("Catelin The Torturer", 300, 10, 50, 10, 500)

anthonyTheAntelope = player("Anthony The Antelope", 100, 5, 20, 10, 100)
giffordTheGiant = player("Gifford The Giant", 150, 2, 25, 15, 50)
factorialFactor = player("Factorial Factor", 75, 10, 30, 5, 75)
hutchTheCabinet = player("Hutch The Cabinet", 125, 5, 15, 10, 50)

print(f"{catelinTheTorturer.name} attacks for {catelinTheTorturer.attack_damage} damage.")

catelinTheTorturer.attack_damage *= 1.5

print(f"{catelinTheTorturer.name} gets a blessing from the gods and gets a 1.5 times increases in damage and attacks again for {catelinTheTorturer.attack_damage} damage.")

anthonyTheAntelope.playerAttack(blobTheBuilder)
giffordTheGiant.playerAttack(blobTheBuilder)
factorialFactor.playerAttack(blobTheBuilder)
hutchTheCabinet.playerAttack(blobTheBuilder)
