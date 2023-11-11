from __future__ import annotations
from openai.api_resources import ChatCompletion
import openai
from profanity import profanity

class Turbo:
    def __init__(self):
        with open("api_key.txt", "r") as file:
            self.api_key: str = file.read().strip()

    async def r_tubo(self) -> None:
        #client = OpenAI(
        #    api_key=self.api_key,
        #)
        complete = []
        while True:

          openai.api_key = self.api_key
          user_data = input()
          if user_data.lower() == "quit":
              break
          if profanity.contains_profanity(user_data):
              user_data = profanity.censor(user_data)
          else:
            complete.append({"role":"user","content":user_data})
            completion = ChatCompletion.create(
               messages=complete,
               model="gpt-3.5-turbo",
               )
            res = completion['choices'][0]['message']['content']
            print("Chatgpt:",res.strip("\n").strip())
            complete.append({"role":"assistant","content":res.strip("\n").strip()})

    async def tubo(self) -> None:
        await self.r_tubo()

