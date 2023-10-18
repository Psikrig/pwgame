import random
import sys
print("Вы входите в древние катакомбы, легенды гласят о чудодейственном артефакте, который здесь запрятан")
try:
        print("кто ты, воин?"
              "\n 1) Варвар - высокая атака, но с защитой все плохо, ведь мертвые не кусаются"
              "\n 2) Наемник - баланс защиты и атаки, да, я не определился, что для меня важнее"
              "\n 3) Рыцарь - высокая защита, а вот с атакой проблемы, своя шкура важнее удобства ")
        h = int(input("Я "))

except: print("так не пойдет, для выбора используйте цифры")
hero = ["class", "def", "agi", "str", "hp max", "hp"]
monster = ["class", "def", "agi", "str", "hp max", "hp"]
if h == 1:
    hero[0] = "варвар"
    hero[1] = 25
    hero[2] = 20
    hero[3] = 3
    hero[4] = 10
    hero[5] = 10
elif h == 2:
    hero[0] = "наемник"
    hero[1] = 50
    hero[2] = 10
    hero[3] = 2
    hero[4] = 15
    hero[5] = 15
elif h == 3:
    hero[0] = "рыцарь"
    hero[1] = 75
    hero[2] = 0
    hero[3] = 1
    hero[4] = 20
    hero[5] = 20
else:
    hero[0] = "варвар"
    hero[1] = 25
    hero[2] = 20
    hero[3] = 3
    hero[4] = 10
    hero[5] = 10
monster[0] = "блёб"
monster[1] = 75
monster[2] = 0
monster[3] = 1
monster[4] = 7
monster[5] = 7

def battle():
    print("на вас нападает", monster[0], ".\t его здоровье =", monster[5])
    while monster[5] > 0 and hero[5] > 0:
         try:
            print("ваше здоровье:", hero[5], "из", hero[4], "\t здоровье монстра:", monster[5], "из", monster[4])
            a = int(input("ваши действия:"
                          "\n 1) удар оружием"
                          "\n 2) защита \n"))

            print(a)
            if a == 1:
                q = random.randint(0, 100)
                if (q + hero[2]) > monster[1]:
                    monster[5] = monster[5] - hero[3]
                    print("вы нанесли", hero[3], "урон")
                else:
                    print("промах")
            elif a == 2:
                hero[2] = hero[2] + 25
                if hero [5] != hero[4]:
                 hero[5] = hero[5] + 1
            else:
                print("вы пропустили ход")
            q = random.randint(0, 100)
            if (q + monster[2]) > hero[1]:
                hero[5] = hero[5] - monster[3]
                print(monster[0], "нанес вам", monster[3], "урон")
            else:
                print(monster[0], " промахнулся")
            if a == 2:
                hero[2] = hero[2] - 25
         except:
             print("выбор совершается цифрами1")
    if (monster[5] <= 0):
        print("победа")
        hero[5] = hero[4]

def chest():
    e = random.randint(1, 4)
    if e == 1:
        print("вы нашли доспех получше")
        hero[1]=hero[1]+20
    if e == 2:
        print("вы нашли зелье ловкости")
        hero[2]=hero[2]+10
    if e == 3:
        print("вы нашли оружие получше")
        hero[3]=hero[3]+1
    if e == 4:
        print("вы нашли зелье увеличения выносливости")
        hero[4]=hero[4]+5



def e():
    x = 1
    while x == 1:
     if hero[5] < 1:
            quit("гамовер")
     try:

            print("перед вами 2 двери, пойти: 1)направо, 2)налево")
            z = int(input())
            if z == 1:
                br1(b1)
            elif z == 2:
                br2(b2)
            break
     except:
            print("выбор совершается цифрами e1")


b1 = 1
def br1(b1):
    x = 1
    if b1 == 0:
      while x == 1:
         if hero[5] < 1:
             quit("гамовер")
      try:
        print("коридор пуст")
        print("Вы стоите в коридоре, куда пойти: 1)вперед или 2)назад?")
        a = int(input())
        if a == 2:
            e()
        elif a == 1:
            cr1(cr1)
      except:
          print("выбор совершается цифрами бр1")
    elif b1 == 1:
     while x == 1:
        try:
            monster[0] = "блёб"
            monster[1] = 75
            monster[2] = 0
            monster[3] = 1
            monster[4] = 7
            monster[5] = 7
            print("к вашим ногам течет бесформенная, но живая слизь, на вас напал блёб")
            battle()
            print("Вы стоите в коридоре, куда пойти: 1)вперед или 2)назад?")
            a = int(input())
            b1 = 0
            if a == 2:

                e()
            elif a == 1:

                cr1(c1)
            break
        except:
            print("выбор совершается цифрами бр1.2")

    if b1 == 0:
     while x == 1:
      try:
        print("коридор пуст")
        print("Вы стоите в коридоре, куда пойти: 1)вперед или 2)назад?")
        a = int(input())
        if a == 2:
            e()
        elif a == 1:
            cr1(cr1)
        break
      except:
          print("выбор совершается цифрами")

b2 = 1
v =1
def br2(b2):
    if b2 == 1:

            print("когда вы входите в комнату, зрелище механического медведя потрясает вас, а его рык потрясает стены")
            monster[0] = "механический медведь"
            monster[1] = 0
            monster[2] = 5
            monster[3] = 5
            monster[4] = 4
            monster[5] = 4
            battle()
            b2 = 0
            while v == 1:
             if hero[5] < 1:
                    quit("гамовер")
             try:
              print("Вы стоите в коридоре, куда пойти: 1)вперед или 2)назад?")
              a = int(input())
              if a == 2:
                b2 = 0
                e()
                break
              else:
                br3(b3)
                break
             except:
              print("выбор совершается цифрами бр2")
    elif b2 == 0:
        while v == 1:
            if hero[5] < 1:
                quit("гамовер")
            try:
                print("коридор пуст")
                print("Вы стоите в коридоре, куда пойти: 1)вперед или 2)назад?")
                a = int(input())
                if a == 2:
                    e()
                    break
                elif a == 1:
                    br3(b3)
                    break

            except:
                print("выбор совершается цифрами бр22")


c1 = 1
def cr1(c1):
    print("вы входите в комнату, тут стоит сундук")
    x = 1
    if c1 == 1:
     while x == 1:
        if hero[5] < 1:
            quit("гамовер")
        try:
            chest()
            print("тут тупик, вы возвращаетесь к входу в подземелье")
            c1 = 0
            e()
        except:
            print("выбор совершается цифрами")
    elif c1 == 0:
        print("тут пусто и тупик, вы возвращаетесь к входу в подземелье")
        e()
b3=1
def br3(b3):
    i = 1
    if b3 == 1:
     while i == 1:
        if hero[5] < 1:
             quit("гамовер")
        try:
            print("из темного утра выскочил шкилет!")
            monster[0] = "шкилет"
            monster[1] = 95
            monster[2] = 25
            monster[3] = 3
            monster[4] = 1
            monster[5] = 1
            battle()
            print("Вы видите дверь, но можете идти дальше по коридору, куда идти: 1)дальше по коридору, 2)пройти в дверь, 3)назад")
            x =int(input())
            if x == 1:
                b3 = 0
                br4(b4)
            elif x == 2:
                b3 = 0
                cr2(c2)
            elif x == 3:
                b3 = 0
                br2(b2)
        except:
            print("выбор совершается цифрами")
    elif b3 == 0:
     while i == 1:
         if hero[5] < 1:
             quit("гамовер")
         try:
             print("Вы видите дверь, но можете идти дальше по коридору, куда идти: 1)дальше по коридору, 2)пройти в дверь, 3)назад")
             x = int(input())
             if x == 1:
                 b3 = 0
                 br4(b4)
             elif x == 2:
                 b3 = 0
                 cr2(c2)
             elif x == 3:
                 b3 = 0
                 br2(b2)
         except:
             print("выбор совершается цифрами")

b4 = 1
c2 = 1
def br4(b4):
    i = 1
    if b4 == 1:
        while i == 1:
            if hero[5] < 1:
                quit("гамовер")
            try:
                print("Перед вами поднимаются, как казалось, пустой доспех")
                monster[0] = "темный рыцарь"
                monster[1] = 75
                monster[2] = 0
                monster[3] = 1
                monster[4] = 15
                monster[5] = 15
                battle()
                print("Вы видите дверь, куда идти: 1)пройти в дверь, 2)назад")
                x = int(input())
                if x == 1:
                    b4 = 0
                    bossr1(boss1)
                elif x == 2:
                    b4 = 0
                    br3(b3)
            except:
                print("выбор совершается цифрами")
    elif b4 == 0:
        while i == 1:
            try:
                print("Вы видите дверь, куда идти: 1)пройти в дверь, 2)назад")
                x = int(input())
                if x == 1:
                    b4 = 0
                    bossr1(boss1)
                elif x == 2:
                    b4 = 0
                    br3(b3)
            except:
                print("выбор совершается цифрами")
def cr2(c2):
    x=1
    print("вы входите в комнату, тут стоит сундук")
    x = 1
    if c2 == 1:
        while x == 1:
            try:
                chest()
                print("тут больше ничего нет, вы выходите из комнаты")
                c1 = 0
                br3(b3)
            except:
                print("выбор совершается цифрами")
    elif c2 == 0:
        print("тут больше ничего нет, вы выходите из комнаты")
        c1 = 0
        br3(b3)
boss1 = 1
def bossr1(boss1):
    boss = ["class", "def", "agi", "str", "hp max", "hp"]
    boss[0] = "Лич"
    boss[1] = 50
    boss[2] = 0
    boss[3] = 1
    boss[4] = 10
    boss[5] = 10
    while boss[5] > 0 and hero[5] > 0:
        try:
            print("ваше здоровье:", hero[5], "из", hero[4], "\t здоровье монстра:", boss[5], "из", boss[4])
            a = int(input("ваши действия:"
                          "\n 1) удар оружием"
                          "\n 2) защита \n"))
            if a == 1:
                q = random.randint(0, 100)
                if (q + hero[2]) > boss[1]:
                    boss[5] = boss[5] - hero[3]
                    print("вы нанесли", hero[3], "урон")
                else:
                    print("промах")
            elif a == 2:
                hero[2] = hero[2] + 25
            else:
                print("вы пропустили ход")
            a = hero[5]
            print("Лич призывает шкилета поменьшбе")
            monster[0] = "шкилет поменьшбе"
            monster[1] = 25
            monster[2] = 25
            monster[3] = 3
            monster[4] = 1
            monster[5] = 1
            battle()
            hero[5] = a
        except:
            print("выбор совершается цифрами")
    if (monster[5] <= 0):
        print("победа")
        hero[5] = hero[4]
        sys.exit(("вы нашли сокровище и вернулись из подземелья!"))
    else:
        quit("game, как говорится, over")
e()