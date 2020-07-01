import smtplib
from pathlib import Path

from string import Template

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

MY_ADDRESS = 'blah'
PASSWORD = 'blah'

contactsDir = Path("/Users/aravindmadanagopal/Documents/Personal/Personal_projects/resources")
contactsList = contactsDir / "contacts.txt"

emailDir = Path("/Users/aravindmadanagopal/Documents/Personal/Personal_projects/resources")
emailTemp = emailDir / "email_template.txt"


def get_contacts(contactsList):
    names = []
    emails = []
    with open(contactsList, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            names.append(a_contact.split()[0])
            emails.append(a_contact.split()[1])
    return names, emails


def read_template(emailTemp):
    with open(emailTemp, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
        print(template_file_content)
    return Template(template_file_content)


def main():
    names, emails = get_contacts(contactsList)  # read contacts
    message_template = read_template(emailTemp)

    # set up the SMTP server
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)

    # For each contact, send the email:
    for name, email in names, emails:
        msg = MIMEMultipart()  # create a message

        # add in the actual person name to the message template
        message = message_template.substitute(PERSON_NAME=name.title())

        # Prints out the message body for our sake
        print(message)

        # setup the parameters of the message
        msg['From'] = MY_ADDRESS
        msg['To'] = email
        msg['Subject'] = "This is TEST"

        # add in the message body
        msg.attach(MIMEText(message, 'plain'))

        # send the message via the server set up earlier.
        s.send_message(msg)
        del msg

    # Terminate the SMTP session and close the connection
    s.quit()


if __name__ == '__main__':
    main()
