
class User:
    def __init__(self):
        self.username = ""
        self.email = ""
        self.password = ""
        self.score = 0
        self.userCredentials = []

    def newUser(self):
        print("🎉Hello there, Adventurer welcome to the HIGHER LOWER GAME.🎉")
        print("Please enter your details to record you score.And see yourself on the leaderboard.")

        self.username = input("Please enter your username('It will appear on the Leaderboard :)'):\n")
        self.email = input("Please enter your email:\n")

        while True:
            new_pass = input("Enter new password:\n")
            confirm_pass = input("Re-enter new password: \n")
            if new_pass == confirm_pass:
                self.password = new_pass
                break
            else:
                print("Passwords didn’t match. Try again.")
        print("Please log in to your account.")
        


    def userDB(self):
        newUser = {self.username : {"email": self.email, "password":self.password ,"score":self.score}}
        self.userCredentials.append(newUser)
        self.existingUser(self.username, self.password)

    def existingUser(self, username, password):
        
        user = input("Please enter your username('It will appear on the Leaderboard :)'):\n")
        credentials = input("Enter new password:\n")
        
        for items in self.userCredentials:
            
            if user == items[username] and credentials == items[username]["password"]:
                print(f"Welcome back, {username}")
            else:
                print("Incorrect credentials")