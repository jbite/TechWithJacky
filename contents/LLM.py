
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

Day9Title = "Day 9 - Introduce Tools"
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
Day10Title="Day 10 - multi modal AI agent"

Day10Content = """
Hello everyone, and welcome. Today, we're diving into the fascinating world of software agents – intelligent entities designed to operate independently and tackle complex tasks. Think of them as digital assistants with specific skill sets.

Let's break down what defines an agent. At its core, an agent is a software entity capable of autonomously performing tasks. This autonomy is crucial; it means they can operate without constant human intervention. They're also goal-oriented, meaning they have a specific objective they're trying to achieve. And finally, they're typically task-specific, meaning they're designed to excel at a particular type of job.   

Now, while these core characteristics are important, more sophisticated agents, especially those designed to handle complex problems, possess additional capabilities. These capabilities allow them to function within an "agent framework," a collaborative environment where multiple agents can work together. Let's explore some of these key features:   

Memory/Persistence: A good agent doesn't forget. It retains information about past interactions, learned experiences, and the current state of its task. This "memory" allows for more efficient and context-aware performance. Think of it like remembering a conversation from earlier – it allows for more natural and relevant follow-up.   
Decision-Making/Orchestration: Agents need to make choices. They need to decide which actions to take, when to take them, and how to adapt to changing circumstances. In an agent framework, this also involves "orchestration" – coordinating the activities of multiple agents to achieve a common goal. It's like a conductor leading an orchestra, ensuring each instrument plays its part at the right time.   
Planning Capabilities: Agents are often required to plan ahead. This involves anticipating future needs, setting sub-goals, and outlining a sequence of actions to achieve the overall objective. Planning gives agents a sense of direction and allows them to tackle more complex, multi-step tasks. Imagine planning a road trip – you wouldn't just start driving without a map or destination in mind.   
Use of Tools: This is where things get really interesting. Agents can leverage external tools and resources to enhance their capabilities. This could involve connecting to databases to retrieve information, accessing the internet for real-time data, or using specific software applications to perform specialized functions. This ability to use tools is what makes agents truly powerful and versatile.   
So, how are we going to put this knowledge into practice? We have three exciting activities planned:

Image Generation: We'll start by exploring the OpenAI interface to generate images. This will give us a tangible example of how AI can create visual content based on textual prompts. This is a very powerful example of an agent using a tool (the image generation model) to achieve a task.
Making Agents: We'll then create our own agents designed to generate both sound and images for a hypothetical store. This will involve designing agents with specific goals and capabilities, giving us hands-on experience in agent development.
Making an Agent Framework: Finally, we'll delve into building a simple agent framework. We'll teach our AI assistant to both "speak" (generate text) and "draw" (generate images), demonstrating how multiple agents can collaborate within a framework to achieve a more complex, multi-modal output.
By the end of this session, you'll have a solid understanding of what agents are, how they work, and how they can be used to solve real-world problems. You'll also have practical experience in creating and using agents, setting you on the path to becoming proficient in this exciting field. Remember, the key is to think about how to break down complex tasks into smaller, manageable sub-tasks that can be assigned to specialized agents working together. This is the essence of the agent framework approach. Let's begin!"""

Day10Code="""
# Some imports for handling images

import base64
from io import BytesIO
from PIL import Image

def artist(city):
    image_response = openai.images.generate(
            model="dall-e-3",
            prompt=f"An image representing a vacation in {city}, showing tourist spots and everything unique about {city}, in a vibrant pop-art style",
            size="1024x1024",
            n=1,
            response_format="b64_json",
        )
    image_base64 = image_response.data[0].b64_json
    image_data = base64.b64decode(image_base64)
    return Image.open(BytesIO(image_data))
from pydub import AudioSegment
from pydub.playback import play

def talker(message):
    response = openai.audio.speech.create(
      model="tts-1",
      voice="onyx",    # Also, try replacing onyx with alloy
      input=message
    )
    
    audio_stream = BytesIO(response.content)
    audio = AudioSegment.from_file(audio_stream, format="mp3")
    play(audio)

def chat(history):
    messages = [{"role": "system", "content": system_message}] + history
    response = openai.chat.completions.create(model=MODEL, messages=messages, tools=tools)
    image = None
    
    if response.choices[0].finish_reason=="tool_calls":
        message = response.choices[0].message
        response, city = handle_tool_call(message)
        messages.append(message)
        messages.append(response)
        image = artist(city)
        response = openai.chat.completions.create(model=MODEL, messages=messages)
        
    reply = response.choices[0].message.content
    history += [{"role":"assistant", "content":reply}]

    # Comment out or delete the next line if you'd rather skip Audio for now..
    talker(reply)
    
    return history, image
# More involved Gradio code as we're not using the preset Chat interface!
# Passing in inbrowser=True in the last line will cause a Gradio window to pop up immediately.

with gr.Blocks() as ui:
    with gr.Row():
        chatbot = gr.Chatbot(height=500, type="messages")
        image_output = gr.Image(height=500)
    with gr.Row():
        entry = gr.Textbox(label="Chat with our AI Assistant:")
    with gr.Row():
        clear = gr.Button("Clear")

    def do_entry(message, history):
        history += [{"role":"user", "content":message}]
        return "", history

    entry.submit(do_entry, inputs=[entry, chatbot], outputs=[entry, chatbot]).then(
        chat, inputs=chatbot, outputs=[chatbot, image_output]
    )
    clear.click(lambda: None, inputs=None, outputs=chatbot, queue=False)

ui.launch(inbrowser=True)

"""