from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

llm = ChatGoogleGenerativeAI(
    model = "gemini-2.5-flash",
    temperature = 0.8
    )

mode = input("Choose AI mode (e.g., happy, sad, strict, funny): ").lower().strip()

messages = [SystemMessage(content = f"""
                          You are a mood-based AI assistant.
                          Your current mode is: {mode}
                          You must strictly adapt your tone, style, and personality to this mode in every response.
                          """)]

print("\n----- Welcome to MoodBot -----")
print("Type '0' to exit\n")

while True :
    prompt = input("You : ")
    if prompt == "0" :
        break
    messages.append(HumanMessage(content = prompt))
    response = llm.invoke(messages)
    messages.append(AIMessage(content = response.content))
    print("Bot : ",response.content)


