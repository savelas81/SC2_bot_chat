import pickle

'''
This is made to reply to chat messages that bot sees on ladder games.
It saves every chat message from enemy.
Messages will be saved in data/messages.dat file
To add replies for saved messages run 'add_responses.py'
Type in single dot (.) for not to reply this message anything.
picle is used to prevent users from corrupting data file.
Bot replies after amount of iteration in self.chat_delay since enemy LAST chat message.

you need to add following lines to your bot and data folder:

from chat_messages import ChatData as chatdata

__init__
    self._chat_data = chatdata()

on_step
    response = self._chat_data.find_response(opponent_chat_data=self.state.chat, my_id_from_proto = self.player_id)
    if response:
        await self._client.chat_send(response, team_only=False)

'''


class ChatData:

    def __init__(self):
        self.chat_delay = 60
        self.chat_messages = {}
        self.loadData()
        self.response = None
        self.chat_timer = 0
        self.no_response = "No programmed response."

    def save_responses(self):
        messages_to_be_deleted = []
        print("Welcome to chat addon!")
        print("DO NOT INSULT ANYONE WITH YOUR CHAT MESSAGES!!!")
        print("Humans have feelings but bots don't.")
        print("At least for now.")
        print("")
        print("Type new message if you want to modify response.")
        print("Type . if you want to clear response.")
        print("Press enter to skip current message. No changes will be made.")
        print("Message format: enemy message * your response *")
        print("")
        for opponent_chat in self.chat_messages.keys():
            print(opponent_chat, "*", self.chat_messages[opponent_chat], "*")
            response = str(input())
            if response:
                if response == ".":
                    response = self.no_response
                print("")
                self.chat_messages.update({opponent_chat: response})
        self.saveData()

    def saveData(self):
        try:
            with open("data/messages.dat", "wb") as file:
                pickle.dump(self.chat_messages, file)
        except (OSError, IOError) as e:
            print(str(e))

    def loadData(self):
        try:
            with open("data/messages.dat", "rb") as file:
                self.chat_messages = pickle.load(file)
                # print("Chat messages:", self.chat_messages)
        except (OSError, IOError) as e:
            print("No chat data found.")
            print(e)

    def find_response(self, opponent_chat_data, my_id_from_proto):
        use_frame = True
        if opponent_chat_data:
            print(opponent_chat_data)
            id_from_chat = opponent_chat_data[0].player_id
            if my_id_from_proto == id_from_chat:
                use_frame = False
                print("My chat message.")
            else:
                print("Enemy chat message.")

        if not use_frame:
            return None

        if not opponent_chat_data:
            if self.response:
                self.chat_timer -= 1
                if self.chat_timer < 0:
                    response = self.response
                    self.response = None
                    return response
                else:
                    return None
            return None
        else:
            opponent_chat = opponent_chat_data[0].message
            if not self.chat_messages.get(opponent_chat):
                self.chat_messages.update({opponent_chat: self.no_response})
                self.saveData()
                return None
            else:
                response = self.chat_messages.get(opponent_chat)
                if response == self.no_response:
                    return None
                else:
                    self.response = response
                    self.chat_timer = self.chat_delay
                    return None
            print("response return error.")
            return None

    # def remove_empty_responses(self):
    #     for message in self.chat_messages.keys():
    #         if self.chat_messages[message] == self.no_response:
    #             self.chat_messages.pop(message)
    #     self.saveData()