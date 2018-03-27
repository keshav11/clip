import os
import argparse
from pathlib import Path

CLIP_FILE = os.path.join(Path.home(), '.clip')
TEMP_FILE = '.TEMP_FILE'

def add_command(key, command):
    if os.path.exists(CLIP_FILE):
        open_mode = 'a'
    else:
        open_mode = 'w+'
    with open(CLIP_FILE, open_mode) as clip_file:
        clip_file.write(key + ": " + command + "\n")


def list_commands():
    with open(CLIP_FILE, 'r') as clip_file:
        for command in clip_file.read().split('\n'):
            print(command)


def get_command(key):
    with open(CLIP_FILE, 'r') as clip_file:
        for command in clip_file.read().split('\n'):
            key_val = command.split(':')
            if key_val[0].strip() == key:
                print(key_val[1].strip())

def delete_command(key):
    with open(TEMP_FILE, 'w+') as temp_file:
        with open(CLIP_FILE, 'r') as clip_file:
            for command in clip_file.read().split('\n'):
                if command.strip() == "":
                    continue
                key_val = command.split(':')
                if key_val[0].strip() != key:
                    temp_file.write(command+"\n")
    try:
        os.rename(TEMP_FILE, CLIP_FILE)
    except Exception as ex:
        os.remove(TEMP_FILE)
        print('remove command failed.', ex)
        return


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='clip commands')
    parser.add_argument('-a', '--add', nargs=2)
    parser.add_argument('-g', '--get', nargs=1)
    parser.add_argument('-d', '--delete', nargs=1)
    parser.add_argument('-l', '--list', action='store_true')

    args = parser.parse_args()

    if args.add:
        add_command(args.add[0], args.add[1])
    elif args.list:
        list_commands()
    elif args.get:
        get_command(args.get[0])
    elif args.delete:
        delete_command(args.delete[0])
