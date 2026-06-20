import os
import gradio as gr
from google import genai
from supabase import create_client, Client
from dotenv import load_dotenv

# 1. Load keys from your .env file
load_dotenv()

SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

# 2. Initialize your clients
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
ai_client = genai.Client(api_key=GEMINI_API_KEY)

# The conceptual question for students
TRICKY_QUESTION = (
    "If a modern browser can execute complex JavaScript logic perfectly fine, "
    "why can't we just run all our database queries and secret business logic directly "
    "inside the user's browser? Why do we need a separate backend server at all? What breaks?"
)

def evaluate_submission(student_name, student_answer):
    if not student_name.strip() or not student_answer.strip():
        return "Please enter both your name and your answer before submitting!"

    # System rules instructing Gemini how to grade
    system_instruction = (
        "You are a strict Senior Software Architect grading a student's system design knowledge. "
        f"The question being answered is: '{TRICKY_QUESTION}'\n\n"
        "Grade their answer out of 10 based strictly on core architectural principles:\n"
        "1. Trust Boundaries & Client-Side Security (Frontend code is completely public and untrusted)\n"
        "2. Centralized State Control and Data Integrity\n\n"
        "If they only give visual descriptions ('frontend is what you see'), give a low score (1-4).\n"
        "If they clearly identify security vulnerabilities or exposed DB credentials, give a high score (8-10).\n\n"
        "You MUST format your response exactly like this:\n"
        "SCORE: [Number]/10\n\n"
        "CRITIQUE: [Your direct architectural feedback]"
    )

    try:
        # 3. Request evaluation from Gemini
        response = ai_client.models.generate_content(
            model='gemini-2.5-flash',
            contents=f"Student Name: {student_name}\nStudent Answer: {student_answer}",
            config={'system_instruction': system_instruction, 'temperature': 0.2}
        )
        ai_verdict = response.text

        # Safely parse the numeric score for database analytics
        score = 0
        if "SCORE:" in ai_verdict:
            try:
                score_part = ai_verdict.split("SCORE:")[1].split("/")[0].strip()
                score = int(score_part)
            except:
                score = 0

        # 4. Save results into your Supabase table
        db_record = {
            "student_name": student_name,
            "question": TRICKY_QUESTION,
            "student_answer": student_answer,
            "score": score,
            "ai_feedback": ai_verdict
        }
        supabase.table("evaluations").insert(db_record).execute()

        return ai_verdict

    except Exception as e:
        return f"System Error Encountered: {str(e)}"

# 5. Build the user interface with Gradio
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 🚀 AI-Powered Architectural First-Principles Evaluator")
    gr.Markdown("### Track A: Backend Boundary & Security Validation")
    
    with gr.Row():
        name_input = gr.Textbox(label="Student Name", placeholder="Type your full name...", scale=2)
    
    gr.Markdown(f"### **Core Architectural Question:**\n> *{TRICKY_QUESTION}*")
    
    answer_input = gr.Textbox(
        label="Your System Architecture Analysis", 
        placeholder="Provide your technical reasoning around security, secrets, and trust boundaries...", 
        lines=6
    )
    
    submit_btn = gr.Button("Submit Assessment to AI Architect", variant="primary")
    
    gr.Markdown("---")
    output_display = gr.Textbox(label="Official Evaluation Verdict & Critique", lines=8, interactive=False)
    
    # Trigger logic on click
    submit_btn.click(
        fn=evaluate_submission,
        inputs=[name_input, answer_input],
        outputs=output_display
    )

if __name__ == "__main__":
    demo.launch()