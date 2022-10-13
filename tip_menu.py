class tip_menu():

    def __init__(self):
        self.x = 10
        self.spam = "test"

    def run(self):
        iMenu = 0
        while iMenu != 4:
            iMenu = self.main_menu()
            print(iMenu)
            if iMenu == 1:
                iMenuA = self.optionAmenu()
                print(iMenuA)
                if iMenuA == 1:
                    print("\tExecuting Function A-1 and then returning to Main Menu!")
                elif iMenuA == 2:
                    print("\tExecuting Function A-2 and then returning to Main Menu!")
                elif iMenuA == 3:
                    print("\tExecuting Function A-3 and then returning to Main Menu!")
                else:
                    print("Returning to Main Menu! and then returning to Main Menu!")
            elif iMenu == 2:
                iMenuB = optionBmenu()
                print(iMenuB)
            elif iMenu == 3:
                iMenuC = optionCmenu()
                print(iMenuC)

    def main_menu(self):
        print("\t\tTIP Main Menu")
        print("\t\t*************\n")
        print("\t1. Option A")
        print("\t2. Option B")
        print("\t3. Option C")
        print("\t4. Exit\n\n")
        sel = int(input("Enter Selection: "))
        return sel

    def optionAmenu(self):
        print("\t\tOption A Menu")
        print("\t\t*************\n")
        print("\t1. Option A 1")
        print("\t2. Option A 2")
        print("\t3. Option A 3\n\n")
        print("\t4. Return to Main Menu")
        sel = int(input("Enter Selection: "))
        return sel

    def optionBmenu(self):
        print("Option B Menu")
        print("*************")
        return 1

    def optionCmenu(self):
        print("Option C Menu")
        print("*************")
        return 1

