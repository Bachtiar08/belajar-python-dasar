print('========= Operator Logika/Boolean =========')
print()
 
print('# And (and): dibahasa pemrograman lain biasanya dengan simbol &&')
print('# Operator and hanya akan menghasilkan True jika semua operannya True, sisanya pasti False')
a = True and True and True
print('a:', a)
b = False and True
print('b:', b)
print('False and False:', False and False)
print('True and False:', True and False)
print('True and True:', True and True)
print('1 > 2 and 1 == 1:', 1 > 2 and 1 == 1)
print()
 
print('# Or (or): dibahasa pemrograman lain biasanya dengan simbol ||')
print('# Operator or hanya akan menghasilkan False jika semua operannya False, sisanya pasti True')
a = True or False or True
print('a:', a)
b = False or False or False or False or False or False or True
print('b:', b)
print('False or False:', False or False)
print('True or False:', True or False)
print('True or True:', True or True)
print('1 > 2 or 1 == 1:', 1 > 2 or 1 == 1)
print()
 
# print('# Not (not)')
# print('# XOr (Xor)')