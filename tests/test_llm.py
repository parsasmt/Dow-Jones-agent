# from llm.llm import llm
# from llm.output_parser import get_content

# messages = [
#     {
#         "role": "user",
#         "content": "What is the Dow Jones?"
#     }
# ]

# response = llm.chat(messages)

# print(get_content(response))

from config import config

print(config.OPENROUTER_API_KEY)
print(config.MODEL_NAME)
print(config.OPENROUTER_BASE_URL)