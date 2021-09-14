
init python:
    class Time:
        now = 1
        all_time = ["m","a","e","n"]
        time = all_time[now]

        def change_time(self):
            self.now += 1
            self.time = self.all_time[self.now % 4]

    def Dialog():
        "Привет."
        m("Рада тебя видеть.")
        "Хорошего дня."
        m("И тебе того же.")

    t = Time()



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
    with dissolve

label Choise:

    $ choise = renpy.imagemap(
    im.FactorScale("Location/Korridor.jpg",1.1111),
    im.FactorScale("Location/HoverKorridor.jpg",1.1111),
    [(777, 222, 888, 555, "to_bath"),(1111, 0, 1500, 1000, "to_hall"),(0, 0, 222, 1000, "to_kitchen")],
     focus="imagemap")

    if choise == "to_bath" and t.time != "m":
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

    scene Restroom
    with dissolve

    if t.time=="m":
        call screen milf

    $ choise = renpy.imagemap(
    im.FactorScale("Location/Restroom.jpg",1.1111),
    im.FactorScale("Location/HoverRestroom.jpg",1.1111),
    [(0, 620, 1280, 720, "to_kor")],
     focus="imagemap")

    if choise == "to_kor":
        jump Kor

label Ha:

    scene Hall
    with dissolve

    if t.time=="e":
        call screen milf

    $ choise = renpy.imagemap(
    im.FactorScale("Location/Hall.jpg",1.1111),
    im.FactorScale("Location/HoverHall.jpg",1.1111),
    [(1000, 0, 1280, 720, "to_kor")],
     focus="imagemap")

    if choise == "to_kor":
       jump Kor

label Kit:

    scene Kitchen
    with dissolve

    if t.time=="a":
        call screen milf

    $ choise = renpy.imagemap(
    im.FactorScale("Location/Kitchen.jpg",1.1111),
    im.FactorScale("Location/HoverKitchen.jpg",1.1111),
    [(1100, 0, 1280, 720, "to_kor")],
     focus="imagemap")

    if choise == "to_kor":
       jump Kor

    return

