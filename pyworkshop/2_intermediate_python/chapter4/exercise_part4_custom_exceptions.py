class MyException(Exception):
    def __init__(self, message):
       new_message = f"!!!ERROR!!! {message}"
        super().__init__(new_message)

raise MyException("Something went wrong!")