
import hashlib
import hmac

salt = "www.exploringsecurity.com"
password = "12345"

methods = {
    "SHA1(salt + password)":
        hashlib.sha1((salt + password).encode()).hexdigest(),

    "SHA1(password + salt)":
        hashlib.sha1((password + salt).encode()).hexdigest(),

    "SHA1(password)":
        hashlib.sha1(password.encode()).hexdigest(),

    "HMAC-SHA1":
        hmac.new(
            salt.encode(),
            password.encode(),
            hashlib.sha1
        ).hexdigest()
}

for method, result in methods.items():
    print(f"{method}: {result}")
