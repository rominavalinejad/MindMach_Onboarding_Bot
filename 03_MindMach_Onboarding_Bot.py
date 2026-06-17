# --- MindMach Onboarding Bot ---

print (""""Welcome to MindMach!😍🥰"
Let's build your mind profile.""" )
print("-"*50)
# Step 1: Name and Surname Registration
user_name = input("Please enter your name (e.g. Romina):")
clean_name = user_name.strip().title()
user_family_name = input("Please enter your family name (e.g. Valinejad):")
clean_family_name = user_family_name.strip().title()
print(f"💠Thank you {clean_name} {clean_family_name}! Your name has been registered.")
print("-"*50)
# Step 2: Username Creation
create_username = input("Choose a unique username for your profile:")
clean_create_username = create_username.strip().lower()
print(f"💠Awesome! Your ID is now: @{clean_create_username}")
print("-"*50)
# Step 3: MBTI & Enneagram Profile
mbti_type = input("Enter your real MBTI type (e.g. ENTP):")
clean_mbti_type = mbti_type.upper().strip()
enneagram_type = input("Enter your real Enneagram type (e.g. 4w3):")
clean_enneagram_type = enneagram_type.lower().strip()
print(f"💠Analysis complete!✅\nYour mind resonates with the archetype of {clean_mbti_type} and the core drive of Enneagram {clean_enneagram_type}.")
print("-"*50)
print("Generating your Identity Card...🧠!")
print("-"*50)
# Step 4: Final Dynamic Ticket
print("Identity Card:")
line1 = f"| MINDMACH PROFILE NAME:  {clean_name} {clean_family_name}" .ljust(45) + "|"
line2 = f"| YOUR ID:                @{clean_create_username}" .ljust(45) + "|"
Line3 = f"| YOUR PERSONALITY TYPE:  {clean_mbti_type} {clean_enneagram_type}" .ljust(45) + "|"
print(line1)
print(line2)
print(Line3)
