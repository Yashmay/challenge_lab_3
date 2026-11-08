
from itertools import product

usernames = ["Sparky", "Mark123", "superman", "JillC"]

candidates = set()

for username in usernames:
    for variant in {username, username.lower(), username.upper()}:
        if 5 <= len(variant) <= 7:
            candidates.add(variant)

        for digit in "0123456789":
            for candidate in (variant + digit, digit + variant):
                if 5 <= len(candidate) <= 7:
                    candidates.add(candidate)

# Small set of common example patterns
candidates.update([
    "abc123", "123abc", "pass123",
    "qwerty", "123456", "1234567",
    "admin1", "welcome", "letmein",
])

with open("candidates.txt", "w", encoding="utf-8") as file:
    for candidate in sorted(candidates):
        if 5 <= len(candidate) <= 7:
            file.write(candidate + "\n")

print(f"Generated {len(candidates)} candidate strings.")
print("Saved candidates.txt")
