# name = "Piyush"
# role = "Software Engineer in Test"
# temperature = 4.0

# #Basic String

# prompt = "You are a helpful Engineer"

# prompt_f = f"{name} is a {role}. {prompt}. Respond helpfully!"

# print(prompt_f)

# prompt_multi_f = f"""
# You are {name}.
# Your role : {role}
# Temperature setting : {temperature}

# Instructions:
# - Be helpful
# - Be concise
# - Be accurate
# """

# print(prompt_multi_f)

#print("Next Topic")

# strip() - Remove whitespaces
response = " The answer is 42. \n"
print(response)
clean = response.strip()
print(clean)

# split() - Break into parts

text = "apple,banana,cherry"
print(text)
items = text.split(",")
print(items)

# join() - combine list into string

parts = ["Step 1: Think","Step 2: Analyze", "Step3 : Answer"]
combined = "\n".join(parts)
print(combined)

# replace() - Substitute text

messy = "The answer is: ```42```"
clean = messy.replace("```","")
print(clean)

# lower()/upper()

user_input = "YES"
if user_input.lower() == 'yes':
    print("User Agreed!")

# startwith()/endswuth() - check patterns

response = "Error: Invalid input"
if response.startswith("Error"):
    print("Handle error!")
elif response.endswith("input"):
    print("OK!!")

# find()/index() - Locate substrings
text = "The capital of India is Delhi"
pos = text.find("India")
print(f"'India' found at position {pos}")

# in operator - Check if substring exists

if "Delhi" in text:
    print("Found it!")