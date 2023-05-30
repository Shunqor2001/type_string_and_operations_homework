def main(word):
    """"Return an optional string of length eight
    Args:
        None
    Returns:
        str: return answer.
    """
    if  8 == len(word):
        return word
    else:
        return "none"
print(main("sagjdsa"))