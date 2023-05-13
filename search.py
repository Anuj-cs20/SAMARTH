import openai
import os

# Load OpenAI API key from file
with open("openai_api_key.txt", "r") as f:
    openai.api_key = f.read().strip()

# Define function to execute command
def execute_command(command):
    os.system(command)


# Get task input from user
task = input("Enter task: ")

# Search for commands using OpenAI API
model_engine = "davinci"
prompt = f"write only os command to {task} in Mac"
completions = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=200,
    n=1,
    stop=None,
    temperature=0.5,
)
commands = completions.choices[0].text.strip()
print(commands)
# Execute commands
# for command in commands.split("\n"):
#     execute_command(command.strip())
