from dotenv import load_dotenv
import os
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationEntityMemory
from langchain.memory.prompt import ENTITY_MEMORY_CONVERSATION_TEMPLATE
from colorama import Fore, Style

def main():
    load_dotenv()

    # test our api key
    if os.getenv("OPENAI_API_KEY") is None or os.getenv("OPENAI_API_KEY") == "":
        print("OPENAI_API_KEY is not set. Please add your key to .env")
        exit(1)

    llm = ChatOpenAI()
    conversation = ConversationChain(
        llm=llm,
        memory=ConversationEntityMemory(llm=llm),
        prompt=ENTITY_MEMORY_CONVERSATION_TEMPLATE,
        verbose=False
    )

    print("Ahooy! Ja som Rejibo a rád ti pomôžem!")

    while True:
        user_input = input("> ")

        ai_response = conversation.predict(input=user_input)

        print("\nAssistant:")
        print("=" * 30)
        print(f"{Fore.GREEN}{ai_response}{Style.RESET_ALL}")
        print("=" * 30)


if __name__ == '__main__':
    main()