import random

R_EATING = "I don't like eating anything because I'm a bot obviously!"
R_ADVICE = "If I were you, I would go to the internet and type exactly what you wrote there!"

def unknown():
    responses = [
        "Could you please rephrase that?",
        "...",
        "Sounds about right.",
        "What does that mean?"
    ]
    return random.choice(responses)

# Example usage
print(unknown())
