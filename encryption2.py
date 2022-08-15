# This is the link to this Python Coding Challenge
# https://www.codewars.com/kata/526d42b6526963598d0004db/train/python
alphabet = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz';
def ceasar(start_text = input('Type in any word:\n'), shift_amount = int(input('Type a number from 1 to 26:\n')), cipher_direction  = input('Type encode or decode:\n')):
    str = ''
    for i in start_text:
        if cipher_direction == 'decode':
            pos = alphabet.index(i)
            new_pos = pos - shift_amount
            str += alphabet[new_pos]
        elif cipher_direction == 'encode':
            pos = alphabet.index(i)
            new_pos = pos + shift_amount
            str += alphabet[new_pos]
        else:
            print('Invalid Choice.  Only type encode or decode')
            break
    print(str)
ceasar()

# alphabet = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz';
# def ceasar(start_text = input('Type in any word:\n'), shift_amount = int(input('Type a number from 1 to 26:\n')), cipher_direction  = input('Type encode or decode:\n')):
#     print(start_text)
#     print(shift_amount, type(shift_amount))
#     print(cipher_direction)
#     str = ''
#     for i in start_text:
#         # print(alphabet.index(i))
#         if cipher_direction == 'decode':
#             pos = alphabet.index(i)
#             # print(pos)
#             new_pos = pos - shift_amount
#             print(pos, new_pos)
#             print(alphabet[new_pos])
#             str += alphabet[new_pos]
#         elif cipher_direction == 'encode':
#             pos = alphabet.index(i)
#             # print(pos)
#             new_pos = pos + shift_amount
#             # print(pos, new_pos)
#             print(alphabet[new_pos])
#             str += alphabet[new_pos]
#         else:
#             print('Invalid Choice.  Only type encode or decode')
#             break
#     print(str)
# ceasar()

# This is the link to this Python Coding Challenge
# https://www.codewars.com/kata/526d42b6526963598d0004db/train/python
# alphabet = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz';
# def ceasar(start_text = input('Type in any word:\n'), shift_amount = int(input('Type a number from 1 to 26:\n')), cipher_direction  = input('Type encode or decode:\n')):
#     str = ''
#     for i in start_text:
#         print(i)
#         if cipher_direction == 'decode':
#             if i in alphabet:
#                 pos = alphabet.index(i)
#                 new_pos = pos - shift_amount
#                 str += alphabet[new_pos]
#             else:
#                 str += i
#         elif cipher_direction == 'encode':
#             if i in alphabet:
#                 pos = alphabet.index(i)
#                 new_pos = pos + shift_amount
#                 str += alphabet[new_pos]
#             else:
#                 str += i
#         else:
#             print('Invalid Choice.  Only type encode or decode')
#             break
#     print(str)
# ceasar()
