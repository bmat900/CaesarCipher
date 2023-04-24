print("Welcome to the Caesar Cipher encrypt!")
cipher = input("Type 'encode' to encrypt, or type 'decode' to decrypt.\n")
message = input("Type your message:\n").lower()
num_encryp = int(input(f"Type the shift number between 1 and 26:\n"))

# Se quiser adicionar characters para uma criptografia maior, pode adicionar aqui.
letters_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z', ' ']
message_list = list(message)


# Encontra a posição de uma letra da mensagem no abecedario.
def position_letter(list_m, list_l):
    for j in range(0, len(list_l)):
        if list_m == list_l[j]:
            return j


# Verifica se a nova posição desejada do abecedario (criptografada) não supera a quantidade de letras, no caso,
# retorna a nova posição.
def check_range_encrypt(list_l, position, num_enc):
    if len(list_l) - 1 < (position + num_enc):
        i = position + num_enc - len(list_l)
        return i
    else:
        return (position + num_enc)


# Devolve a posição decriptografado das letras da mensagem.
def check_range_decrypt(position, num_enc):
    return position - num_enc


# Criptografa a mensagem com variabilidade na quantidade de posições desejada no abecedario.
def encode(mensagem, abecedario, num_enc):
    lista_crip = []
    for i in range(0, len(mensagem)):
        j = check_range_encrypt(abecedario, position_letter(mensagem[i], abecedario), num_enc)
        lista_crip.append(abecedario[j])
    palavra_crip = "".join(lista_crip)
    return palavra_crip


# Decriptografa a mensagem com variabilidade na quantidade de posições na qual foi realizada a criptografia.
def decode(mensagem, abecedario, num_enc):
    lista_crip = []
    for i in range(0, len(mensagem)):
        x = check_range_decrypt(position_letter(mensagem[i], abecedario), num_enc)
        lista_crip.append(abecedario[x])
    palavra_crip = "".join(lista_crip)
    return palavra_crip

# Basicamente este é o programa... =)
if 1 <= num_encryp <= 26:
    if cipher == 'encode':
        palavra = encode(message_list, letters_list, num_encryp)
        print(f'The message encode is: \n{palavra}')
    elif cipher == 'decode':
        palavra = decode(message_list, letters_list, num_encryp)
        print(f'The message decode is: \n{palavra}')
    else:
        print('Invalid input encode or decode.')
else:
    print('Invalid input shift number.')


