singleQuote = 'Single quote string \' \" \\'
print(singleQuote)

doubleQuote = 'Same as single quote string \' \" \\'
print(doubleQuote)

tripleQuotes = '''Triple quotes ' " \"
Hello '''
print(tripleQuotes)

# ignoring escape sequences
# When a string is enclosed within double quotes, double quote can't be used without printing escape charecter
print(r"I'll \' \" be ignored \n")

print('Hello' + ' World')

print ('Length: %d'%len('Impana'))

# Indexing from start
print('First %s'%'Impana'[0])

# Indexing from the end
print('Last %s'%'Impana'[-1])

# Indexing a range
print('Last %s'%'Impana'[0:4])

# Indexing a range with skipping intervel
print('Last %s'%'Impana'[0:4:2])

# Strings are immutable
# Error str = "Impana"; str[0] = 'V'
str = 'Impana'.replace('Im', 'Sha')
print(str)

# Test for string in a string
print('mp' in 'Impana')
print('mp' not in 'Impana')
print('Impana'.find('v'))
print('A'+' Impana '.lstrip()+'A')
print('A'+' Impana '.rstrip()+'A')
print('A'+' Impana '.strip()+'A')

print('A'.join(['V','I','K']))

name = 'V' # input()

print(f"Hello {name}")
print("Hello {name}".format(name=name))

print('I,m,p,a,n,a'.split(','))

print('Is a'.isalnum())
print('Isa'.isalnum())
print('Is a'.isalpha())
print('Isa'.isalpha())
print('Is a'.isdigit())
print('123'.isdigit())
print('12.3'.isdigit())
print('12.3'.isdecimal())
print('3'.isdecimal())