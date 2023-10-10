import re

email = input("what's your email? ").strip()

print("valid") if re.search(r"^\w+@\w+\.edu$", email) else print("Invalid")









