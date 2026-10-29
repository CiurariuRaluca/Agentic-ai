import sys
from openai import OpenAI

def main():
    client=OpenAI(base_url="http://localhost:11434/v1",api_key="ollama")

    history=[{"role":"system", "content": "You a Windows Powershell expert. Make sure to provide commands that work on Windows 10/11 . Be concise!"}]

    print("Terminal chat started: to exit type 'exit' or 'quit' to end the chat")

    while True:
        user_input=input("user: ")

        if user_input.lower() in ['exit','quit']:
            print("exiting...")
            break
        if not user_input.strip():
            continue

        history.append({"role":"user","content": user_input})

        try:
            response=client.chat.completions.create(
                model="qwen2.5:1.5b",
                temperature=0.2,
                messages=history
            )
            agent_reply=response.choices[0].message.content
            print (f"agent:{agent_reply}")
            history.append({"role": "assistant", "content":agent_reply})

        except Exception as e :
            print(f"Error: {e}")
            history.pop()

if __name__=="__main__":
    main()