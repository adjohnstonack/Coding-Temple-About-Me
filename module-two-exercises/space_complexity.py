"""
===========================================================
Part 1 — Space Complexity Classification
===========================================================
"""

# Function A
# Space Complexity: O(n)
# Explanation: Slicing creates a brand‑new reversed string, requiring space proportional to the input length.
def reverse_string(s):
    return s[::-1]


# Function B
# Space Complexity: O(k)
# Explanation: The dictionary stores one entry per unique character, so space grows with the number of distinct characters.
def count_letters(text):
    counts = {}
    for char in text:
        counts[char] = counts.get(char, 0) + 1
    return counts


# Function C
# Space Complexity: O(n^2)
# Explanation: Builds an n×n matrix, which requires storing n² integers.
def matrix_identity(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]


# Function D
# Space Complexity: O(1)
# Explanation: Uses only a single running total regardless of input size.
def running_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    print(total)



"""
===========================================================
Part 2 — Duplicate Email Detection Approaches
===========================================================
"""

# ----------------------------------------------------------
# Approach 1: Set-based duplicate detection
# Time Complexity: O(n) average — set insert & lookup are O(1)
# Space Complexity: O(n) — stores all emails, with extra hash-table overhead
# ----------------------------------------------------------
def find_duplicates_set(emails):
    seen = set()
    duplicates = set()

    for email in emails:
        if email in seen:
            duplicates.add(email)
        else:
            seen.add(email)

    return duplicates


# ----------------------------------------------------------
# Approach 2: Sort-and-scan duplicate detection
# Time Complexity: O(n log n) — sorting dominates runtime
# Space Complexity: O(n) — stores all emails in a list; lists use less memory per item
# ----------------------------------------------------------
def find_duplicates_sort(emails):
    emails_sorted = sorted(emails)
    duplicates = set()

    for i in range(1, len(emails_sorted)):
        if emails_sorted[i] == emails_sorted[i - 1]:
            duplicates.add(emails_sorted[i])

    return duplicates



"""
===========================================================
Tradeoff Decision
===========================================================

Machine with 4GB RAM:
    Choose: Sort-and-scan approach
    Reason: A list has lower per-item memory overhead than a set.
            With 5 million rows, avoiding hash-table bloat helps prevent
            running out of memory. Priority: memory efficiency.

Machine with 64GB RAM:
    Choose: Set-based approach
    Reason: Plenty of RAM means the extra overhead of a set is irrelevant.
            The O(n) runtime is significantly faster than O(n log n).
            Priority: speed.
===========================================================
"""