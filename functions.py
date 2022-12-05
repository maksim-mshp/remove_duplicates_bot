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

def is_duplicate(words1, words2, max_intersection):
    words1 = set(words1)
    words2 = set(words2)
    length = (len(words1) + len(words2)) // 2
    intersection = words1.intersection(words2)
    
    return (len(intersection) / length) >= (max_intersection / 100)

if __name__ == "__main__":
    a = """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Et magnis dis parturient montes nascetur ridiculus mus. Lacus vel facilisis volutpat est velit egestas dui id ornare. Vitae tortor condimentum lacinia quis vel eros. Elit duis tristique sollicitudin nibh sit. Vitae purus faucibus ornare suspendisse sed nisi. Eu consequat ac felis donec et odio pellentesque diam. Auctor eu augue ut lectus arcu bibendum. Ultricies integer quis auctor elit. Commodo sed egestas egestas fringilla phasellus faucibus scelerisque eleifend donec. Arcu cursus euismod quis viverra. Netus et malesuada fames ac turpis egestas integer eget aliquet. Hendrerit dolor magna eget est. Velit scelerisque in dictum non. Nullam vehicula ipsum a arcu cursus. Eget nunc lobortis mattis aliquam faucibus purus. Congue eu consequat ac felis donec et.
    """
    b = """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Et magnis dis parturient montes nascetur ridiculus mus. Lacus vel facilisis volutpat est velit egestas dui id ornare. Vitae tortor condimentum lacinia quis vel eros. Elit duis tristique sollicitudin nibh sit. Vitae purus faucibus ornare suspendisse sed nisi. Eu consequat ac felis donec et odio pellentesque diam. Auctor eu augue ut lectus arcu bibendum. Ultricies integer quis auctor elit. Commodo sed egestas egestas fringilla phasellus faucibus scelerisque eleifend donec. Arcu cursus euismod quis viverra. Netus et malesuada fames ac turpis egestas integer eget aliquet. Hendrerit dolor magna eget est. Velit scelerisque in dictum non. Nullam vehicula ipsum a arcu cursus. Eget nunc lobortis mattis aliquam faucibus purus. Congue eu consequat ac felis donec et..
    """
    print(is_duplicate(a.split(), b.split(), 97))