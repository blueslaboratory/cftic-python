# Day 29 - 07/07/2023
# pip install openai
# https://liveconnect.chat/es/obtener-api-key-openai-chatgpt

import openai

while True:

    prompts = input("\n Introduce una pregunta: ")

    # pon tu token de chatgpt aqui
    openai.api_key = "Clave chatgpt"

    if prompts == "exit":
        break
    completion = openai.Completion.create(engine="text-davinci-003", prompt=prompts, max_tokens=2048)

    print(completion.choices[0].text)

