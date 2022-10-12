with open('out.bin','wb') as file:
    for i in range(0,10):
        file.write(i.to_bytes(4,byteorder='little',signed=True))


    
