class CustomValueError(Exception):
    def __init__(self,message="The Choice is not between 1 and 5"):
        self.message = message

