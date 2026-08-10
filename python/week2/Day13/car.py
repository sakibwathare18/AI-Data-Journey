class car:

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.running = False

    def display(self):
        print(f"\nBrand : {self.brand} \nModel : {self.model} \nYear : {self.year}")

    def start(self):

        if not self.running:
            self.running = True
            print(f"{self.brand} {self.model} is started.....")
        else :
            print(f"{self.brand} {self.model} is already started.....")

    def stop(self):

        if self.running:
            self.running = False
            print(f"{self.brand} {self.model} is stoped.....")
        else :
            print(f"{self.brand} {self.model} is already stoped.....")


car1 = car("Hyundai","Creata",2023)

car1.display()

car1.start()

car1.stop()