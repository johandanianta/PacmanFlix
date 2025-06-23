from tabulate import tabulate

data = {
    "Shandy": ["Basic Plan", 12, "shandy-2134"],
    "Cahya": ["Standard Plan", 24, "cahya-abcd"],
    "Ana": ["Premium Plan", 5, "ana-2f9g"],
    "Bagus": ["Basic Plan", 11, "bagus-9f92"]
}

class User:
    def __init__(self, username, duration_plan, current_plan):
        self.username = username
        self.duration_plan = duration_plan
        self.current_plan = current_plan

    def check_benefit(self):
        headers = ["Services", "Basic Plan", "Standard Plan", "Premium Plan"]
        
        table = [
            ["Bisa Stream", True, True, True],
            ["Bisa Download", True, True, True],
            ["Bisa Kualitas SD", True, True, True],
            ["Bisa Kualitas HD", False, True, True],
            ["Bisa Kualitas UHD", False, False, True],
            ["Number Devices", 1, 2, 4],
            ["Jenis Konten", "3rd party Movie Only", 
             "Basic Plan Content + Sports", 
             "Basic Plan + Standard Plan + PacFlix Original Series"],
            ["Harga", "120,000", "160,000", "200,000"]
        ]

        print("\nPacflix Plan Member Benefits")
        print(tabulate(table, headers, tablefmt="grid"))

    def check_plan(self):
        if self.username in data:
            plan_data = data[self.username]
            print(f"\nUser: {self.username}")
            print(f"Plan: {plan_data[0]}")
            print(f"Duration: {plan_data[1]} Bulan")
            print(f"\n{plan_data[0]} PacFlix Benefit List")
            
            if plan_data[0] == "Basic Plan":
                table = [
                    [True, "Bisa Stream"],
                    [True, "Kualitas SD"],
                    [False, "Kualitas HD"],
                    [False, "Kualitas UHD"],
                    [1, "Number of Devices"],
                    ["3rd party movie only", "Jenis Konten"],
                    ["120,000", "Harga"]
                ]
                headers = ["Basic Plan", "Services"]
                
            elif plan_data[0] == "Standard Plan":
                table = [
                    [True, "Bisa Stream"],
                    [True, "Kualitas SD"],
                    [True, "Kualitas HD"],
                    [False, "Kualitas UHD"],
                    [2, "Number of Devices"],
                    ["Basic Plan + Sport (F1, Football, Basketball)", "Jenis Konten"],
                    ["160,000", "Harga"]
                ]
                headers = ["Standard Plan", "Services"]
                
            elif plan_data[0] == "Premium Plan":
                table = [
                    [True, "Bisa Stream"],
                    [True, "Kualitas SD"],
                    [True, "Kualitas HD"],
                    [True, "Kualitas UHD"],
                    [4, "Number of Devices"],
                    ["Basic Plan + Standard Plan + Pacflix Original Series or Movie", "Jenis Konten"],
                    ["200,000", "Harga"]
                ]
                headers = ["Premium Plan", "Services"]
                
            else:
                print("Plan doesn't exist")
                return
            
            print(tabulate(table, headers, tablefmt="grid"))
        else:
            print("User not found")

    def upgrade_plan(self, new_plan):  # Hapus parameter current_plan karena tidak diperlukan
        if new_plan != self.current_plan:
            if self.duration_plan > 12:
                if new_plan == "Basic Plan":
                    total = 120_000 - (120_000 * 0.05)
                elif new_plan == "Standard Plan":
                    total = 160_000 - (160_000 * 0.05)
                elif new_plan == "Premium Plan":
                    total = 200_000 - (200_000 * 0.05)
                else:
                    raise Exception("Plan tidak ada di List !!")
            else:
                if new_plan == "Basic Plan":
                    total = 120_000
                elif new_plan == "Standard Plan":
                    total = 160_000
                elif new_plan == "Premium Plan":
                    total = 200_000
        
            # Tambahkan output untuk menampilkan hasil
            print(f"\nUpgrade plan untuk {self.username}:")
            print(f"Dari: {self.current_plan}")
            print(f"Ke: {new_plan}")
            print(f"Durasi langganan: {self.duration_plan} bulan")
            print(f"Harga setelah {'diskon 5% ' if self.duration_plan > 12 else ''}Rp {total:,.0f}")
        
            return total
        else:
            print("Anda sudah berlangganan plan ini")
            return None

# Correct way to create and use the User instance
user1 = User("Ana", 5, "Premium Plan")
user1.check_plan()

user2 = User("Cahya", 24 , "Standard Plan")

user2.upgrade_plan("Premium Plan")
