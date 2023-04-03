import openai
import os

os.system("clear")

print("""

   ________          __  __________  ______
  / ____/ /_  ____ _/ /_/ ____/ __ \\/_  __/
 / /   / __ \\/ __ `/ __/ / __/ /_/ / / /   
/ /___/ / / / /_/ / /_/ /_/ / ____/ / /    
\\____/_/ /_/\\__,_/\\__/\\____/_/     /_/     """)

with open("api_key.txt", "r") as f:
    api_key = f.read().strip()

openai.api_key = api_key

#openai.api_key = input("Введите ваш API-ключ OpenAI: ")

while(True):
    
    chat = input("Введите вопрос ChatGPT: ")

    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": chat }])
    print(completion.choices[0].message.content)

