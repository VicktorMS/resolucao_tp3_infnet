from password import ASCII_TABLE, generate_password, validate_password_strength

def encrypt_password(password, shift):
    """
    Criptografa uma senha utilizando uma cifra de substituição baseada na tabela ASCII imprimível.

    Args:
    password (str): A senha a ser criptografada.
    shift (int): O número de posições para deslocar os caracteres na tabela ASCII.

    Returns:
    str: A senha criptografada com base no deslocamento (shift) fornecido.
    """
    encrypted_password = []
    for char in password:
        ascii_char_idx = ASCII_TABLE.find(char)
        if ascii_char_idx != -1:  
            new_idx = (ascii_char_idx + shift) % len(ASCII_TABLE)
            encrypted_password.append(ASCII_TABLE[new_idx])
        else:
            encrypted_password.append(char)
    return "".join(encrypted_password)

def decrypt_password(encrypted_password, shift):
    """
    Descriptografa uma senha previamente criptografada, revertendo o deslocamento aplicado.

    Args:
    encrypted_password (str): A senha criptografada.
    shift (int): O número de posições usadas para o deslocamento durante a criptografia.

    Returns:
    str: A senha original descriptografada.
    """
    decrypted_password = []
    
    for char in encrypted_password:
        ascii_char_idx = ASCII_TABLE.find(char)
        if ascii_char_idx != -1:  
            new_idx = (ascii_char_idx - shift) % len(ASCII_TABLE)
            decrypted_password.append(ASCII_TABLE[new_idx])
        else:
            decrypted_password.append(char)
    return "".join(decrypted_password)
    
def encrypt_passwords(passwords, shift):
    """
    Criptografa uma lista de senhas, aplicando o mesmo deslocamento a cada uma delas.

    Args:
    passwords (list): Uma lista de senhas a serem criptografadas.
    shift (int): O número de posições para deslocar os caracteres na tabela ASCII.

    Returns:
    list: Uma lista de senhas criptografadas.
    """
    return [encrypt_password(password, shift) for password in passwords]

def decrypt_passwords(encrypted_passwords, shift):
    """
    Descriptografa uma lista de senhas previamente criptografadas, revertendo o deslocamento.

    Args:
    encrypted_passwords (list): Uma lista de senhas criptografadas.
    shift (int): O número de posições usadas para o deslocamento durante a criptografia.

    Returns:
    list: Uma lista de senhas descriptografadas.
    """
    return [decrypt_password(password, shift) for password in encrypted_passwords]   
    


# Testando a função de gerar senha
print("=" * 40)
print("Testando a função de gerar senha:")
generated_pw = generate_password(10)
print(f"Senha gerada: {generated_pw}")

# Testando a função de validar força de senha
print("=" * 40)
print("Testando a função de validar força de senha (senha fraca):")
weak_pw = "abc123"
validated_pw = validate_password_strength(weak_pw)
print(f"Senha original (fraca): {weak_pw}")
print(f"Senha validada (fortalecida): {validated_pw}")

print("=" * 40)
print("Testando a função de validar força de senha (senha forte):")
strong_pw = "Aa1@strong"
validated_pw = validate_password_strength(strong_pw)
print(f"Senha original (forte): {strong_pw}")
print(f"Senha validada: {validated_pw}")

# Testando o código de criptografia
print("=" * 40)
print("Testando criptografia e descriptografia de uma senha:")
testing_pw = generate_password(password_length=10)
encrypted_pw = encrypt_password(testing_pw, 12)
decrypted_pw = decrypt_password(encrypted_pw, 12)

print(f"Senha normal: {testing_pw}")
print(f"Senha criptografada (shift 12): {encrypted_pw}")
print(f"Senha descriptografada: {decrypted_pw}")

# Testando a criptografia e descriptografia de uma lista de senhas
print("=" * 40)
print("Testando criptografia e descriptografia de uma lista de senhas:")
password_list = [generate_password(password_length=10) for _ in range(3)]
encrypted_password_list = encrypt_passwords(password_list, 12)
decrypted_password_list = decrypt_passwords(encrypted_password_list, 12)

print(f"\nLista de senhas originais: {password_list}")
print(f"Lista de senhas criptografadas (shift 12): {encrypted_password_list}")
print(f"Lista de senhas descriptografadas: {decrypted_password_list}")
print("=" * 40)
