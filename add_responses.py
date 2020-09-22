from chat_messages import ChatData as chatdata

def main():
    chat_data = chatdata()
    chat_data.save_responses()

if __name__ == '__main__':
    main()
