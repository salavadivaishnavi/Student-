n=int(input().strip())
no_bits=n.bit_length()
set_num=(1 << no_bits)-1
print(set_num)
