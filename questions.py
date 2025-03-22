import os
from dotenv import load_dotenv
import google.generativeai as genai
import json
import time
import uuid


load_dotenv()

gemini_key = os.getenv('GEMINI_KEY')

genai.configure(api_key=gemini_key)
model = genai.GenerativeModel('gemma-3-27b-it')



topics =  [
    {"category": "Nigerian Music", "sub_category": "Fuji Music by Pasuma (2009)"},
    {"category": "Nigerian Sports", "sub_category": "Super Eagles AFCON 2013 Victory"},
    {"category": "Nigerian Movies", "sub_category": "Nollywood Blockbusters in 2010"},
    {"category": "Nigerian Sports", "sub_category": "World Cup"}
]

def generate_question(category, sub_category):

    prompt = f"""
    Generate a **multiple-choice trivia question** about **{sub_category}** in **{category}** and return the result **strictly in JSON format**.  

    ### **✅ Formatting Rules:**  
    - **question** → A clear, objective, and fact-based trivia question.  
    - **options** → Four **unique** answer choices.  
    - **answer** → The **correct option's index mapped to a letter (A, B, C, or D)**.  
    - **Ensure NO opinion-based or ambiguous questions**—all answers must be verifiable facts.  
    - **Return ONLY JSON with no extra text or explanations.**  
    - Do NOT repeat questions
    ---
    ### **✅ Example Output**  
    ```json
    {{
      "questions": [
        {{
          "question": "Who scored for Argentina against Nigeria in the 2010 FIFA World Cup?",
          "options": ["Lionel Messi", "Gabriel Heinze", "Javier Mascherano", "Gonzalo Higuaín"],
          "answer": "B"
        }},
        {{
          "question": "What year did Tuface Idibia release the hit song 'African Queen'?",
          "options": [2001, 2002, 2003, 2004],
          "answer": "D"
        }}
      ]
    }}


    ### Bad example - DO NOT GENERATE THESE

    {{
        "questions": [
        {{
            "question": "Who is the best Nigerian rapper in 2010?",
            "options": ["Olamide", "Dagrin", "Phyno", "Infinity"],
            "reason": "No well-defined metric for this question"
        }}]
    }}
        
    """

    response = model.generate_content(prompt)
    
    try:
        response_text = response.candidates[0].content.parts[0].text
    except (IndexError, AttributeError) as e:
        print(f"Error extracting response text: {e}")
        return None

    # Clean and parse JSON
    question_data = extract_json(response_text)

    if question_data:
        question_data.update({
            "id": str(uuid.uuid4()),
            "category": category,
            "sub_category": sub_category,
            "created_at": time.strftime("%Y-%m-%dT%H:%M:%SZ")
        })

    return question_data
    


def extract_json(response_text):
    try:
        json_str = response_text.strip()  # Remove leading/trailing whitespace
        if json_str.startswith("```json"):
            json_str = json_str[7:]  # Remove ```json\n
        if json_str.endswith("```"):
            json_str = json_str[:-3]  # Remove trailing ```
        return json.loads(json_str)
    except json.JSONDecodeError as e:
        print(f"JSON parsing error: {e}")
        print(f"Response text:\n{response_text}")  # Debugging output
        return None


questions = []
for topic in topics:
    print(f"Generating questions for topic {topic['category']}")
    question = generate_question(topic["category"], topic["sub_category"])
    if question:
        questions.append(question)
    

# Save to JSON file
with open("nigerian_trivia_questions.json", "w") as f:
    json.dump(questions, f, indent=4)

print("Question generation complete! Data saved to nigerian_trivia_questions.json")




