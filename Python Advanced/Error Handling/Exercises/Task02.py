class Error(Exception):
    """Base class for other exceptions"""
    pass


class NameTooShortError(Error):
    """Name must be more than 4 characters"""


class MustContainAtSymbolError(Error):
    """Email must contain @"""


class InvalidDomainError(Error):
    """Domain must be one of the following: .com, .bg, .org, .net"""


email = input()

while email != 'End':

    if email.count('@') < 1:
        raise MustContainAtSymbolError("Email must contain @")

    idx_of_symbol = email.index('@')
    name = email[:idx_of_symbol]
    if len(name) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")

    idx_of_starting_domain = email.index('.')
    domain = email[idx_of_starting_domain:]
    if domain not in ('.com', '.bg', '.org', '.net'):
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")

    email = input()