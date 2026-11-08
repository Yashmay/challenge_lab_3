
import hashlib
import time

# Tomtom's hash from the assignment
target = "06f6fe0f73c6e197ee43eff4e5f7d10fb9e438b2"

# Salt hypotheses based on document contents
salts = [
    "www.exploringsecurity.com",
    "exploringsecurity.com",
    "exploringsecurity",
    "CommonHash",
]

start = time.time()
found = False

for salt in salts:
    print(f"\nTesting salt: {salt}")

    for number in range(100000):
        password = f"{number:05d}"

        # Two possible concatenation orders
        combinations = [
            ("salt + password", salt + password),
            ("password + salt", password + salt),
        ]

        for method, combined in combinations:
            result = hashlib.sha1(
                combined.encode("utf-8")
            ).hexdigest()

            if result == target:
                print("\nMATCH FOUND!")
                print("Password:", password)
                print("Salt:", salt)
                print("Method:", method)
                found = True
                break

        if found:
            break

    if found:
        break

if not found:
    print("\nNo match in this search.")
    print("Other salts, methods or lengths remain possible.")

print(f"Elapsed time: {time.time() - start:.2f} seconds")
