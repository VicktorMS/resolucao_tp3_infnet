
def validate_cpf(cpf):
    if len(cpf) < 11 or not cpf.isdigit():
        return False, ""
    return True, f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}"

def validate_email(email):
    email = email.lower()
    if not all(char in email for char in ["@", "."]):
        return False, "Email inválido! Não contém '@' ou '.'"
    
    host, domain = email.split("@", 1)
    
    if not host.isalnum() or "." not in domain:
        return False, "Email contém caracteres não alfa-numéricos ou domínio inválido"
    
    domain_name, extension = domain.rsplit(".", 1)
    
    
    if not domain_name.isalnum() or not extension.isalpha():
        return False, "Email contém domínio ou extensão do domínio inválidos"
    
    return True, email

def validate_phone_number(phone_number):
    cleaned_number, formatted_phone_number = "", ""
    for char in phone_number:
        if char.isdigit():
            cleaned_number += (char)
            
    if not 10 <= len(cleaned_number) <= 11:
        return False, ''
    else:
        formatted_phone_number = f"({cleaned_number[:2]})"
        if len(cleaned_number) == 10:
            formatted_phone_number += f" {cleaned_number[2:6]}-{cleaned_number[6:10]}"
        else:
            formatted_phone_number += f" {cleaned_number[2:7]}-{cleaned_number[7:11]}"
        
    return True, formatted_phone_number

# print(validate_email("victormoraes@gmail.com"))
print(validate_phone_number("1234567891"))