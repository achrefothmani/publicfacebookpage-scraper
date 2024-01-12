def text_purify(text: str):
    """
    Remove whitespaces from string
    """
    return text.strip()

def todigit(text: str):
    """
    return a string with only digits
    """
    
    digits = ''.join(filter(str.isdigit, text))
    return digits


def extract_date(text: str):
    """
    Extract published date from facebook post
    """
    text = text.split('\n')
    return text_purify(text[0])
    
    