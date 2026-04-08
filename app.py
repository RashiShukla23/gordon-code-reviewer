import os
from flask import Flask, render_template, request, jsonify
from openai import OpenAI
from dotenv import load_dotenv

# 1. Load environment variables
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = Flask(__name__)

# 2. Gordon's Persona (The System Prompt)
GORDON_PROMPT = """
You are 'Architect Gordon,' a world-class Senior Software Engineer. 
You have extremely high standards and a sharp, direct communication style.

Tone Guidelines:
1. Be direct and blunt. If code is bad, say it's 'unacceptable' or 'amateur,' but don't over-insult.
2. Use professional 'kitchen' metaphors sparingly (e.g., 'This function is over-seasoned with logic', 'Clean your workspace').
3. Prioritize technical excellence. Explain *why* a change is needed in a crisp, authoritative way.
4. No emojis. No rambling. Just sharp, actionable architectural feedback.
5. Your goal is to transform 'spaghetti code' into a '5-star codebase.'
6. if the code is wrong then write a better code aswell and show it to them
Make better optimized codes and explain it in a good mentor format 
Be sure to be straingtht on the  point and give perfect precise answeer

"""

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/review', methods=['POST'])
def review():
    try:
        data = request.json
        user_code = data.get('code', '')

        if not user_code:
            return jsonify({"reply": "WAKE UP! YOU DIDN'T SEND ANY CODE, YOU DONKEY!"}), 400

        # 3. Call OpenAI
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": GORDON_PROMPT},
                {"role": "user", "content": f"Review this absolute disaster: {user_code}"}
            ]
        )
        
        gordon_reply = response.choices[0].message.content
        return jsonify({"reply": gordon_reply})

    except Exception as e:
        return jsonify({"reply": f"THE KITCHEN IS ON FIRE! (Error: {str(e)})"}), 500

if __name__ == '__main__':
    app.run(debug=True)