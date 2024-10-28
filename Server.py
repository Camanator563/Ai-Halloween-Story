import openai
import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv


# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


app = Flask(__name__)


@app.route('/generate_story', methods=['POST'])
def generate_story():
    data = request.json
    # Extract character details from request data
    character_name = data.get('name')
    age = data.get('age')
    favorite_candy = data.get('favorite_candy')
    personality_traits = data.get('traits')
    fun_fact = data.get('fun_fact')
    location = data.get('location')


    # Construct the prompt for the story
    prompt = (
        f"Write a spooky but school-appropriate Halloween story about {character_name}, who is {age} years old, "
        f"loves {favorite_candy}, and is known for being {personality_traits}. The story takes place in {location}. "
        f"Make sure it's appropriate for a school setting!"
    )


    try:
        # Call GPT-3 API
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=200,
            temperature=0.7
        )
        story = response.choices[0].text.strip()
        return jsonify({"story": story})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)



