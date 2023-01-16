import re
def Validation(CC):
    if len(re.findall(r'\d', CC))==16:
        if re.findall(r'^[456]',CC):
            a=re.sub(r'\d{4}', "",CC)
            b=re.sub(r'[^\d{4}]', "",CC)
            if a!= "---":
                if a!= "":
                    return "Invalid"
                else:
                    return "Valid"
            else:
                if re.findall(r'((\d)\2{3,})',b):
                    return "Invalid"
                else:
                    return "Valid"
        else:
            return "Invalid"
    else:
        return "Valid"