# --- METHODS YOU'LL USE DAILY ---

response = "  The answer is 42.  \n"

# 1. strip() - Remove whitespace (LLM responses often have extra spaces)
clean = response.strip()
print(f"'{clean}'")  # 'The answer is 42.'

# 2. split() - Break into parts (parsing structured responses)
text = "apple,banana,cherry"
items = text.split(",")
print(items)  # ['apple', 'banana', 'cherry']

# 3. join() - Combine list into string (building prompts from parts)
parts = ["Step 1: Think", "Step 2: Analyze", "Step 3: Answer"]
combined = "\n".join(parts)
print(combined)

# 4. replace() - Substitute text (cleaning responses)
messy = "The answer is: ```42```"
clean = messy.replace("```", "")
print(clean)  # 'The answer is: 42'

# 5. lower()/upper() - Normalize case (for comparison)
user_input = "YES"
if user_input.lower() == "yes":
    print("User agreed")

# 6. startswith()/endswith() - Check patterns
response = "Error: Invalid input"
if response.startswith("Error"):
    print("Handle error!")

# 7. find()/index() - Locate substrings
text = "The capital of France is Paris"
pos = text.find("Paris")
print(f"'Paris' found at position {pos}")

# 8. in operator - Check if substring exists
if "Paris" in text:
    print("Found it!")