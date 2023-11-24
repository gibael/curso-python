#primeiro 
"""
if len(input()) > 140:
    print('MUTE')
else:
    print('TWEET')
"""

#segundo

""" month = input()

months_dict = {
  "1":"January",
  "2":"February",
  "3":"March",
  "4":"April",
  "5":"May",
  "6":"June",
  "7":"July",
  "8":"August",
  "9":"September",
  "10":"October",
  "11":"November",
  "12":"December"

}

print(months_dict[month])
"""


n = int(input())  # Quantidade de casos de teste

i = 0
while i < n:
    A, B = input().split()

    if len(A) < len(B):
        print("nao encaixa")
    else:
        if A[-len(B):] == B:
            print("encaixa")
        else:
            print("nao encaixa")

    i += 1