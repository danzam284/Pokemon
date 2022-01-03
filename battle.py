import random, sys, os, time

BLACK = '\033[30m'
DARKGREY = '\033[90m'
RED = '\033[31m'
GREEN = '\033[32m'
LIGHTGREEN = '\033[92m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
LIGHTBLUE = '\033[94m'
PURPLE = '\033[35m'
MAGENTA = '\033[35m'
PINK='\033[95m'
CYAN = '\033[36m'
WHITE = '\033[37m'
LIGHTGREY = '\033[37m'
BROWN  = '\33[36m'
ORANGE = '\033[33m'
UNDERLINE = '\033[4m'
BOLD = '\033[01m'
RESET = '\033[0m'
BLINK = '\33[5m'

os.system("Clear")
type_options = ["normal", "fire", "water", "grass", "electric", "ice", "fighting", "poison", "ground", "flying", "psychic", "bug", "rock", "ghost" ,"dragon", "dark", "steel"]
strong = {"normal": ("fighting"), "fire": ("water", "ground", "rock"), "water": ("grass", "electric"), "grass": ("fire", "ice", "poison", "bug", "flying"), "electric": ("ground"), "ice": ("rock", "steel", "fire", "fighting"), "fighting": ("flying", "psychic"), "poison": ("ground", "psychic"), "ground": ("water", "grass", "ice"), "flying": ("ice", "electric", "rock"), "psychic": ("bug", "dark", "ghost"), "bug": ("rock", "fire", "flying"), "rock": ("fighting", "water", "grass", "steel", "ground"), "ghost": ("ghost", "dark"), "dragon": ("ice", "dragon"), "dark": ("fighting", "bug"), "steel": ("fighting", "fire", "ground")}
weak = {"normal": (), "fire": ("fire", "grass", "ice", "bug", "steel"), "water": ("water", "fire", "ice", "steel"), "grass": ("grass", "water", "electric", "ground"), "electric": ("electric", "flying", "ground", "steel"), "ice": ("ice"), "fighting": ("bug", "rock", "dark"), "poison": ("poison", "grass", "fighting", "bug"), "ground": ("rock", "poison", "bug"), "flying": ("grass", "bug", "fighting"), "psychic": ("psychic", "fighting"), "bug": ("grass", "fighting", "ground"), "rock": ("normal", "fire", "poison", "flying"), "ghost": ("poison", "bug"), "dragon": ("fire", "water", "grass", "electric"), "dark": ("ghost", "dark"), "steel": ("rock", "normal", "flying", "steel", "grass", "ice", "psychic", "bug", "dragon")}
immune = {"normal": ("ghost"), "ground": ("electric"), "flying": ("ground"), "ghost": ("normal", "fighting"), "dark": ("psychic"), "steel": ("poison")}
os.system("")
mode = input(RESET + "easy (e) or hard (h) or opMons (o)?\n")
while mode != 'e' and mode != 'h' and mode != 'o':
    os.system("Clear")
    os.system("")
    mode = input(RESET + "easy (e) or hard (h) or opMons (o)?\n")

def extract_file_data():
    with open("moves.txt") as f:
        moves_options = f.readlines()
        f.close()
    for i in range(len(moves_options)):
        if i != len(moves_options) - 1:
            moves_options[i] = moves_options[i][:-1]
        moves_options[i] = moves_options[i].split(" ")

    with open ("pokemon.txt") as f:
        pokemon_options = f.readlines()
        f.close()
    for i in range(len(pokemon_options)):
        if i != len(pokemon_options) - 1:
            pokemon_options[i] = pokemon_options[i][:-1]
        pokemon_options[i] = pokemon_options[i].split(" ", 9)
        newNine = []
        currentstr = ""
        for str in pokemon_options[i][9]:
            if str != " ":
                if str != "[" and str != "]":
                    currentstr += str
            else:
                newNine.append(currentstr)
                currentstr = ""
        pokemon_options[i][9] = newNine
    return moves_options, pokemon_options


def main():
    class move:
        def __init__(self, name, power, accuracy, version, type, col):
            self.name = name
            self.power = power
            self.accuracy = accuracy
            self.version = version
            self.type = type
            if type == "normal": self.col = WHITE
            if type == "fire": self.col = RED
            if type == "water": self.col = BLUE
            if type == "grass": self.col = GREEN
            if type == "electric": self.col = YELLOW
            if type == "ice": self.col = CYAN
            if type == "fighting": self.col = ORANGE
            if type == "poison": self.col = MAGENTA
            if type == "ground": self.col = ORANGE
            if type == "flying": self.col = LIGHTBLUE
            if type == "psychic": self.col = PINK
            if type == "bug": self.col = LIGHTGREEN
            if type == "rock": self.col = DARKGREY
            if type == "ghost": self.col = PURPLE
            if type == "dragon": self.col = BROWN
            if type == "dark": self.col = BLACK
            if type == "steel": self.col = LIGHTGREY
        
        def get_name(self):
            return self.name
        def get_power(self):
            return int(self.power)
        def get_accuracy(self):
            return int(self.accuracy)
        def get_version(self):
            return self.version
        def get_type(self):
            return self.type
        def get_col(self):
            return self.col

    class pokemon:
        def __init__(self, name, t1, t2, hp, attack, defense, spattack, spdefense, speed, available_moves, maxhp):
            self.name = name
            self.t1 = t1
            self.t2 = t2
            self.hp = hp
            self.attack = attack
            self.defense = defense
            self.spattack = spattack
            self.spdefense = spdefense
            self.speed = speed
            self.available_moves = available_moves
            self.moves = []
            self.maxhp = hp
            while len(self.moves) < 4:
                option = random.choice(move_options)
                if option[0] in available_moves: 
                    ok = True
                    for mov in self.moves:
                        if option[0] == mov.get_name():
                            ok = False
                            break
                    if ok:
                        newMove = move(option[0], option[1], option[2], option[3], option[4], "")
                        self.moves.append(newMove)

        def get_name(self):
            return self.name
        def get_t1(self):
            return self.t1
        def get_t2(self):
            return self.t2
        def get_hp(self):
            return int(self.hp)
        def get_attack(self):
            return int(self.attack)
        def get_defense(self):
            return int(self.defense)
        def get_spattack(self):
            return int(self.spattack)
        def get_spdefense(self):
            return int(self.spdefense)
        def get_speed(self):
            return int(self.speed)
        def get_available_moves(self):
            return self.available_moves
        def get_moves(self):
            return self.moves
        def get_maxhp(self):
            return int(self.maxhp)
        def set_hp(self, hp):
            self.hp = hp

    def pick_mons():
        mons, team = [], []
        bot_mons, bot_team = [], []
        if mode == 'o':
            mons = ['filler' * 6]
            team.append(pokemon("Arceus", "normal", "none", "120", "120", "120", "120", "120", "120", "[outrage doubleedge closecombat energyball]", []))
            team.append(pokemon("Dialga", "dragon", "steel", "100", "120", "120", "150", "100", "90", "[flashcannon dracometeor dragonpulse aurasphere]", []))
            team.append(pokemon("Palkia", "dragon", "water", "90", "120", "100", "150", "120", "100", "[surf dragonpulse earthpower hydropump]", []))
            team.append(pokemon("Giratina", "dragon", "ghost", "150", "100", "120", "100", "120", "90", "[phantomforce dracometeor shadowball earthquake]", []))
            team.append(pokemon("Rayquaza", "dragon", "flying", "105", "150", "90", "150", "90", "95", "[dragonrush dracometeor fly bravebird thunder blizzard flamethrower earthquake]", []))
            team.append(pokemon("Mewtwo", "psychic", "none", "106", "110", "90", "154", "90", "130", "[flamethrower psychic sludgewave thunderbolt]", []))
        while len(mons) < 6 and mode != 'o':
            mon = random.choice(pokemon_options)
            if mon not in mons:
                pok = pokemon(mon[0], mon[1], mon[2], mon[3], mon[4], mon[5], mon[6], mon[7], mon[8], mon[9], [])
                team.append(pok)
                mons.append(mon)
                pokemon_options.remove(mon)
        while len(bot_mons) < 6:
            mon = random.choice(pokemon_options)
            if mon not in bot_mons:
                pok = pokemon(mon[0], mon[1], mon[2], mon[3], mon[4], mon[5], mon[6], mon[7], mon[8], mon[9], [])
                bot_team.append(pok)
                bot_mons.append(mon)
                pokemon_options.remove(mon)
        return (team, bot_team)

    def get_choice(current):
        os.system("CLEAR")
        print(RESET + "YOUR POKEMON: " + mons[0].get_name() + " " * (20 - len(mons[0].get_name())) + "HP: " + str(round(mons[0].get_hp() / mons[0].get_maxhp() * 100, 2)) + "%")
        os.system("")
        for i in range(len(mons[0].get_moves())):
            print(mons[0].get_moves()[i].get_col() + str(i) + ": " + mons[0].get_moves()[i].get_name() + " (" + mons[0].get_moves()[i].get_type() + ")")
        os.system("")
        print(RESET + "\nENEMY POKEMON: " + bot_mons[0].get_name() + " " * (19 - len(bot_mons[0].get_name())) + "HP: " + str(round(bot_mons[0].get_hp() / bot_mons[0].get_maxhp() * 100, 2)) + "%")
        os.system("")
        choice = input(RESET + "\nWhich move would you like to do? (s to switch) (i for info)\n")
        while choice != 's' and choice != 'i' and choice not in list(map(lambda x: str(x), range(4))):
            get_choice(current)
        if choice.lower() == 's':
            switch(mons[0])
            get_choice(mons[0])
        elif choice.lower() == 'i':
            os.system("Clear")
            print("Your Pokemon: ")
            i = 0
            for mon in mons:
                print(str(i) + ": " + mon.get_name())
                i += 1
            print("Amount of pokemon remaining: " + str(len(mons)))
            print("\nCurrent Enemy Pokemon: ")
            print(str(i) + ": " + bot_mons[0].get_name())
            print("Amount of enemy pokemon remaining: " + str(len(bot_mons)))
            choice = input("\nPick a number to get info on a pokemon (or c to cancel)\n")
            while choice != 'c' and choice not in list(map(lambda x: str(x), range(len(mons) + 1))):
                os.system("Clear")
                print("Your Pokemon: ")
                i = 0
                for mon in mons:
                    print(str(i) + ": " + mon.get_name())
                    i += 1
                print("Amount of pokemon remaining: " + str(len(mons)))
                print("\nCurrent Enemy Pokemon: ")
                print(str(i) + ": " + bot_mons[0].get_name())
                print("Amount of enemy pokemon remaining: " + str(len(bot_mons)))
                choice = input("\nPick a number to get info on a pokemon (or c to cancel)\n")
            if choice.lower() == 'c':
                pass
            else:
                os.system("Clear")
                i = int(choice)
                if i < len(mons):
                    if "none" != mons[i].get_t2():
                        print(mons[i].get_name() + " (" + mons[i].get_t1() + ", " + mons[i].get_t2() + ")\n")
                    else:
                        print(mons[i].get_name() + " (" + mons[i].get_t1() + ")")
                    os.system("")
                    for move in mons[i].get_moves():
                        print(move.get_col() + move.get_name() + ": " + str(move.get_power()) + " power, (" + move.get_type() + ")")
                    print(RESET + "\nStats: ")
                    print("HP: " + str(mons[i].get_hp()))
                    print("Attack: " + str(mons[i].get_attack()))
                    print("Defense: " + str(mons[i].get_defense()))
                    print("Special Attack: " + str(mons[i].get_spattack()))
                    print("Special Defense: " + str(mons[i].get_spdefense()))
                    print("Speed: " + str(mons[i].get_speed()))
                else:
                    if "none" != bot_mons[0].get_t2():
                        print(bot_mons[0].get_name() + " (" + bot_mons[0].get_t1() + ", " + bot_mons[0].get_t2() + ")\n")
                    else:
                        print(bot_mons[0].get_name() + " (" + bot_mons[0].get_t1() + ")")
                    for move in bot_mons[0].get_moves():
                        print(move.get_col() + move.get_name() + ": " + str(move.get_power()) + " power, (" + move.get_type() + ")")
                    print(RESET + "\nStats: ")
                    print("HP: " + str(bot_mons[0].get_hp()))
                    print("Attack: " + str(bot_mons[0].get_attack()))
                    print("Defense: " + str(bot_mons[0].get_defense()))
                    print("Special Attack: " + str(bot_mons[0].get_spattack()))
                    print("Special Defense: " + str(bot_mons[0].get_spdefense()))
                    print("Speed: " + str(bot_mons[0].get_speed()))
                input(UNDERLINE + "\nPress enter to leave\n")
        else:
            best_option = 0
            if mode == 'h' or mode == 'o':
                options = []
                player_types = [mons[0].get_t1(), mons[0].get_t2()]
                for mon in bot_mons:
                    score = 0
                    types = [mon.get_t1(), mon.get_t2()]
                    tests = []
                    tests.append(move_mult(types[0], player_types))
                    tests.append(move_mult(types[1], player_types))
                    for test in tests:
                        if test == 0:
                            score -= 3
                        elif test == 0.25:
                            score -= 2
                        elif test == 0.5:
                            score -= 1
                        elif test == 1:
                            pass
                        elif test == 2:
                            score += 1
                        elif test == 4:
                            score += 2
                    tests = []
                    tests.append(move_mult(player_types[0], types))
                    tests.append(move_mult(player_types[1], types))
                    for test in tests:
                        if test == 0:
                            score += 3
                        elif test == 0.25:
                            score += 2
                        elif test == 0.5:
                            score += 1
                        elif test == 1:
                            pass
                        elif test == 2:
                            score -= 1
                        elif test == 4:
                            score -= 2
                    options.append(score)
                best_option = options.index(max(options))

            if best_option == 0:                         
                os.system("Clear")
                if mons[0].get_speed() >= bot_mons[0].get_speed():
                    attack(mons[0].get_moves()[int(choice)])
                    if bot_mons[0].get_hp() > 0:
                        enemy_attack(mons[0])
                        if mons[0].get_hp() <= 0:
                            print("Your " + mons[0].get_name() + " has fainted.")
                            mons.pop(0)
                            time.sleep(2)
                            if len(mons) == 0:
                                print("YOU LOSE")
                                sys.exit()
                            switch("dead")
                    else:
                        print("The enemy " + bot_mons[0].get_name() + " has fainted.")
                        time.sleep(2)
                        bot_mons.pop(0)
                        if len(bot_mons) == 0:
                            print("YOU WIN")
                            sys.exit()
                        best_option = bot_dead()
                        temp = bot_mons[best_option]
                        bot_mons[best_option] = bot_mons[0]
                        bot_mons[0] = temp
                        print("The enemy sent out " + bot_mons[0].get_name() + ".")
                        time.sleep(1)
                else:
                    enemy_attack(mons[0])
                    if mons[0].get_hp() > 0:
                        attack(mons[0].get_moves()[int(choice)])
                        if bot_mons[0].get_hp() <= 0:
                            print("The enemy " + bot_mons[0].get_name() + " has fainted.")
                            time.sleep(2)
                            bot_mons.pop(0)
                            if len(bot_mons) == 0:
                                print("YOU WIN")
                                sys.exit()
                            best_option = bot_dead()
                            temp = bot_mons[best_option]
                            bot_mons[best_option] = bot_mons[0]
                            bot_mons[0] = temp
                            print("The enemy sent out " + bot_mons[0].get_name() + ".")
                            time.sleep(1)
                    else:
                        print("Your " + mons[0].get_name() + " has fainted.")
                        mons.pop(0)
                        time.sleep(2)
                        if len(mons) == 0:
                            print("YOU LOSE")
                            sys.exit()
                        switch("dead")
            else:
                os.system("Clear")
                temp = bot_mons[best_option]
                bot_mons[best_option] = bot_mons[0]
                bot_mons[0] = temp
                print("The enemy switched to " + bot_mons[0].get_name() + ".")
                time.sleep(1)
                attack(mons[0].get_moves()[int(choice)])
                if bot_mons[0].get_hp() <= 0:
                    print("The enemy " + bot_mons[0].get_name() + " has fainted.")
                    time.sleep(2)
                    bot_mons.pop(0)
                    if len(bot_mons) == 0:
                        print("YOU WIN")
                        sys.exit()
                    best_option = bot_dead()
                    temp = bot_mons[best_option]
                    bot_mons[best_option] = bot_mons[0]
                    bot_mons[0] = temp
                    print("The enemy sent out " + bot_mons[0].get_name() + ".")
                    time.sleep(1)

    def attack(move):
        print("Your " + mons[0].get_name() + " used " + move.get_name())
        dmg = move.get_power()
        accuracy = move.get_accuracy()
        tmove = move.get_type()
        if move.get_version() == 'p':
            attack = mons[0].get_attack()
            defense = bot_mons[0].get_defense()
        else:
            attack = mons[0].get_spattack()
            defense = bot_mons[0].get_spdefense()
        if random.randrange(0, 100) > accuracy:
            print("You Missed!")
        else:
            ran = random.randrange(95, 105) * 0.01
            stab = 1
            crit = 1
            if random.randrange(0, 100) > 91:
                crit = 1.5
            if tmove == mons[0].get_t1() or tmove == mons[0].get_t2:
                stab = 1.5
            mult = move_mult(tmove, [bot_mons[0].get_t1(), bot_mons[0].get_t2()])
            if mult == 0:
                print("There is no effect.")
            elif mult < 1:
                print("It's Not very effective.")
            elif mult > 1:
                print("It's super effective!")
            if crit == 1.5:
                print("A Critical Hit!")
            total = ran * crit * stab * mult * dmg * attack / defense / 5
            current_hp = bot_mons[0].get_hp()
            bot_mons[0].set_hp(current_hp - total)
        time.sleep(2)
    
    def enemy_attack(current):
        if mode == "e":
            move_bot = random.choice(bot_mons[0].get_moves())
            print("The enemy " + bot_mons[0].get_name() + " used " + move_bot.get_name())
            dmg = move_bot.get_power()
            accuracy = move_bot.get_accuracy()
            tmove = move_bot.get_type()
            if move_bot.get_version() == 'p':
                attack = bot_mons[0].get_attack()
                defense = mons[0].get_defense()
            else:
                attack = bot_mons[0].get_spattack()
                defense = mons[0].get_spdefense()
            if random.randrange(0, 100) > accuracy:
                print("The enemy " + bot_mons[0].get_name() +  " Missed!")
            else:
                ran = random.randrange(95, 105) * 0.01
                stab = 1
                crit = 1
                if random.randrange(0, 100) > 91:
                    crit = 1.5
                if tmove == bot_mons[0].get_t1() or tmove == bot_mons[0].get_t2:
                    stab = 1.5
                mult = move_mult(tmove, [mons[0].get_t1(), mons[0].get_t2()])
                if mult == 0:
                    print("There is no effect.")
                elif mult < 1:
                    print("It's Not very effective.")
                elif mult > 1:
                    print("It's super effective!")
                if crit == 1.5:
                    print("A Critical Hit!")
                total = stab * crit * ran * mult * dmg * attack / defense / 5
                current_hp = mons[0].get_hp()
                mons[0].set_hp(current_hp - total)
            time.sleep(2)
        else:
            type_player = [mons[0].get_t1(), mons[0].get_t2()]
            type_enemy = [bot_mons[0].get_t1(), bot_mons[0].get_t2()]
            dmgs = []
            for move in bot_mons[0].get_moves():
                dmg = move.get_power()
                if move.get_version() == 'p':
                    attack = bot_mons[0].get_attack()
                    defense = mons[0].get_defense()
                else:
                    attack = bot_mons[0].get_spattack()
                    defense = mons[0].get_spdefense()
                mult = move_mult(move.get_type(), [mons[0].get_t1(), mons[0].get_t2()])
                stab = 1
                if move.get_type() in type_enemy:
                    stab = 1.5
                dmgs.append(stab * mult * dmg * attack / defense / 5)
                most = 0
            for i in range(len(dmgs)):
                if dmgs[i] > dmgs[most]:
                    most = i
            mult = move_mult(bot_mons[0].get_moves()[most].get_type(), [mons[0].get_t1(), mons[0].get_t2()])
            print("The enemy " + bot_mons[0].get_name() + " used " + bot_mons[0].get_moves()[most].get_name())
            accuracy = bot_mons[0].get_moves()[most].get_accuracy()
            if random.randrange(0, 100) > accuracy:
                print("The enemy " + bot_mons[0].get_name() + " missed.")
            else:
                if mult == 0:
                    print("There is no effect.")
                elif mult < 1:
                    print("It's Not very effective.")
                elif mult > 1:
                    print("It's super effective!")
                total = dmgs[most]
                ran = random.randrange(95, 105) * 0.01
                crit = 1
                if random.randrange(0, 100) > 91:
                    crit = 1.5
                if crit == 1.5:
                    print("A Critical Hit!")
                total = total * crit * ran
                current_hp = mons[0].get_hp()
                mons[0].set_hp(current_hp - total)
            time.sleep(2)
    
    def bot_dead():
        best_option = 0
        if mode == 'h' or mode == 'o':
            options = []
            player_types = [mons[0].get_t1(), mons[0].get_t2()]
            for mon in bot_mons:
                score = 0
                types = [mon.get_t1(), mon.get_t2()]
                tests = []
                tests.append(move_mult(types[0], player_types))
                tests.append(move_mult(types[1], player_types))
                for test in tests:
                    if test == 0:
                        score -= 3
                    elif test == 0.25:
                        score -= 2
                    elif test == 0.5:
                        score -= 1
                    elif test == 1:
                        pass
                    elif test == 2:
                        score += 1
                    elif test == 4:
                        score += 2
                tests = []
                tests.append(move_mult(player_types[0], types))
                tests.append(move_mult(player_types[1], types))
                for test in tests:
                    if test == 0:
                        score += 3
                    elif test == 0.25:
                        score += 2
                    elif test == 0.5:
                        score += 1
                    elif test == 1:
                        pass
                    elif test == 2:
                        score -= 1
                    elif test == 4:
                        score -= 2
                options.append(score)
            best_option = options.index(max(options))
        return best_option

    def switch(mode):
        os.system("Clear")
        for i in range(len(mons)):
            if mode == "dead":
                print(str(i) + ": " + mons[i].get_name() + ": " + mons[i].get_t1() + " " + mons[i].get_t2())
            else:
                if i != 0:
                    print(str(i) + ": " + mons[i].get_name() + ": " + mons[i].get_t1() + " " + mons[i].get_t2())
        print("\nEnemy Pokemon: " + bot_mons[0].get_name() + ": " + bot_mons[0].get_t1() + " " + bot_mons[0].get_t2()) 
        if mode == "dead":
            choice = input("\nWhich pokemon would you like to switch to?\n")
            while choice not in list(map(lambda x: str(x), range(len(mons)))):
                os.system("Clear")
                for i in range(len(mons)):
                    if mode == "dead":
                        print(str(i) + ": " + mons[i].get_name() + ": " + mons[i].get_t1() + " " + mons[i].get_t2())
                    else:
                        if i != 0:
                            print(str(i) + ": " + mons[i].get_name() + ": " + mons[i].get_t1() + " " + mons[i].get_t2())
                print("\nEnemy Pokemon: " + bot_mons[0].get_name() + ": " + bot_mons[0].get_t1() + " " + bot_mons[0].get_t2()) 
                choice = input("\nWhich pokemon would you like to switch to?\n")
        else:
            choice = input("\nWhich pokemon would you like to switch to? (c to cancel)\n")
            while choice != 'c' and choice not in list(map(lambda x: str(x), range(1, len(mons)))):
                os.system("Clear")
                for i in range(len(mons)):
                    if mode == "dead":
                        print(str(i) + ": " + mons[i].get_name() + ": " + mons[i].get_t1() + " " + mons[i].get_t2())
                    else:
                        if i != 0:
                            print(str(i) + ": " + mons[i].get_name() + ": " + mons[i].get_t1() + " " + mons[i].get_t2())
                print("\nEnemy Pokemon: " + bot_mons[0].get_name() + ": " + bot_mons[0].get_t1() + " " + bot_mons[0].get_t2()) 
                choice = input("\nWhich pokemon would you like to switch to? (c to cancel)\n")
        if choice.lower() == 'c':
            get_choice(mons[0])
        elif mode != "dead":
            temp = mons[int(choice)]
            mons[int(choice)] = mons[0]
            mons[0] = temp
            print("You switched to " + mons[0].get_name() + ".")
            time.sleep(1)
            enemy_attack(mons[0])
            if mons[0].get_hp() <= 0:
                print("Your " + mons[0].get_name() + " has fainted.")
                mons.pop(0)
                time.sleep(2)
                if len(mons) == 0:
                    print("YOU LOSE")
                    sys.exit()
                switch("dead")
        else:
            temp = mons[int(choice)]
            mons[int(choice)] = mons[0]
            mons[0] = temp
            print("You switched to " + mons[0].get_name() + ".")
            time.sleep(1)

    def move_mult(tmove, t):
        mult = 1
        for type in t:
            if type.lower() != "none" and tmove!= "none":
                if type in strong and tmove in strong[type]:
                    mult *= 2
                elif type in weak and tmove in weak[type]:
                    mult /= 2
                elif type in immune and tmove in immune[type]:
                    mult = 0
        return mult

    move_options, pokemon_options = extract_file_data()
    mons, bot_mons = pick_mons()
    os.system("Clear")
    print("YOUR POKEMON:")
    os.system("")
    for mon in mons:
        print(RESET + mon.get_name(), end=": ")
        for mov in mon.get_moves():
            print(mov.get_col() + mov.get_name(), end=" ")
        print()
    print(RESET + "\nENEMY POKEMON:")
    for mon in bot_mons:
        print(RESET + mon.get_name(), end=": ")
        for mov in mon.get_moves():
            print(mov.get_col() + mov.get_name(), end=" ")
        print(RESET)
    input(UNDERLINE + "\nPress Enter to Start\n")
    os.system("")
    current = mons[0]
    current_bot = bot_mons[0]

    while len(mons) > 0 and len(bot_mons) > 0:
        get_choice(current)

    if len(mons) == 0:
        print("YOU LOST")
    else:
        print("YOU WIN")

if __name__ == "__main__":
    main()
