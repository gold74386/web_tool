from zhipuai import ZhipuAI

class ChatBot:
    def __init__(self, api_key):
        self.client = ZhipuAI(api_key=api_key)

    def chat(self, user_input):
        response = self.client.chat.completions.create(
            model="glm-4",
            messages=[
                {"role": "user", "content": user_input},
                {"role": "assistant", "content": "我是人工智能助手"},
            ],
        )
        
        return ("机器人：" + response.choices[0].message.content)

# 使用示例
if __name__ == "__main__":
    api_key = "eb96b3d8daba32c54cbffe8e350096ba.Ot4TZHhR33zfdBMR"  # 请填写您自己的APIKey
    bot = ChatBot(api_key)
    while True:
       user_input = input("您：")
       print(bot.chat(user_input))