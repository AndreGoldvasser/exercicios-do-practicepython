# Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a
# mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating
# a new password every time the user asks for a new password. Include your run-time code in a main method.
import secrets
import string
import time


def main():
    print(f'A senha gerada: {gera_senha()}')
    print(f'Tempo de execução: {time.process_time()}s')


def gera_senha():
    return str(''.join(secrets.choice(string.ascii_letters + string.digits + string.punctuation) for x in range(15)))


if __name__ == '__main__':
    main()
