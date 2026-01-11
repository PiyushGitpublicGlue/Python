# Variables
name = "Claude"
role = "AI Assistant"
temperature = 0.7

# Basic string
prompt = "You are a helpful assistant"

# f-string (THIS IS KEY FOR PROMPTS)
prompt_template = f"You are {name}, a {role}. Respond helpfully."
print(prompt_template)

# Multi-line f-string (common for prompts)
system_prompt = f"""
You are {name}.
Your role: {role}
Temperature setting: {temperature}

Instructions:
- Be helpful
- Be concise
- Be accurate
"""
print(system_prompt)