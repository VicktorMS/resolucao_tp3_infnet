import random
import string

# Tabela ASCII imprimível
ASCII_TABLE = string.printable.strip()

def generate_password(password_length):
    """
    Gera uma senha aleatória com o comprimento especificado.

    Args:
    password_length (int): O comprimento da senha a ser gerada.

    Returns:
    str: Uma nova senha gerada aleatoriamente a partir da tabela ASCII imprimível.
    """
    new_password = ""
    for _ in range(password_length):
        random_char_idx = random.randint(0, len(ASCII_TABLE) - 1)
        new_password += ASCII_TABLE[random_char_idx]
    return new_password

def validate_password_strength(password):
    """
    Valida a força de uma senha. Se a senha for muito curta ou não contiver todos os tipos de caracteres necessários
    (maiúsculas, minúsculas, números e caracteres especiais), uma nova senha é gerada.

    Args:
    password (str): A senha a ser validada.

    Returns:
    str: A senha original, se for forte o suficiente, ou uma nova senha gerada se a original não for válida.
    """
    if len(password) < 8:
        return generate_password(password_length=8)
    
    has_upper, has_lower, has_number, has_special = False, False, False, False

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_number = True
        else:
            has_special = True
    
    # Verifica se a senha contém pelo menos um de cada tipo de caractere
    if has_upper and has_lower and has_number and has_special:
        return password
    else:
        return generate_password(password_length=len(password))


