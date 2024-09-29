QUANTIFIERS = ["at least", "at most", "exactly"]


def format_object_text(quantity: int, object_type=None, color=None, style=None):
    subject = ""
    if color:
        subject += f" {color}"
    if style:
        subject += f" {style}"
    if object_type:
        if quantity == 1:
            subject += f" {object_type}"
        else:
            subject += f" {object_type}s"
    else:
        if quantity == 1:
            subject += " object"
        else:
            subject += " objects"
    subject = subject.strip()

    return subject


def number_to_times(quantity: int):
    if quantity == 0:
        return "no"

    if quantity == 1:
        return "once"

    if quantity == 2:
        return "twice"

    if quantity == 3:
        return "three times"

    if quantity == 4:
        return "four times"

    if quantity == 5:
        return "five times"

    return f"{quantity} times"
