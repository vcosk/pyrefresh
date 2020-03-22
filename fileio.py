with open('mydata.txt', mode='w', encoding='utf-8') as myFile:
    myFile.write('This my text\n')

with open('mydata.txt', mode='r', encoding='utf-8') as myFile:
    print(myFile.read())

