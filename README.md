# SC2_bot_chat
Chat add on for bots playing SC2

This add on is made to reply to chat messages that bot sees on ladder games.
It saves every chat message from enemy.
Messages will be saved in data/messages.json file
To add replies for saved messages replace ----- with your reply
Bot replies after amount of iterations in self.chat_delay (chat_messages.py) since enemy LAST chat message.

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
Download data directory from ladder.

STEP 5:
replace ----- with your replies.
	(----- = no response)

STEP 6:
ZIP all data directory content!

STEP 7:
Upload your zip file on ladder and enjoy "intelectual" bot conversations.

Repeat steps 4 to 7 when you want add new responses.

Smileware :D

Use at your own risk.
I'm not taking any responsibility for damaged software, hardware or feelings.
