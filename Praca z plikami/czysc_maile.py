import sys

input_file = sys.argv[1]
output_file = sys. argv[2]

#najpierw bez pomocy funkcji
with open("dane/" + input.file) as in_file:   #z tego powstanie napis
    data = in_file.read().splitlines()


cleaned_emails = set()
for email in data:
    if email.count("@") == 1:
        cleaned_emails.add(email.strip().lower())

    cleaned_emails = list(cleaned_emails)
    cleaned_emails.sort()
    return cleaned_emails






