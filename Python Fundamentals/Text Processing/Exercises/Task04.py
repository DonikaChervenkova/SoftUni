encrypted_version = input()

final_version = ""
for letter in encrypted_version:
    final_version += chr(ord(letter) + 3)

print(final_version)