# Validação dos dados 
def validate_cpf(cpf):
    """
    Valida um CPF com base em seu comprimento e verifica se contém apenas dígitos.
    
    Args:
        cpf (str): O CPF a ser validado.
    
    Returns:
        tuple: (bool, str) - True e CPF formatado se for válido, False e string vazia se for inválido.
    """
    if len(cpf) != 11 or not cpf.isdigit():
        return False, "CPF inválido! Deve conter 11 dígitos numéricos."
    
    # Formatação: XXX.XXX.XXX-XX
    return True, f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}"


def validate_email(email):
    """
    Valida um e-mail verificando se contém '@', '.' e se o domínio e extensão são válidos.
    O e-mail será convertido para minúsculas.
    
    Args:
        email (str): O e-mail a ser validado.
    
    Returns:
        tuple: (bool, str) - True e e-mail formatado se for válido, False e mensagem de erro se for inválido.
    """
    email = email.lower()  # Normaliza para minúsculas

    if not all(char in email for char in ["@", "."]):
        return False, "Email inválido! Não contém '@' ou '.'."
    
    try:
        host, domain = email.split("@", 1)
    except ValueError:
        return False, "Email inválido! Não contém '@' corretamente."
    
    if not host.isalnum() or "." not in domain:
        return False, "Email contém caracteres não alfanuméricos ou domínio inválido."
    
    try:
        domain_name, extension = domain.rsplit(".", 1)
    except ValueError:
        return False, "Domínio do email inválido! Falta a extensão após o ponto."

    if not domain_name.isalnum() or not extension.isalpha():
        return False, "Email contém domínio ou extensão do domínio inválidos."

    return True, email


def validate_phone_number(phone_number):
    """
    Valida e formata um número de telefone. O número deve conter entre 10 e 11 dígitos.
    
    Args:
        phone_number (str): O número de telefone a ser validado.
    
    Returns:
        tuple: (bool, str) - True e número formatado se for válido, False e string vazia se for inválido.
    """
    cleaned_number = ""
    
    # Limpa o número, removendo caracteres que não são dígitos
    for char in phone_number:
        if char.isdigit():
            cleaned_number += char
    
    # Verifica se o número tem entre 10 e 11 dígitos
    if not 10 <= len(cleaned_number) <= 11:
        return False, "Número de telefone inválido! Deve conter 10 ou 11 dígitos."

    # Formatação: (XX) XXXX-XXXX ou (XX) XXXXX-XXXX
    if len(cleaned_number) == 10:
        formatted_phone_number = f"({cleaned_number[:2]}) {cleaned_number[2:6]}-{cleaned_number[6:10]}"
    else:
        formatted_phone_number = f"({cleaned_number[:2]}) {cleaned_number[2:7]}-{cleaned_number[7:11]}"
    
    return True, formatted_phone_number


# Funções de entrada e validação
def input_and_validate_cpf():
    """
    Solicita ao usuário o CPF e valida até que ele forneça um CPF válido.
    """
    while True:
        cpf = input("Digite seu CPF (apenas números): ")
        is_valid, result = validate_cpf(cpf)
        if is_valid:
            print(f"CPF válido: {result}")
            break
        else:
            print(result) 


def input_and_validate_email():
    """
    Solicita ao usuário o e-mail e valida até que ele forneça um e-mail válido.
    """
    while True:
        email = input("Digite seu e-mail: ")
        is_valid, result = validate_email(email)
        if is_valid:
            print(f"E-mail válido: {result}")
            break
        else:
            print(result) 


def input_and_validate_phone():
    """
    Solicita ao usuário o número de telefone e valida até que ele forneça um número válido.
    """
    while True:
        phone_number = input("Digite seu número de telefone: ")
        is_valid, result = validate_phone_number(phone_number)
        if is_valid:
            print(f"Número de telefone válido: {result}")
            break
        else:
            print(result)  