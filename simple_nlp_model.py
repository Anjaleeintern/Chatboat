import json
import random

# Load JSON data from the file
with open("college_intents.json", "r") as file:
    intents = json.load(file)["intents"]

def get_response(user_input):
    user_input = user_input.lower()
    
    # Iterate through each intent and check if user input matches any pattern
    for intent in intents:
        for pattern in intent["patterns"]:
            if pattern.lower() in user_input:
                # Return a random response from the matched intent
                return random.choice(intent["responses"])
    
    # Default response if no match is found
    return "I'm not sure I understand. Could you please rephrase?"


