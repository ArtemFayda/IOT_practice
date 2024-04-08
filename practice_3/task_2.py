class Dog():
    def __init__(self,name, age):
        self._name=name
        self._age=age
    def Sit(self):
        print(self._name,"села")
    def Roll_over(self):
        print(self._name,"перекатывается")
myDog=Dog("Lord", 3)
myDog1=Dog("Bublik",5)
myDog.Sit()
myDog.Roll_over()
myDog1.Sit()
myDog1.Roll_over()