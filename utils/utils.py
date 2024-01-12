def text_purify(text: str):
    """
    Remove whitespaces from string
    """
    return text.strip()

def todigit(text: str):
    digits = ''.join(filter(str.isdigit, text))
    return digits
    