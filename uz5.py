"""
Parašykite programą, apibrėžiančią funkciją extract_email_addresses(), kuri priima tekstą kaip įvestį ir iš teksto ištraukia visus el. pašto adresus
"""


def extract_email_addresses():
    enter = input("Enter text containing Email addresses: ")
    emails = []
    for email in enter.split():
        if "@" in email and "." in email: emails.append(email)
        return emails

emails = extract_email_addresses()
print(emails)

