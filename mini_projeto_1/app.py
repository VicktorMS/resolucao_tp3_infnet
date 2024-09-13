from validation import input_and_validate_cpf, input_and_validate_email, input_and_validate_phone


def main():
    """
    Função principal que chama as funções de validação de CPF, e-mail e telefone.
    """
    print("Validação de dados pessoais")
    input_and_validate_cpf()      # Valida CPF
    input_and_validate_email()    # Valida e-mail
    input_and_validate_phone()    # Valida número de telefone
    print("Todos os dados foram validados com sucesso!")


# Chama a função principal
if __name__ == "__main__":
    main()