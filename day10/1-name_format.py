"""Functions with output"""


def format_name(f_name, l_name):
    """Format user names into title case"""
    if f_name == "" or l_name == "":
        return "Please provide valid input"
    return "{} {}".format(f_name.title(), l_name.title())


name = format_name("tam", "adb")
print(name)
