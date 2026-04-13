def contamination(text, char):
    if not text or not char:
        return ""
    
    return char * len(text)