[24bcs170@mepcolinux itt]$cat course.py
Harish = {"C++", "C", "Python", "Java"}
Varshiv = {"C++", "AngularJS", "Flutter", "MongoDB"}

print("Common Interests         : ", end = "")
common = Harish & Varshiv
for course in common:
   print(course, end = ", ")
print()

print("Harish's Suggestions    : ", end = "")
harish = Harish - Varshiv
for course in harish:
   print(course, end = ", ")
print()

print("Varshiv's Suggestions : ", end="")
varshiv = Varshiv - Harish
for course in varshiv:
   print(course, end = ", ")
print()



[24bcs170@mepcolinux itt]$cat email.py
import re

def is_valid_gmail(email):
    banned_words = [
        "king", "boss", "cool", "official", "real",
        "legend", "hacker", "admin", "support"
    ]

    # Must end with @gmail.com
    if not email.endswith("@gmail.com"):
        return False, "Email must end with @gmail.com"

    username = email[:-10]  # remove '@gmail.com'

    # Length check
    if len(username) < 6 or len(username) > 30:
        return False, "Username length must be between 6 and 30 characters"

    # Only lowercase letters, numbers, dot
    if not re.fullmatch(r"[a-z0-9.]+", username):
        return False, "Only lowercase letters, numbers, and and dots allowed"

    # Must start and end with a letter
    if not (username[0].isalpha()):
        return False, "Username must start and end with a letter"

    # No consecutive dots
    if ".." in username:
        return False, "Consecutive dots are not allowed"

    # Numbers only allowed at the end
    if re.search(r"[0-9]+[a-z]", username):
        return False, "Numbers must appear only at the end"

    # Banned words check
    for word in banned_words:
        if word in username:
            return False, f"Username contains banned word: '{word}'"

    return True, "Valid professional Gmail ID"


# Main Program
email = input("Enter a Gmail ID: ").strip()

valid, message = is_valid_gmail(email)

if valid:
   print("ACCEPTED:", message)
else:
   print("REJECTED:", message)
