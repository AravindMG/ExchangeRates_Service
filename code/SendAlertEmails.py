from string import Template


def get_contacts():
    names = []
    emails = []
    with open("../resources/contacts.txt", mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            names.append(a_contact.split()[0])
            emails.append(a_contact.split()[1])
    return names, emails


def read_template():
    with open("../resources/email_template.txt", 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
        print(template_file_content)
    return Template(template_file_content)


if __name__ == '__main__':
    read_template()
