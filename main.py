from openai import OpenAI

key = "api_key"

messages = []

client = OpenAI(
    api_key=key,  # This is the default and can be omitted
)

def completion(message):
    global messages
    messages.append(
        {
            "role": "user",
            "content": message
        }
    )

    chat_completion = client.chat.completions.create( messages=messages,
                        model="gpt-4o"
                        )
    
    # print(chat_completion)
    message = {
        "role": "assistant",
        "content": chat_completion.choices[0].message.content
    }
    messages.append(message)
    print(f"Jarvis: {message['content']}")

if __name__ == "__main__":
    print(f"Jarvis: Hi I am Jarvis, How may I help you\n")
    while True:
        user_question = input()
        print(f"User: {user_question}")

        completion(user_question)
