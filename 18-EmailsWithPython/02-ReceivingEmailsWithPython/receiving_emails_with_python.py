import imaplib
import getpass
import email

M = imaplib.IMAP4_SSL('imap.gmail.com')

email = getpass.getpass("Email: ")
password = getpass.getpass("Password: ")

M.login(email, password)
# M.list()

M.select('inbox')

(typ, data) = M.search(None, 'SUBJECT "New test python"')
email_id = data[0]

(result, email_data) = M.fetch(email_id, '(RFC822)')

raw_email = email_data[0][1]
raw_email_str = raw_email.decode('utf-8')

email_message = email.message_from_string(raw_email_str)

for part in email_message.walk():
    if part.get_content_type() == 'text/html':
        body = part.get_payload(decode=True)

        print(body)