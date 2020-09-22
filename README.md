# SC2_bot_chat
Chat add on for bots playing SC2

This add on is made to reply to chat messages that bot sees on ladder games.
It saves every chat message from enemy bot.
Messages will be saved in data/messages.dat file
Picle is used to prevent users from corrupting data file.

        DO NOT INSULT ANYONE WITH YOUR CHAT MESSAGES!!!
        Humans have feelings but bots don't.
        At least for now.


Installation and usage:

STEP 1:
Copy all files in your bot root directory.

STEP 2:
Add following lines to your bot:

from chat_messages import ChatData as chatdata

__init__
    self._chat_data = chatdata()

on_step
    response = self._chat_data.find_response(opponent_chat_data=self.state.chat, my_id_from_proto = self.player_id)
    if response:
        await self._client.chat_send(response, team_only=False)

STEP 3:
Upload yor bot to ladder and let it run few days

STEP 4:
Download data directory from ladder and save it on your bots local data directory.

STEP 5:
Run chat.bat file and follow instructions

STEP 6:
ZIP your all your data directory content!

STEP 7:
Upload your zip file on ladder and enjoy "intelectual" bot conversations.

Repeat steps 4 to 7 when you want add new responses.

Smileware :D
