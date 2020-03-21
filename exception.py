while True:
    try:
        number = int(input('Enter a number: '))
        break
    except ValueError:
        print('Enter a number')
    except:
        print('Unknown Error')

print('Ty')