import re
import os

regex_file = "^(\d+)\.txt$"
directory = "dumps"
list = os.listdir(directory)
for l in list:
    m = re.search(regex_file, l)
    if m:
        with open("{}/{}".format(directory, l), 'r') as f:
            string = f.read()

        (new_string, subs) = re.subn(
            "^\ +(\"is_free\":\ (true|false),|\"dlc\":\ |\d+(,|\ *\n\ +\],)).*$",
            "",
            string,
            flags=re.MULTILINE
        )

        new_string = re.sub(
            "\n\n+",
            "\n",
            new_string
        )

        with open("{}/{}".format(directory, l), 'w+') as f:
            f.write(new_string)

        if subs > 0:
            print("{}: {}".format(m.group(1), subs))


replace_regex = "^\ +(\"is_free\":\ (true|false),|\"dlc\":\ |\d+,?|\],).*$"
