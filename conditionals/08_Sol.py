# Password Strength Checker
# Problem: Check if a password is "Weak", "Medium", or "Strong". Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).

user_password = "pass@2433u5"
password_length = len(user_password)

if password_length < 6:
    password = "Weak"
elif password_length <= 10:
    password = "Medium"
else:
    password = "Strong"

print(password)