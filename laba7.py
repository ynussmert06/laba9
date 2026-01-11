import os
class Employee():
    def __init__(self, id, name):
        self.name = name
        self.id = id
    def get_info(self):
        return f"Id: {self.id}, Name: {self.name}"

class Manager(Employee):
    def __init__(self, name, id, department):
        Employee.__init__(self,name, id)
        self.department = department
        
    def manage_project(self):
        if self.department == "tehnologi_shop":
            return "ok you goint to TEchManager"
        elif self.department == "help":
            return "ok you goint to TEchManager"
        elif self.department == "shop":
            return "ok you goint to TEchManager" 
        else:
            return "we dont need manager"
            
    def Manager_info(self):
       if Manager.manage_project(self) != "we dont need manager":
            return f"{super().get_info()}, Meneger: " + str(self.department)
       else:
           return "I asked you, we not need manager"
    
    
class Technik(Employee):
    def __init__(self, name, id, tech):
        Employee.__init__(self,name, id)
        self.tech = tech
    def Tech_project(self):
        if self.tech == "car":
            return "ok you goint to TEchManager"
        elif self.tech == "computer":
            return "ok you goint to TEchManager"
        else:
            return "we not need technik"
    def Tech_info(self):
         if Technik.Tech_project != "we not need technik":
            return f"{super().get_info()}, Tech: " + str(self.tech)
         else:
            return "I asked you, we not need technik"
class TechManager(Manager , Technik):
        def __init__(self, name, id, department, tech):
            Manager.__init__(self,name, id, department)
            Technik.__init__(self,name, id, tech)
        def get_info_Manager_card(self):
            if Manager.manage_project(self) != "we dont need manager":
                return ("========Your Meneger Card=========" + "\n"
                        "Name: " + self.name + "\n"
                        "id: " + self.id + "\n"
                        "deparment: " + self.department + "\n")
            else:
                return "you not have a status meneger"
        def get_info_Tech_card(self):
            if Technik.Tech_project(self) != "we not need technik": 
                return ("========Your TEchnik Card=========" + "\n"
                        "Name: " + self.name + "\n"
                        "id: " + self.id + "\n"
                        "tech: " + self.tech + "\n")
            else:
                return "you not have a status tech"
           
v = TechManager("9393", "y","tehnologi_shop", "car")
# карта менеджера
print(v.get_info_Manager_card())
# карта техника
print(v.get_info_Tech_card())
#имя и айди
print(v.get_info())

# инфо о технике
print(v.Tech_info())
print(v.Tech_project())

# инфо о менеджере
print(v.Manager_info())
print(v.manage_project())

#Просто вывод информации о человеке
# c = Employee("1929", "d")
# print(c.get_info())


#взаимодейсвие с классом менеджер
# c = Manager("2321", "dse", "tehnologi_shop")
# print(c.get_info())
# print(c.Manager_info())
# print(c.manage_project())

# c = Technik("2321", "dse", "car")
# print(c.get_info())
# print(c.Tech_info())
# print(c.Tech_project())
