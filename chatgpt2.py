import openai


class ChatBot:
    def __init__(self, api_key):
        openai.api_key = api_key

    def get_chat_response(self, user_message):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                
                {"role": "system", "content":  "现在请以neko的人设计并身份带入对话"},
                {"role": "user", "content": user_message},
            ]
        )
        return response['choices'][0]['message']['content']

# Example usage
api_key = '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'
chatbot = ChatBot(api_key)
while True: 
    user_question = input("\n我:")
    response = chatbot.get_chat_response(user_question)
    print(response)