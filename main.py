import csv
import vobject
import sys

COLS = [
    'First Name',  # 0
    'Middle Name',  # 1
    'Last Name',  # 2
    'Title',  # 3
    'Suffix',  # 4
    'Nickname',  # 5
    'Given Yomi',  # 6
    'Surname Yomi',  # 7
    'E-mail Address',  # 8
    'E-mail 2 Address',  # 9
    'E-mail 3 Address',  # 10
    'Home Phone',  # 11
    'Home Phone 2',  # 12
    'Business Phone',  # 13
    'Business Phone 2',  # 14
    'Mobile Phone',  # 15
    'Car Phone',  # 16
    'Other Phone',  # 17
    'Primary Phone',  # 18
    'Pager',  # 19
    'Business Fax',  # 20
    'Home Fax',  # 21
    'Other Fax',  # 22
    'Company Main Phone',  # 22
    'Callback',  # 23
    'Radio Phone',  # 24
    'Telex',  # 25
    'TTY/TDD Phone',  # 26
    'IMAddress',  # 27
    'Job Title',  # 28
    'Department',  # 29
    'Company',  # 30
    'Office Location',  # 31
    "Manager's Name",  # 32
    "Assistant's Name",  # 33
    "Assistant's Phone",  # 34
    'Company Yomi',  # 35
    'Business Street',  # 36
    'Business City',  # 37
    'Business State',  # 38
    'Business Postal Code',  # 39
    'Business Country/Region',  # 40
    'Home Street',  # 41
    'Home City',  # 42
    'Home State',  # 43
    'Home Postal Code',  # 44
    'Home Country/Region',  # 45
    'Other Street',  # 46
    'Other City',  # 47
    'Other State',  # 48
    'Other Postal Code',  # 49
    'Other Country/Region',  # 50
    'Personal Web Page',  # 51
    'Spouse',  # 52
    'Schools',  # 53
    'Hobby',  # 54
    'Location',  # 55
    'Web Page',  # 56
    'Birthday',  # 57
    'Anniversary',  # 58
    'Notes',  # 59
]

if __name__ == '__main__':
    reader = csv.reader(sys.stdin)



    for line in reader:
        card = vobject.vCard()

        card.add('n')
        card.n.value = vobject.vcard.Name(family=line[2], given=line[0])
        card.add('fn')
        card.fn.value = f'{line[0]} {line[2]}'
        card.add('email')
        card.email.value = line[8]
        card.add('org')
        card.org.value = line[30]

        for ix in [11, 12, 13, 14, 15]:
            val = line[ix]
            if val:
                card.add('tel')
                card.tel.value = val

        sys.stdout.write(card.serialize())
