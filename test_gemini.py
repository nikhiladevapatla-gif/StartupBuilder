
from dotenv import load_dotenv
from google import genai

print("Starting Gemini test...", flush=True)

load_dotenv()

try:
    client = genai.Client()

    print("Connecting to Gemini...", flush=True)

    response = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents="Explain what a startup is in three simple sentences."
    )

    print("\nGemini Response:")
    print(response.text)

    print("\nSUCCESS! Gemini is connected.")

except Exception as e:
    print("\nERROR:")
    print(type(e).__name__)
    print(e)
