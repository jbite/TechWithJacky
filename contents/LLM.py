
Day1Title = "Try LLM"
Day1Content = """
- Try Ollama locally
- Complete a news summarize application with open API and reuqests
"""

Day2Title = "Compare to frontier"
Day2Content = """
- What are the frontiers of LLM model
  - OpenAI
  - Gemini
  - Cohere
  - Perplexity
- What can LLM model do?
  - synthesizeing information
  - fleshing out a skeleton 
  - coding
- Compare to those models
"""

Day3Title = "Token, Context windows, API cost, and leaderboard of LLM model"
Day3Content = """
Tokens introducing
In the early days, neural networks wee trained at the character level: predict the next character in this sequence
small vocab, but expects too much from network

Then neural network were trained off words: predict the next word in this sequence
The breakthrough was to work with chunks of words, called tokens

Less commo words (and invented words) get broken into multiple tokens
In many cases, the meaning is still captured by the tokens; hand_crafted, masterers
Sometimes, like qu_ip

see how numbers are treated - this may explain why earlier GPTs struggled with math with more than 3 digits
rule-of-thumbs: in typical english writing 
- 1 token is ~4 haracters
- 1 tokens is ~0.75 words
obviously the token count is higher for 

COntext windows
Max number of tokens that the model can consider when generating the next tken

includes the original input prompt, subsequent conversation, the latest input prompt and almost all the output prompt
it governs how well the model can remember references, content and context
Particularly important for multi-shot prompting where the prompt includes examples, or for long conversations or questions on the complete works of shakespeare

API costs
chat interfaces typycally have pro plan with a monthly sybscription. Rate limited, but no per-usage charge
APIs typically have no subscription, but carge per API call.
The cost is based on the number of input tikens and the number of output tokens
"""

Day5Title = "Day5 - Application with ollama API"
Day5Content ="""
# imports
import os
import json
import requests
from typing import List
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from IPython.display import Markdown, display, update_display

MODEL_LLAMA = 'llama3.2'
# here is the question; type over this to ask something new

AI_tutor_system_prompt = "you are an AI senior tutor. you always provide a insightful and humor courses to student. you are excel in python and data science. Now you always work in machine learning area."
question = "what is AI"
AI_learner_user_prompt = f"Answer the following question: \n\{question\}"

# Get Llama 3.2 to answer
# API endpoint
url = "http://localhost:11434/api/chat"
# Request payload
payload = {
    "model": MODEL_LLAMA,
    "messages": [
        {"role": "system", "content": AI_tutor_system_prompt},
        {"role": "user", "content": question}
    ],
    "stream": False
}

response = requests.post(url, json=payload)

#output
if response.status_code == 200:
    try:
        # Parse the JSON response
        assistant_message = response.json()["message"]["content"]

        # Display Markdown
        display_handle = display(Markdown("Waiting for response..."), display_id=True)
        update_display(Markdown(assistant_message), display_id=display_handle.display_id)
    except ValueError as json_err:
        print(f"JSON Parsing Error: {json_err}")
        print(f"Response Content: {response.text}")
else:
    print(f"Error: {response.status_code}, {response.text}")
"""

Day9Title = "Introduce Tools"
Day9Content = """
Tools
allow frontier models to connect with external functions
- richer repsonses by extending knowledgeability to carry out actions within the application
enhanced capabilities , like calculations

how it works
- in a request to the llm, specify available tools
- the reply is either text or a request to run a tools
- we run the tool and call the LLM with the results

Common use cases for Tools
- Fetch data or add knowledge or context
- Take action, like booking a meeting
- Perform calculations
- Modify the UI
"""

Day9Code = """
#The Informed Airline Customer support agent
# Let's start by making a useful function

ticket_prices = {"london": "$799", "paris": "$899", "tokyo": "$1400", "berlin": "$499"}

def get_ticket_price(destination_city):
    print(f"Tool get_ticket_price called for {destination_city}")
    city = destination_city.lower()
    return ticket_prices.get(city, "Unknown")
	
# There's a particular dictionary structure that's required to describe our function:

price_function = {
    "name": "get_ticket_price",
    "description": "Get the price of a return ticket to the destination city. Call this whenever you need to know the ticket price, for example when a customer asks 'How much is a ticket to this city'",
    "parameters": {
        "type": "object",
        "properties": {
            "destination_city": {
                "type": "string",
                "description": "The city that the customer wants to travel to",
            },
        },
        "required": ["destination_city"],
        "additionalProperties": False
    }
}

# And this is included in a list of tools:

tools = [{"type": "function", "function": price_function}]

# We have to write that function handle_tool_call:

def handle_tool_call(message):
    tool_call = message.tool_calls[0]
    arguments = json.loads(tool_call.function.arguments)
    city = arguments.get('destination_city')
    price = get_ticket_price(city)
    response = {
        "role": "tool",
        "content": json.dumps({"destination_city": city,"price": price}),
        "tool_call_id": tool_call.id
    }
    return response, city

gr.ChatInterface(fn=chat, type="messages").launch()
"""