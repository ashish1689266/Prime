# create a chat system using OOPs concepts
# user
# message
# chatroom
# and we have to implement functions
# sending messages
# viewing chat history
# user joining and leaving the chatroom

class chatroom:
    def __init__(self):
        self.enter = False

    def entry(self):
        self.enter = True

    def out_of_chatroom(self):
        self.enter = False

class message:
    def __init__(self):
        self.message_dictionary = {}

    def send_message(self, reciever_no):
        if self.message_dictionary.get(reciever_no) == None:
            print("New contact")
            self.message_dictionary.update({
                reciever_no: []
            })
            print("Keep entering new messages, enter exit to quit messaging")
            while True:
                text = input("Enter your text: ")
                if text.lower() == "exit":
                    print("You are going out of the text sending zone.")
                    break
                self.message_dictionary[reciever_no].append(text)
        else:
            print("Keep entering new messages, enter exit to quit messaging")
            while True:
                text = input("Enter your text: ")
                if text.lower() == "exit":
                    print("You are going out of the text sending zone.")
                    break
                self.message_dictionary[reciever_no].append(text)

    def message_history(self, reciever_no):
        if self.message_dictionary.get(reciever_no) != None:
            list1 = self.message_dictionary[reciever_no]
            text_no = 1
            for text in list1:
                print(f"{text_no}: {text}")
                text_no += 1 
                

class user(chatroom, message):
    def __init__(self, name, phone, id):
        self.name = name
        self.phone = phone
        self.id = id
        super().__init__()
        message.__init__(self)

    def __del__(self):
        print("User deleted completely.")

    

# So now we will start the chat system
user_dictionary = {}
user_name = ()
user_index = 0
while True:
    
    will = input("Do you want to register, Yes or No?: enter 'exit' to quit: ")
    
    if will == "Yes":
        name = input("Enter your name: ")
        phone = input("Enter your mobine no. ")
        user_name = user_name + (name,)
        user_dictionary.update({
            name : user(name, phone, user_index)
        })
        user_index = user_index + 1

        enter_chatroom = input("Do you wish to enter chatroom? Yes/ No: ")
        if enter_chatroom == "Yes":
            user_dictionary[name].entry()

            while True:
                print("A. send message")
                print("B. message history")
                print("C. get out of chatroom")

                choice = input("Enter your choice: ")
                match choice:
                    case 'A':
                        reciever_no = input("Enter reciever no. ")
                        user_dictionary[name].send_message(reciever_no)
                    case 'B':
                        reciever_no = input("Enter reciever no. ")
                        user_dictionary[name].message_history(reciever_no)
                    case 'C':
                        print("Going out of chatroom")
                        user_dictionary[name].out_of_chatroom()
                        break
                    case _:
                        print("Invalid Input, please select a proper choice.")

    elif will == "No":
        print("A. Want to continue as old user.")
        print("B. Delete your account")
        choice = input("Enter your choice: ")
        match choice:
            case 'A':
                name = input("Enter your name: ")
                enter_chatroom = input("Do you wish to enter chatroom? Yes/ No: ")
                if enter_chatroom == "Yes" and user_dictionary.get(name) != None:
                    user_dictionary[name].entry()
                
                    while True:
                        print("A. send message")
                        print("B. message history")
                        print("C. get out of chatroom")
                
                        choice = input("Enter your choice: ")
                        match choice:
                            case 'A':
                                reciever_no = input("Enter reciever no. ")
                                user_dictionary[name].send_message(reciever_no)
                            case 'B':
                                reciever_no = input("Enter reciever no. ")
                                user_dictionary[name].message_history(reciever_no)
                            case 'C':
                                print("Going out of chatroom")
                                user_dictionary[name].out_of_chatroom()
                                break
                            case _:
                                print("Invalid Input, please select a proper choice.")
                else:
                    print("This user does not exist. enter a valid name")
            case 'B':
                name = input("Enter your name: ")
                if user_dictionary.get(name) != None:
                    print("Deleting your account hence deleting object completely")
                    del user_dictionary[name]
                else:
                    print("The user does not exist")
    elif will == 'exit':
        print("Exiting the program")
        exit()
    else:
        print("Invalid input.")
    

    
