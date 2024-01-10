def fun(s):
    """  
    Return True if s is a valid email, else return False
    """
    # username@website.extension
    format_type = s.__contains__('@' and '.')
    amp, dot = s.find('@'), s.find('.')
    # amp = 0 if s.find('@') == 0 else amp
    username, web, ext = s[:amp] if amp != 0 else '', s[amp+1:dot], s[dot+1:]
    
    usernameFilter = lambda y: y.isalnum() or y.__contains__('_') or y.__contains__('-')
    usernameBool = all([usernameFilter(i) for i in username]) if amp != 0 else False
    
    webFilter = lambda y: y.isalnum()
    webBool = all([webFilter(j) for j in web])
    
    extFilter = lambda y: y.isalpha()
    extBool = all([extFilter(k) for k in ext] + [len(ext) <= 3])
    return all((format_type, usernameBool, webBool, extBool))
      
      
def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == "__main__":
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())
