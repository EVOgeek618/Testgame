
init python:

    class Inventory:
        position = []
        things = []
        for i in range(8):
            for j in range(3):
                position.append((270+i*125,80+j*125,112,112))
        def add_thing(self, thing):
            self.things.append({"image":thing, "position":self.position[len(self.things)+1]})

    class Time:
        now = 0
        all_time = ["m","a","e","n"]
        time = all_time[now]

        def change_time(self):
            self.now += 1
            self.time = self.all_time[self.now % 4]

    def change_cursor(cur=None):
        if cur:
            config.mouse_displayable = MouseDisplayable(cur, 0, 0)
        else:
            config.mouse_displayable = None
            global cursor
            cursor = None
    cursor = None
    t = Time()
    i = Inventory()
    active = None
    i.add_thing("Interface/Отмычка_Икон.png")

define config.layers = [ 'master', 'transient', 'screens', 'overlay' ]
define m = Character("Milf")
image Korridor = im.FactorScale("Location/Korridor.jpg",1.1111)
image Restroom = im.FactorScale("Location/Restroom.jpg",1.1111)
image Hall = im.FactorScale("Location/Hall.jpg",1.1111)
image Kitchen = im.FactorScale("Location/Kitchen.jpg",1.1111)
image HoverKorridor = im.FactorScale("Location/HoverKorridor.jpg",1.1111)
image HoverRestroom = im.FactorScale("Location/HoverRestroom.jpg",1.1111)
image HoverHall = im.FactorScale("Location/HoverHall.jpg",1.1111)
image HoverKitchen = im.FactorScale("Location/HoverKitchen.jpg",1.1111)
image GG1 = im.FactorScale("Characters/GG1.png",0.7)
image M1 = im.FactorScale("Characters/M1.png",0.7)


label start:

label Kor:

    scene Korridor

label Choise:

    call screen Kor

    $ choise = _return

    if (choise == "to_bath" and t.time != "m") or (choise == "to_bath" and t.time == "m" and cursor=="Interface/Отмычка_Икон.png"):
        jump Rest
    elif choise == "to_bath" and t.time == "m":
        "Мама заперлась изнутри"
        scene Korridor
    elif choise == "to_hall":
        jump Ha
    elif choise == "to_kitchen":
        jump Kit

    jump Choise

label Rest:

    $change_cursor()

    scene Restroom

    show M1 at right

label Rest_choise:

    call screen Rest

    $ choise = _return


    if choise == "to_kor":
       jump Kor
    jump Rest_choise

label Ha:

    $change_cursor()

    scene Hall

    show M1 at right

label Ha_choise:

    call screen Ha
    $ choise = _return

    if choise == "to_kor":
       jump Kor
    jump Ha_choise

label Kit:

    $change_cursor()

    scene Kitchen

    show M1 at right

label Kit_choise:

    call screen Kit

    $ choise = _return

    if choise == "to_kor":
       jump Kor
    jump Kit_choise
    return


