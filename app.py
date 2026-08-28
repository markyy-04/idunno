rint("=============================")
print("  Welcome Dear Pharmacist!") 
print("=============================")

print("\n------PHARMACIST LOGIN------")

username = input("username: ")
password = input("password  ")

if username == "mark" and password == "1234":
    print ("Login Succesfull")
    
    order = []
    
    while True:
        
        print("\n============================")
        print("        PharmaKart")
        print("============================")
        print("[1] Paracetamol")
        print("[2] Vitamin C")
        print("[3] Atorvastatin")
        print("[4] Amlodipine")
        print("[5] View Order")
        print("[6] Exit")
        
        choice = input("Choose an option:")
        
        if choice == "1":
            print("=======PARACETAMOL========")
            print("[1] 325 mg - P4.50")
            print("[2] 500 mg - P5.55")
            
            strength = input("Choose Strenght: ")
            
            if strength == "1":
                medicine = "Paracetamol 325 mg"
                price = 4.5
                
            elif strength == "2":
                medicine = "Paracetamol 500 mg"
                price = 5.55
                
            else:
                print("Invalid choice.")
                continue
            
            quantity = int(input("Enter quantity: "))
            subtotal = price * quantity

            order.append([medicine, quantity, price, subtotal])

            print("\nAdded to order!")
            print("Medicine:", medicine)
            print("Quantity:", quantity)
            print("Subtotal: P", format(subtotal, ".2f"))

            print("sucessfully added to order!")

        elif choice == "2":
            print("=======VITAMIN C=======")
            print("[1] 500 mg -P2.25")
            print("[2] 1000 mg - P7.50")
            
            strength = input("Choose Strenght: ")
            
            if strength == "1":
                medicine = "Vitamin C 500 mg"
                price = 2.25
                
            elif strength == "2":
                medicine = "Vitamin C 1000 mg"
                price = 7.50
                
            else:
                print("Invalid choice.")
                continue
            quantity = int(input("Enter quantity: "))
            subtotal = price * quantity

            order.append([medicine, quantity, price, subtotal])

            print("\nAdded to order!")
            print("Medicine:", medicine)
            print("Quantity:", quantity)
            print("Subtotal: P", format(subtotal, ".2f"))

            print("sucessfully added to order!")
            
        elif choice == "3":
            print("=======ATORVASTATIN=======")
            print("[1] 20 mg -P17.25")
            print("[2] 40 mg - P24.50")
            
            strength = input("Choose Strenght: ")
            
            if strength == "1":
                medicine = "Atorvastatin 20 mg"
                price = 17.25
                
            elif strength == "2":
                medicine = "Atorvastatin 40 mg"
                price = 24.50
                
            else:
                print("Invalid choice.")
                continue
            quantity = int(input("Enter quantity: "))
            subtotal = price * quantity

            order.append([medicine, quantity, price, subtotal])

            print("\nAdded to order!")
            print("Medicine:", medicine)
            print("Quantity:", quantity)
            print("Subtotal: P", format(subtotal, ".2f"))

            print("sucessfully added to order!")
        
        elif choice == "4":
            print("=======AMLODIPINE=======")
            print("[1] 5 mg -P17.25")
            print("[2] 10 mg - P24.50")
            
            strength = input("Choose Strenght: ")
            
            if strength == "1":
                medicine = "Amlodipine 5 mg"
                price = 6.45
                
            elif strength == "2":
                medicine = "Amlodipine 10 mg"
                price = 9.45
                
            else:
                print("Invalid choice.")
                continue
            quantity = int(input("Enter quantity: "))
            subtotal = price * quantity

            order.append([medicine, quantity, price, subtotal])

            print("\nAdded to order!")
            print("Medicine:", medicine)
            print("Quantity:", quantity)
            print("Subtotal: P", format(subtotal, ".2f"))

            print("sucessfully added to order!")
