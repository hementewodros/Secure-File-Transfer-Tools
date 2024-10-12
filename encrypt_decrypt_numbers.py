enc_Key = tuple(map(int, input("Encryption Key in the form of (e, En): ").strip('()').split(',')))
enc_no=int(input("Number that you want to encrypt/decrypt: "))
print((enc_no**enc_Key[0])%enc_Key[1])

