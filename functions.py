def deEmojify(text):
    import re
    regrex_pattern = re.compile(pattern = "["
        u"\U0001F600-\U0001F64F"
        u"\U0001F300-\U0001F5FF"
        u"\U0001F680-\U0001F6FF"
        u"\U0001F1E0-\U0001F1FF"
        u"\U0001FA70-\U0001FAFF"
        u"\U0001FB00-\U0001FBFF"
                           "]+", flags = re.UNICODE)
    return regrex_pattern.sub(r'',text)