import os
from dotenv import load_dotenv
import google.generativeai as genai
import json
import time
import uuid
from utils import topics, extract_json


load_dotenv()

gemini_key = os.getenv('GEMINI_KEY')

genai.configure(api_key=gemini_key)
model = genai.GenerativeModel('gemma-3-27b-it')





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
    - Let the correct option be very random. Have no bias for a correct answer
    - Let each question be a popular question any adult could answer
    - Medium difficulty with the questions
    - No INCORRECT answer
    ---
    ### **✅ Example Output**  
    ```
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


    ### Bad example - DO NOT GENERATE THESE

        {{
            "question": "Who is the best Nigerian rapper in 2010?",
            "options": ["Olamide", "Dagrin", "Phyno", "Infinity"],
            "reason": "No well-defined metric for this question"
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

    if question_data and isinstance(question_data, dict):  # Ensure it's a dict before updating
        question_data.update({
            "id": str(uuid.uuid4()),
            "category": category,
            "sub_category": sub_category,
            "created_at": time.strftime("%Y-%m-%dT%H:%M:%SZ")
        })
        return question_data
    else:
        print(f"Invalid question format: {question_data}")
        return None
    





questions = []
for topic in topics:
    try:
        print(f"Generating questions for topic {topic['category']}")
        question = generate_question(topic["category"], topic["sub_category"])
        print(question)
        if question:
            questions.append(question)
    except Exception as e:
        print(f"Error generating question for {topic['category']} - {topic['sub_category']}: {e}")
    

# Save to JSON file
with open("nigerian_trivia_questions.json", "w") as f:
    json.dump(questions, f, indent=4)

print("Question generation complete! Data saved to nigerian_trivia_questions.json")




