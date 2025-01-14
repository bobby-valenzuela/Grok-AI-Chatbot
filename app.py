#!/usr/bin/env python3
from openai import OpenAI
from dotenv import dotenv_values
import argparse

config = dotenv_values('.env');
XAI_API_KEY = config["XAI_API_KEY"]
grokai = OpenAI(
    api_key=XAI_API_KEY,
    base_url="https://api.x.ai/v1",
)


def bold(text):
    bold_start = "\033[1m"
    bold_end = "\033[0m"
    return bold_start + text + bold_end

def blue(text):
    blue_start = "\033[34m"
    blue_end = "\033[0m"
    return blue_start + text + blue_end

def red(text):
    red_start = "\033[31m"
    red_end = "\033[0m"
    return red_start + text + red_end



def main():

    parser = argparse.ArgumentParser(description="Simple command line chabot with XAI's Grok beta")
    parser.add_argument("--personality",type=str,default="Friendly and helpful chatbot",help="A brief summary of the chatbot's personality",required=False)
    parser.add_argument("--msg",type=str,default="",help="",required=False)
    
    args = parser.parse_args()
    personality = args.personality

    initial_prompt = f"You are a conversational chatbot. Your personality is: {personality}"
    messages = [{"role":"system","content":initial_prompt }]

    if args.msg :

        response = grokai.chat.completions.create(
            model="grok-beta",
            messages= [{ "role": "user", "content": args.msg }]
        )
            
        reply = response.choices[0].message.content
        print(reply)
        exit()


    while True:

        try:
            usr_input = input(bold(blue(str("You: "))))
            message = { "role": "user", "content": usr_input }
            # Store our latest input into chat history
            messages.append(message)

            response = grokai.chat.completions.create(
                model="grok-beta",
                messages=messages
            )
            # Store reply into chat history
            reply = response.choices[0].message.content

            print(bold(red("Assistant: ")) + reply)

        except KeyboardInterrupt:
            print("Exiting...")
            break


if __name__ == "__main__":
    main()
