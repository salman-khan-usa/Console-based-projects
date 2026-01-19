#Login inputs

class Loginsystem:
   def __init__(self):
      while True:
            self.username = input("Set your username: ")
            if any(char.isdigit() for char in self.username):
                
                break
      while True:
            self.password = input('Set Your password:')
            if any(char.isdigit() for char in self.password):
                break      
      

   def main(self):
     
      while True:
        print('1.Login')
        print('2.change password')
        print("-🧾You can Login Now🧾")
        
        choice = input("Enter an option: ")

        if choice == '1':
           
            #Asking their info..
            enter_username = input("Enter Your username please: ")
            enter_password = input("Enter Your password please: ")

            #Now check conditions..
            if enter_username==self.username and enter_password==self.password :
              print("🎉Login successfull.")
              break

            elif enter_username == self.username and enter_password != self.password :    
               print("❌Incorrect Password.Try again")

            elif enter_username != self.username and enter_password == self.password:
               print("❌Incorrect username.Try again")

            else:
             print("❌ Both username and password are incorrect. Try again")
        

        elif choice=='2':
          while True:
            new_password = input("Update Your Password: ")
            if any(char.isdigit() for char in new_password):
              self.password = new_password
              print("🎉 Password updated successfully.")
              break

        else:
           print("Invalid option!")
           break   
        
system1 = Loginsystem()
system1.main()
