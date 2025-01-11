# Did encryption of the message manually
print("Enter whether the message is to be encrypted or decrypted")

x=input("E for encryption, D for Decryption: ")
y=x.lower()

if y=='e':
    i=input("Enter the text to be encrypted: ")
    a=i.lower()
    b=a.replace('a','`').replace('b','~').replace('c','!').replace('d','@').replace('e','#').replace('f','$').replace('g','%').replace('h','^').replace('i','&').replace('j','*').replace('k','<').replace('l','>').replace('m','{').replace('n','=').replace('o','l').replace('p','k').replace('q','j').replace('r','i').replace('s','h').replace('t','g').replace('u','f').replace('v','e').replace('w','d').replace('x','c').replace('y','b').replace('z','a').replace('0','+').replace('1','-').replace('2','_').replace('3','|').replace('4','}').replace('5','3').replace('6','4').replace('7','1').replace('8','2').replace('9','0')
    print("Message encrypted successfully!",'\n','\n','Encrypted Message: ',b)

elif y=='d':
    i=input("Enter the text to be decrypted: ")
    a=i.lower()
    b=a.replace('l','o').replace('k','p').replace('j','q').replace('i','r').replace('h','s').replace('g','t').replace('f','u').replace('e','v').replace('d','w',).replace('c','x').replace('b','y',).replace('a','z').replace('`','a').replace('~','b').replace('!','c').replace('@','d').replace('#','e').replace('$','f',).replace('%','g',).replace('^','h').replace('&','i',).replace('*','j').replace('<','k').replace('>','l').replace('{','m').replace('=','n').replace('3','5').replace('4','6',).replace('1','7').replace('2','8').replace('0','9').replace('+','0').replace('-','1').replace('_','2').replace('|','3').replace('}','4')
    print("Message decrypted successfully!",'\n','\n','Decrypted Message: ',b)
else:
    print("(Error_0001) Enter the valid literal !!")