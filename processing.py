import re

def normalizeCode(raw_code):
    pattern = re.compile("[\s-]")
    result = re.sub(pattern, "", raw_code)
    return result