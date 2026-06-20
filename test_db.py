import os
from supabase import create_client, Client
from dotenv import load_dotenv

# Load your keys from .env
load_dotenv()

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")

print("Attempting connection to Supabase...")

try:
    if not url or not key:
        raise ValueError("Credentials are empty! Check your .env file details.")

    supabase: Client = create_client(url, key)
    
    dummy_data = {
        "student_name": "Renuka Mewada",
        "question": "Testing database setup",
        "student_answer": "This is a direct insert test from Cursor terminal.",
        "score": 10,
        "ai_feedback": "Database link is fully functioning!"
    }
    
    response = supabase.table("evaluations").insert(dummy_data).execute()
    print("Success! Data inserted smoothly into your cloud table.")
    print("Inserted Data ID:", response.data[0]['id'] if response.data else "No data returned")

except Exception as e:
    print(" Connection Failed! Error message:", str(e))