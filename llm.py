import os
from google import genai
from dotenv import load_dotenv

# 1. Load variables from your .env file
load_dotenv()

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

print("Initializing Google Gemini Client...")

try:
    if not GEMINI_API_KEY:
        raise ValueError("Missing GEMINI_API_KEY inside your .env file!")

    # 2. Set up the Google GenAI Client
    client = genai.Client(api_key=GEMINI_API_KEY)
    
    print("Sending a quick test prompt to gemini-2.5-flash...")
    
    # 3. Request a simple completion
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents='Respond with exactly these words: "Gemini API is working perfectly!"',
    )
    
    print("\nSUCCESS! Your Google Gemini key is fully active.")
    print("Gemini Response:", response.text)

except Exception as e:
    print("\nConnection Failed! Something is wrong with your Gemini key setup.")
    print("Error Details:", str(e))