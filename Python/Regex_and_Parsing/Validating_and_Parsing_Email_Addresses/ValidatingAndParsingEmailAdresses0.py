#!/bin/python3
# Without using the Regex Module
# Enter your code here. Read input from STDIN. Print output to STDOUT
def getEmail(email) -> str:
    """
    getEmail: Filters the email address in the form: NAME <username@domain.extension>
    """
    name, email_address = email.split(' ')
    return email_address[1:len(email_address)-1]


if __name__ == "__main__":
    n = int(input().strip())
    
    for _ in range(0, n):
        email = input('')
        email_address = getEmail(email)
        
        try:  # For cases with double '@'
            if (email_address.count('@') == 1 and email_address.__contains__('@') and email_address.__contains__('.')):
                isValidEmail = True
                details = email_address.split('@')
                username, domain_and_ext = details  # Get the username
                domain, extension = domain_and_ext.split('.')   # Get the domain & extension
            else:
                isValidEmail = False
        
            try:  # For cases with ',', '-', and '.' in the extension
                isUsernameStartGood = True if (username[0].isalpha()) else False
            
                isRestOfUsernameGood = True if (username[1:].isalnum() or '-' in username[1:] or '.' in username[1:] or '_' in username[1:]) else False
                
                isDomainAlphabetic = True if (domain.isalpha()) else False
                
                isExtensionAlphabetic = True if (extension.isalpha()) else False
                
                isExtensionLengthGood = bool(1 if (1 <= len(extension) <= 3) else 0)
                
                if all([isValidEmail, isUsernameStartGood, isRestOfUsernameGood, isDomainAlphabetic, isExtensionAlphabetic, isExtensionLengthGood]):
                    print(email)
                else:
                    print('', end = '')

            except NameError:
                print('', end = '')
                
        except ValueError or NameError:
            print('',  end= '')
