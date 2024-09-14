def format_subject(quantity: int, object_type=None, color=None, style=None):
    subject = ""
    if color:
        subject += f" {color}"
    if style:
        subject += f" {style}"
    if object_type:
        if quantity < 2:
            subject += f" {object_type}"
        else:
            subject += f" {object_type}s"
    else:
        if quantity < 2:
            subject += " object"
        else:
            subject += " objects"
    return subject.strip()
