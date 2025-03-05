import random
import string
from cryptography.hazmat.primitives import hashes
import binascii
letras_maiusculas = string.ascii_uppercase
letras_minusculas = string.ascii_lowercase
caracteres_espec = string.punctuation
numeros = string.digits
caracteres = ""
if input("Você irá querer caracteres maiuscúlos(s/n):").lower() == "s":
    caracteres += letras_maiusculas
if input("Você irá querer caracteres especiais?(s/n):").lower() == "s":
    caracteres += caracteres_espec
if input("Incluir números?(s/n):").lower() == "s":
    caracteres += numeros
if not caracteres:
    print("Nenhum caracter foi escolhido,usando apenas letras minusculas")
caracteres += letras_minusculas
tamanho = int(input("Digite o tamanho da senha:"))
senha = "".join(random.choice(caracteres) for i in range(tamanho))
senha_byte = senha.encode()
senhas = [senha]
digest = hashes.Hash(hashes.SHA256())
digest.update(senha_byte)
hash_final = digest.finalize()
senha_hex = (binascii.hexlify(hash_final).decode())
list_hex = [senha_hex]
with open("Senhas.txt","a") as arquivo:
    for s in list_hex:
        arquivo.write(s + "\n")