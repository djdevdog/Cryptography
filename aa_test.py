from cipers import CaesarCiper, AtbashCiper
string = 'hello'

# Atbash Test
encrypted_str = AtbashCiper.encrypt(string)
print(encrypted_str)

decrypted_str = AtbashCiper.decrypt(encrypted_str)
print(decrypted_str)


# Cesaer Test
encrypted_str = CaesarCiper.encrypt(string, 5)
print(encrypted_str)

decrypted_str = CaesarCiper.decrypt(encrypted_str, 5)
print(decrypted_str)