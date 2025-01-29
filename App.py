import tkinter as tk
import openai
import pyttsx3


# Replace 'YOUR_OPENAI_API_KEY' with your actual OpenAI API key.
openai.api_key = 'Insert your Api Key Here'


# Initialize the TTS engine
engine = pyttsx3.init()


# Customize TTS settings
# Change speech rate (default is usually around 200)
engine.setProperty('rate', 150)


# Change voice (0 = male, 1 = female)
voices = engine.getProperty('voices')
if len(voices) > 1:  # Check if there are multiple voices available
    engine.setProperty('voice', voices[1].id)  # Use female voice, if available
else:
    print("Female voice not available; using default voice.")


def submit_character():
    # Collect input from the form
    character_name = name_entry.get()
    age = age_entry.get()
    favorite_candy = candy_entry.get()
    personality_traits = traits_entry.get()
    fun_fact = fun_fact_entry.get("1.0", tk.END).strip()
    location = location_entry.get()


    # Construct the messages for the Chat API
    messages = [
        {"role": "user", "content": (
            f"Write a spooky but school-appropriate Halloween story about {character_name}, who is {age} years old, "
            f"loves {favorite_candy}, and is known for being {personality_traits}. The story takes place in {location}. "
            f"Make sure it's appropriate for a school setting!"
        )}
    ]



    try:
        # Use the gpt-3.5-turbo model
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Switching to the Chat API model
            messages=messages,
            max_tokens=200,
            temperature=0.7
        )
        story = response['choices'][0]['message']['content'].strip()


        # Display the story in the result text area
        result_text.config(state=tk.NORMAL)
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, story)
        result_text.config(state=tk.DISABLED)


        # Speak the story
        engine.say(story)
        engine.runAndWait()


    except Exception as e:
        result_text.config(state=tk.NORMAL)
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"Error: {e}")
        result_text.config(state=tk.DISABLED)


# Set up tkinter window
root = tk.Tk()
root.title("Halloween Story Generator")


# Input fields for character details
tk.Label(root, text="Name").grid(row=0, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)


tk.Label(root, text="Age").grid(row=1, column=0)
age_entry = tk.Entry(root)
age_entry.grid(row=1, column=1)


tk.Label(root, text="Favorite Candy").grid(row=2, column=0)
candy_entry = tk.Entry(root)
candy_entry.grid(row=2, column=1)


tk.Label(root, text="Personality Traits").grid(row=3, column=0)
traits_entry = tk.Entry(root)
traits_entry.grid(row=3, column=1)


tk.Label(root, text="Fun Fact").grid(row=4, column=0)
fun_fact_entry = tk.Text(root, height=2, width=30)
fun_fact_entry.grid(row=4, column=1)


tk.Label(root, text="Location").grid(row=5, column=0)
location_entry = tk.Entry(root)
location_entry.grid(row=5, column=1)


# Submit button
submit_button = tk.Button(root, text="Generate Story", command=submit_character)
submit_button.grid(row=6, column=1)


# Result area
tk.Label(root, text="Generated Story").grid(row=7, column=0)
result_text = tk.Text(root, height=10, width=50, state=tk.DISABLED)
result_text.grid(row=8, column=0, columnspan=2)


root.mainloop()





