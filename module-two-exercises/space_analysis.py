#Part 1 - Classify Space Complexity#
#Function A: O(n) slicing creates a brand‑new reversed string of the same length as the input.#
#Function B: O(k) — the dictionary only stores one entry per unique character, so space grows with the number of distinct characters rather than the total length.#
#Function C: O(n^2) — the function builds an n×n matrix, which requires storing n^2 integers.#
#Function D: O(1) — it keeps only a single running total regardless of how large the input list is.#


#Time: O(n) average — hash lookups and inserts are O(1)#
#Space: O(n) — stores all emails, but each set entry has extra hash-table overhead#
#FAST, No sorting step, hash lookups are extremely quick, runtime grows linearly with the number of rows#
#Why it uses more memory-the object reference, the hash, empty slots for load factor, padding for future growth#
#On 64GB RAM, choose set‑based (much faster)#
def find_duplicates_set(emails):
    seen = set()
    duplicates = set()

    for email in emails:
        if email in seen:
            duplicates.add(email)
        else:
            seen.add(email)

    return duplicates

#Time: O(n log n) — sorting dominates the runtime#
#Space: O(n) — stores all emails in a list; lists use less memory per item than sets#
#Why this is slower-O(n log n) dominates the runtime#
#Why it uses less memory-A pointer to each string, No hashing, no load-factor padding# 
#On 4GB RAM, choose sort‑and‑scan (lower memory footprint)#
def find_duplicates_sort(emails):
    emails_sorted = sorted(emails)
    duplicates = set()

    for i in range(1, len(emails_sorted)):
        if emails_sorted[i] == emails_sorted[i - 1]:
            duplicates.add(emails_sorted[i])

    return duplicates