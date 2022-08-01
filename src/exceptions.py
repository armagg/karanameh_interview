class NotUrlError(Exception):
    """
    when input for shorting is not a url
    """
    pass

class NotExistErorr(Exception):
    """
    when called shortend link not exists
    """
    pass