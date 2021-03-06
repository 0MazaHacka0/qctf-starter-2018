import random
import sys
import json
import string

SEED = 412
LOGIN_LENGTH = 8
PASSWORD_LENGTH = 10
DIRECTORY_NAME_LENGTH = 10
FLAG_PATTERN = 'QCTF{{VALIDATE_USER_DATA_{}}}'
FLAG_SUFFIX_LEN = 10

def get_rand_str(rand, l):
    return ''.join([rand.choice(string.ascii_lowercase) for _ in range(l)])

def generate_flag(rand):
    return FLAG_PATTERN.format(''.join([rand.choice(string.ascii_uppercase) for _ in range(FLAG_SUFFIX_LEN)]))

def generate_user(rand):
    login = get_rand_str(rand, LOGIN_LENGTH)
    password = get_rand_str(rand, PASSWORD_LENGTH)
    directory = get_rand_str(rand, DIRECTORY_NAME_LENGTH)
    flag = generate_flag(rand)
    return {'login': login, 'password': password, 'directory': directory, 'flag': flag}

def main():
    if len(sys.argv) < 2:
        print('Usage: {} number-of-users'.format(sys.argv[0]))
        return
    
    n = int(sys.argv[1])
    rand = random.Random(SEED)

    used_logins = set()
    users = []
    for i in range(n):
        user = None
        while user is None or user['login'] in used_logins:
            user = generate_user(rand)
        used_logins.add(user['login'])
        users.append(user)

    print(json.dumps(users, indent=4))

if __name__ == '__main__':
    main()
