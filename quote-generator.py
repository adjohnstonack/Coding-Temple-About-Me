import random

quotes = [
    ("The best way to get started is to quit talking and begin doing.", "Walt Disney"),
    ("It always seems impossible until it’s done.", "Nelson Mandela"),
    ("Success is not final, failure is not fatal: it is the courage to continue that counts.", "Winston Churchill"),
    ("Believe you can and you're halfway there.", "Theodore Roosevelt"),
    ("Dream big and dare to fail.", "Norman Vaughan"),
    ("Everything you’ve ever wanted is on the other side of fear.", "George Addair"),
    ("Act as if what you do makes a difference. It does.", "William James"),
    ("The future belongs to those who believe in the beauty of their dreams.", "Eleanor Roosevelt"),
    ("Do what you can, with what you have, where you are.", "Theodore Roosevelt"),
    ("What you get by achieving your goals is not as important as what you become by achieving your goals.", "Zig Ziglar")
]

quote, author = random.choice(quotes)
print(f'"{quote}" — {author}')
