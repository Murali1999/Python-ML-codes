#heirarchical inheritance
#b,c->a
#d,e->b
#f,g,h->c
#a->b,c | b->d,e | c->f,g,h

class Aclass:
    def __init__(self,age):
        self.age=age
    def infoA(self):
        print(self.age)

class Bclass(Aclass):
    def __init__(b,name):
        b.name=name
    def infoB(b):
        print(b.name)

class Cclass(Aclass):
    def __init__(c,course):
        c.course=course
    def infoC(c):
        print(c.course.upper())
        
#inherits classes B and A
class Dclass(Bclass,Aclass):
    def __init__(d,city,name):
        d.city=city
        d.name=name
    def infoD(d):
        print('City -',d.city.upper())
        print('Name -',d.name.upper())

class Eclass(Bclass,Aclass):
    def __init__(e,gender):
        e.gender=gender
    def infoE(e):
        print('Gender -',e.gender.upper())

#inherits classes C and A
class Fclass(Cclass,Aclass):
    def __init__(f,state,age,course):
        f.state=state
        f.age=age
        f.course=course
    def infoF(f):
        print('State -',f.state.upper())
        print('Course -',f.course.upper())
        print('Age -',f.age)

class Gclass(Cclass,Aclass):
    def __init__(g,country):
        g.country=country
    def infoG(g):
        print('Country -',g.country.upper())

class Hclass(Cclass,Aclass):
    def __init__(h,clg):
        h.clg=clg
    def infoH(h):
        print('College -',h.clg.upper())

obj1=Aclass(19)
obj2=Bclass('Murali')
obj3=Cclass('csf')
obj4=Dclass('new delhi','Murali')
obj5=Eclass('m')
obj6=Fclass('delhi',19,'csf')
obj7=Gclass('india')
obj8=Hclass('upes')

obj4.infoD()
obj5.infoE()
obj6.infoF()
obj7.infoG()
obj8.infoH()
