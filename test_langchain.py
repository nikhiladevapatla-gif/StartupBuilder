
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

print("Starting LangChain test...", flush=True)

load_dotenv()

try:
    llm = ChatGoogleGenerativeAI(
        model="gemini-3.1-flash-lite",
        max_retries=2,
        timeout=60
    )

    print("Sending request...", flush=True)

    response = llm.invoke(
        "Suggest three innovative startup ideas for college students."
    )

    print("\nGemini Response:")
    print(response.content)

    print("\nSUCCESS! LangChain is connected.")

except Exception as e:
    print("\nERROR:")
    print(type(e).__name__)
    print(e)
