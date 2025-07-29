from groq import Groq 
from tools import *
import streamlit as st
import json

def run_Agent(topic):
    tools=[{
            "type": "function",
            "function": {
                "name": "searcher",
                "description": "Get the URLs,titles for a given search query",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "search_query": {
                            "type": "string",
                            "description": "The query which is to be searched",
                        }
                    },
                    "required": ["search_query"],
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "scraper",
                "description": "Get the scraped content for a given URL",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "url": {
                            "type": "string",
                            "description": "The URL which is to be scraped",
                        }
                    },
                    "required": ["url"],
                },
            },
        }
    ]
    messages = [  
        {"role": "system", "content": "You are a helpful research assistant. Use the provided tools to search for information and scrape content(this is mandatory)."},  
        {"role": "user", "content": f"write a short report based on the scraped content only on the topic :{topic}  You MUST: 1) Search for {topic} , 2) Actually scrape the content from the URL you find (this is mandatory), 3) Base your report only on the scraped content, 4) If scraping fails, clearly state that you couldn't access the content"},  
    ]
    available_functions = {
        "searcher": searcher,
        "scraper":scraper
    }


    client = Groq(api_key="NA")  

    response = client.chat.completions.create(
        model="llama3-8b-8192", messages=messages, tools=tools, tool_choice="required",  temperature=0.0
    )
    print(f"response 1st:{response}")


    response_message = response.choices[0].message

    tool_calls = response_message.tool_calls

    messages.append(response_message)

    for tool_call in tool_calls:
        function_name = tool_call.function.name
        function_to_call = available_functions[function_name]
        function_args = json.loads(tool_call.function.arguments)
        function_response = function_to_call(**function_args)
        messages.append(
                {
                    "role": "tool",
                    "content": str(function_response),
                    "tool_call_id": tool_call.id,
                }
            )
    final_response = client.chat.completions.create(
        model="llama3-8b-8192", messages=messages,temperature=0.0
    )
    return final_response.choices[0].message.content

st.title("Researcher Agent")
query = st.text_input("Ask anything:")
if st.button("Search"):
    with st.spinner("Thinking…"):
        st.write(run_Agent(query))

