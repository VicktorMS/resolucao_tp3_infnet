# Mini Projeto 1: Validação e Formatação de Dados em um Sistema de Cadastro

Na vida de um desenvolvedor e analista de sistemas, a validação de dados é uma etapa extremamente importante que previne diversas dificuldades posteriores à coleta dos dados.

Crie um programa com funções em Python para solicitar ao usuário que insira os dados listados abaixo e valide os seguintes campos de cadastro com as seguintes regras:

- **CPF**: Verifique se o CPF possui 11 dígitos e formate-o no padrão "xxx.xxx.xxx-xx".
- **E-mail**: Verifique se o e-mail possui um formato válido (com "@" e um domínio válido) e normalize-o para minúsculas. O e-mail deve conter caracteres alfanuméricos + '@' + caracteres alfanuméricos + '.' + caracteres alfabéticos.
- **Telefone**: Remova caracteres não numéricos e converta o número de telefone para uma string formatada como `(XX) XXXXX-XXXX` ou `(XX) XXXX-XXXX`, exibindo o número inteiro e a string formatada na tela.

---

# Mini Projeto 2: Análise de Dados de Vendas

Uma empresa de comércio eletrônico deseja analisar os dados de vendas para entender melhor o comportamento dos clientes e otimizar as estratégias de marketing.

Implemente um programa em Python que receba uma lista de transações, onde cada transação é representada por uma string no formato:

`ID_do_Produto,Nome_do_Produto,Quantidade,Valor_Unitário`

O programa deve:

1. Calcular e exibir o valor total das vendas para cada produto.
2. Criar uma função que receba a lista de transações e retorne:
   - O produto mais vendido (baseado na quantidade).
   - O produto que gerou a maior receita total.
3. Escrever um script que converta os valores totais de vendas para uma nova moeda, dado um fator de conversão fornecido pelo usuário, e exiba os valores convertidos no formato monetário adequado.

---

# Mini Projeto 3: Gerenciamento de Senhas

Um administrador de sistemas precisa desenvolver uma ferramenta para gerenciar senhas de usuários em uma rede corporativa.

Desenvolva um programa em Python com as seguintes funcionalidades:

1. **Geração de senhas seguras**: Desenvolva uma função que gera senhas aleatórias seguras, atendendo aos critérios:
   - Mínimo de 8 caracteres.
   - Inclui letras maiúsculas, minúsculas, números e caracteres especiais.
   
2. **Validação de senhas**: Implemente uma função que receba uma senha do usuário e verifique se ela atende aos critérios de segurança mencionados. Para cada senha que não atender aos critérios, sugerir uma senha nova.

3. **Criptografia de senhas**: Crie um programa que criptografa uma lista de senhas utilizando uma cifra de substituição (similar à cifra de César), considerando todos os caracteres imprimíveis da tabela ASCII, e armazene o resultado. Inclua uma função para descriptografar as senhas quando necessário.

---

# Mini Projeto 4: Processamento de Textos Jurídicos

Um escritório de advocacia deseja automatizar parte do processo de análise de contratos, extraindo informações relevantes de documentos longos.

Desenvolva um programa em Python que faça o seguinte:

1. **Extração de valores monetários**: Receba o texto completo de um contrato e extraia todas as cláusulas que mencionem valores monetários. Os valores devem ser identificados e exibidos em uma lista separada.

2. **Análise de termos legais**: Implemente uma função que, dada uma lista de termos legais, verifique quantas vezes cada termo aparece no contrato e exiba as ocorrências em ordem decrescente de frequência.
