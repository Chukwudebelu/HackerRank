#!/bin/python3

def fun(s) -> bool:
    valid = True
    
    if s.count('@') != 1:
        return not valid
    else:
        username, rear = s.split('@')
        if len(username) > 0:
            for t in username:
                if not (t.isalnum() or t in ['_', '-']):
                    return not valid
        else:
            return not valid
                
        if rear.count(".") != 1:
            return not valid
        else:
            website, extension = rear.split('.')
            if len(extension) > 3:
                return not valid
            else:
                for t in extension:
                    if not t.isalpha():
                        return not valid
            
            for t in website:
                if not t.isalnum():
                    return not valid
    return valid
      
def filter_mail(emails) -> list:
    return [*filter(fun, emails)]

if __name__ == "__main__":
    n = int(input())
    emails = [str(input()) for _ in range(n)]

filtered_emails = filter_mail(emails)
print(sorted(filtered_emails))
