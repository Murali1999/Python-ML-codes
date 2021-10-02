#encrypt a message and decrypt it

global pt,k,m #plaintext, key and message
m = input("Enter message - ") #message
k = int(input("Enter key - ")) #key
alp = 'abcdefghijklmnopqrstuvwxyz' #list of alphabets
pt,ct,x='','',0 #plaintext and ciphertext

for i in range(len(m)):
    for j in range(len(alp)):
        if(m[i] in alp[j]):
            x=(alp.index(m[i]))%26
            x=x+k
            ct=ct+alp[x]

print("Cipher text -",ct)
            
for i in range(len(ct)):
    for j in range(len(alp)):
        if(ct[i] in alp[j]):
            x=(alp.index(ct[i]))%26
            x=x-k
            pt=pt+alp[x]
        
print("Plain text -",pt)
