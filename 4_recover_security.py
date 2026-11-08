
import hashlib
import time

salt = "www.exploringsecurity.com"
target = "fafa4483874ec051989d53e1e432ba3a6c6b9143"

start = time.time()
found = False

for length in range(5, 8):
    print(f"Testing {length}-digit passwords...")

    for number in range(10 ** length):
        password = f"{number:0{length}d}"

        combined = salt + password
        generated = hashlib.sha1(
            combined.encode("utf-8")
        ).hexdigest()

        if generated == target:
            print("\nMATCH FOUND!")
            print("Username: security")
            print("Password:", password)
            print("Length:", length)
            print("Salt:", salt)
            found = True
            break

    if found:
        break

if not found:
    print("No matching password found.")

print(f"Elapsed: {time.time() - start:.2f} seconds")
