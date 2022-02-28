# csv2vcard

Made for converting an Office365 contacts export to a vcard that can be imported in icloud.

## Usage

Tested with a Python3.9 interpreter.

Pipe a CSV to stdin and a vcf file will be written to csv containing all contacts.

python3 main.py < /path/to/csv > output.vcf

