import re
records = [
    "Name: Alice Johnson | Email: alice.j@gmail.com | Phone: (555) 123-4567 | Joined: 01/15/2023",
    "Name: Bob Smith | Email: bob_smith@yahoo.com | Phone: 555.987.6543 | Joined: 03-22-2023",
    "Name: Charlie Brown | Email: charlie@outlook.com | Phone: 555 111 2222 | Joined: 2023/07/01",
    "Name: Diana Prince | Email: diana.prince@company.co.uk | Phone: (555)444-3333 | Joined: 11/30/2023",
]


def extract_names(records):
    """Return a list of names."""
    pattern = r"Name:\s*([^|]+)"
    return [re.search(pattern, record).group(1).strip()
            for record in records]


def extract_emails(records):
    """Return a list of email addresses."""
    pattern = r"[\w\.-]+@[\w\.-]+\.\w+"
    return [re.search(pattern, record).group()
            for record in records]


def normalize_phones(records):
    """Return phone numbers in XXX-XXX-XXXX format."""
    phone_pattern = r"\(?(\d{3})\)?[\s\.-]?(\d{3})[\s\.-]?(\d{4})"

    phones = []

    for record in records:
        match = re.search(phone_pattern, record)

        if match:
            area, prefix, line = match.groups()
            phones.append(f"{area}-{prefix}-{line}")

    return phones


def extract_dates(records):
    """Return all dates regardless of format."""
    pattern = r"\d{2}[/-]\d{2}[/-]\d{4}|\d{4}[/-]\d{2}[/-]\d{2}"

    dates = []

    for record in records:
        match = re.search(pattern, record)

        if match:
            dates.append(match.group())

    return dates


def parse_records(records):
    """
    Return a list of dictionaries:
    {
        'name': ...,
        'email': ...,
        'phone': ...,
        'joined': ...
    }
    """

    parsed = []

    phone_pattern = r"\(?(\d{3})\)?[\s\.-]?(\d{3})[\s\.-]?(\d{4})"
    date_pattern = r"\d{2}[/-]\d{2}[/-]\d{4}|\d{4}[/-]\d{2}[/-]\d{2}"

    for record in records:

        name = re.search(r"Name:\s*([^|]+)", record).group(1).strip()

        email = re.search(
            r"[\w\.-]+@[\w\.-]+\.\w+",
            record
        ).group()

        phone_match = re.search(phone_pattern, record)
        phone = (
            f"{phone_match.group(1)}-"
            f"{phone_match.group(2)}-"
            f"{phone_match.group(3)}"
        )

        joined = re.search(date_pattern, record).group()

        parsed.append({
            "name": name,
            "email": email,
            "phone": phone,
            "joined": joined
        })

    return parsed


# -------------------
# Test Output
# -------------------

print("Names:")
print(extract_names(records))

print("\nEmails:")
print(extract_emails(records))

print("\nNormalized Phones:")
print(normalize_phones(records))

print("\nDates:")
print(extract_dates(records))

print("\nParsed Records:")
for record in parse_records(records):
    print(record)


    
