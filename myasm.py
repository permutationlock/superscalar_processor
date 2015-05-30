import sys

f = open(sys.argv[1],'r')

code = f.read()

token = code.split()

def toBin(x,width):
    return (str(bin(x))[2:])[:width].zfill(width)
    
def toHex(bits):
    print(bits)
    return hex(int(bits,2))[2:].zfill(2)

hexcommands = []
i=0
while i<len(token):
    print("i = "+str(i)+" token = "+str(token))
    if token[i]=='mov':
        i1 = token[i+1]
        i2 = token[i+2]
        opbits = toBin(0,3)
        if i1[:1]!='r':
            print('moving '+i2+' to non-register')
            break
        if i2[:1]=='r':
            cbit = '0'
            r1 = int(float(i1[-1:]))
            r1bits = toBin(r1,2)
            r2 = int(float(i2[-1:]))
            r2bits = toBin(r2,2)
            print(token[i]+' '+token[i+1]+' '+token[i+2])
            i+=3
            print(cbit+' '+opbits+' '+r2bits+' '+r1bits)
            hexcommands.append(toHex(cbit+opbits+r2bits+r1bits))
        else:
            cbit = '1'
            r1 = int(float(i1[-1:]))
            r1bits = toBin(r1,2)
            const = int(i2)
            shiftbit = '0'
            if const>15:
                const>>4
                shiftbit = '1'
            constbits = toBin(const,4)
            print(token[i]+' '+token[i+1]+' '+str(const))
            i+=3
            print(cbit+' '+shiftbit+' '+constbits+' '+r1bits)
            hexcommands.append(toHex(cbit+shiftbit+constbits+r1bits))
    elif token[i]=='add':
        i1 = token[i+1]
        i2 = token[i+2]
        opbits = toBin(1,3)
        if i1[:1]!='r' or i2[:1]!='r':
            print('adding non-registers')
            break
        else:
            cbit = '0'
            r1 = int(float(i1[-1:]))
            r1bits = toBin(r1,2)
            r2 = int(float(i2[-1:]))
            r2bits = toBin(r2,2)
            print(token[i]+' '+token[i+1]+' '+token[i+2])
            i+=3
            print(cbit+' '+opbits+' '+r2bits+' '+r1bits)
            hexcommands.append(toHex(cbit+opbits+r2bits+r1bits))
    elif token[i]=='sub':
        i1 = token[i+1]
        i2 = token[i+2]
        opbits = toBin(2,3)
        if i1[:1]!='r' or i2[:1]!='r':
            print('adding non-registers')
            break
        else:
            cbit = '0'
            r1 = int(float(i1[-1:]))
            r1bits = toBin(r1,2)
            r2 = int(float(i2[-1:]))
            r2bits = toBin(r2,2)
            print(token[i]+' '+token[i+1]+' '+token[i+2])
            i+=3
            print(cbit+' '+opbits+' '+r2bits+' '+r1bits)
            hexcommands.append(toHex(cbit+opbits+r2bits+r1bits))
    elif token[i]=='mul':
        i1 = token[i+1]
        i2 = token[i+2]
        opbits = toBin(4,3)
        if i1[:1]!='r' or i2[:1]!='r':
            print('adding non-registers')
            break
        else:
            cbit = '0'
            r1 = int(float(i1[-1:]))
            r1bits = toBin(r1,2)
            r2 = int(float(i2[-1:]))
            r2bits = toBin(r2,2)
            print(token[i]+' '+token[i+1]+' '+token[i+2])
            i+=3
            print(cbit+' '+opbits+' '+r2bits+' '+r1bits)
            hexcommands.append(toHex(cbit+opbits+r2bits+r1bits))
    elif token[i]=='div':
        i1 = token[i+1]
        i2 = token[i+2]
        opbits = toBin(2,3)
        if i1[:1]!='r' or i2[:1]!='r':
            print('adding non-registers')
            break
        else:
            cbit = '0'
            r1 = int(float(i1[-1:]))
            r1bits = toBin(r1,2)
            r2 = int(float(i2[-1:]))
            r2bits = toBin(r2,2)
            print(token[i]+' '+token[i+1]+' '+token[i+2])
            i+=3
            print(cbit+' '+opbits+' '+r2bits+' '+r1bits)
            hexcommands.append(toHex(cbit+opbits+r2bits+r1bits))
    else:
        print('Invalid Command!')
        break;

f = open(sys.argv[1]+".bits", 'w')
commands = ''
count = 0
for c in hexcommands:
    if count<4:
        commands=c+' '+commands
        count=count+1
    else:
        commands=c+'\n'+commands
        count=0
f.write(commands)
