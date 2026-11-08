
import hashlib

# Example candidate salt from the assignment
salt = "www.exploringsecurity.com"

# Demonstration password (not a recovered password)
password = "12345"

# Test the hypothesis: SHA1(salt + password)
combined = salt + password
result = hashlib.sha1(combined.encode("utf-8")).hexdigest()

print("Candidate salt:", salt)
print("Test password:", password)
print("Combined input:", combined)
print("Generated hash:", result)
print("Hash length:", len(result))
