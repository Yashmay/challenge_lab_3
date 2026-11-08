
import hashlib

# A sample SHA-1 hash for comparison
sample = hashlib.sha1(b"hello").hexdigest()

print("SHA-1 example:", sample)
print("Hash length:", len(sample))
print("Hash format:", "hexadecimal")
print("SHA-1 digest size:", hashlib.sha1().digest_size * 8, "bits")
