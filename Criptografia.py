from cryptography.fernet import Fernet 

print("Codificador de mensagens:") 
while True: 
  modo = str(input("Digite 1 para criptografar e 2 para descriptografar: ")) 
   if(modo == '1'): 
     key = Fernet.generate_key() 
     f = Fernet(key) 
     mensagem = (str(input("Digite a mensagem a ser criptografada: "))) 
     b = bytes(mensagem, 'utf-8') 
     token = f.encrypt(b) 
     print(token) 
     chave = (str(input("Digite 1 para ver a chave ou qualquer tecla para continuar: 
 "))) 
   if(chave == '1'): 
     print("Mantenha a chave em um lugar seguro, pois sem ela a descriptografia 
     da mensagem não será possivel!") 
     print(key) 
     if(modo == '2'): 
     key = str(input('Digite a chave para descriptografar: ')) 
     f = Fernet(key) 
     mensagem = str(input("Digite a mensagem a ser descriptografada: ")) 
     b = bytes(mensagem, 'utf-8') 
    token = f.decrypt(b) 
     print(token) 
   if(modo != '1') and (modo != '2'): 
    print('Erro, digite um modo válido.') 
 saida = str(input("Digite 1 para sair, ou qualquer tecla para continuar: "))
