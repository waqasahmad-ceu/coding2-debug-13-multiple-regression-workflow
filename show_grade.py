"""Display your Homework 2 mark: uv run python show_grade.py."""

from hashlib import sha256

SALT = "5615b9dc5cb59f30cabcac5b9c8bed2b"
GRADE_HASH = "3ae40e12157c7dd3b67c7c98d2930674b808592764e1beee7045ef76f1ff9eac"

# Match the stored hash against each possible whole-number mark.
for mark in range(101):
    candidate = sha256(f"{SALT}:{mark}".encode("utf-8")).hexdigest()
    if candidate == GRADE_HASH:
        print(f"Homework 2: {mark}/100")
        break
else:
    raise RuntimeError("The mark could not be verified. Please contact the instructor.")
