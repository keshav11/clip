import os
import argparse
from pathlib import Path

CLIP_FILE = os.path.join(Path.home(), '.clip')
TEMP_FILE = '.TEMP_FILE'


def add_text(key, text):
    if os.path.exists(CLIP_FILE):
        open_mode = 'a'
    else:
        open_mode = 'w+'
    with open(CLIP_FILE, open_mode) as clip_file:
        clip_file.write(key + ": " + text + "\n")


def list_texts():
    with open(CLIP_FILE, 'r') as clip_file:
        for text in clip_file.read().split('\n'):
            print(text)


def get_text(key):
    with open(CLIP_FILE, 'r') as clip_file:
        for text in clip_file.read().split('\n'):
            key_val = text.split(':')
            if key_val[0].strip() == key:
                print(key_val[1].strip(), end='')


def delete_text(key):
    exists = False
    with open(TEMP_FILE, 'w+') as temp_file:
        with open(CLIP_FILE, 'r') as clip_file:
            for text in clip_file.read().split('\n'):
                if text.strip() == "":
                    continue
                key_val = text.split(':')
                if key_val[0].strip() != key:
                    temp_file.write(text+"\n")
                else:
                    exists = True
    if not exists:
        print("key:", key, "was not found in the clip store")
    try:
        os.rename(TEMP_FILE, CLIP_FILE)
    except Exception as ex:
        os.remove(TEMP_FILE)
        print('remove text failed.', ex)


def main():
    parser = argparse.ArgumentParser(description='clips and saves texts from the command line')
    parser.add_argument('-a', '--add', nargs=2)
    parser.add_argument('-g', '--get', nargs=1)
    parser.add_argument('-d', '--delete', nargs=1)
    parser.add_argument('-l', '--list', action='store_true')

    args = parser.parse_args()

    if args.add:
        key, value = args.add[0], args.add[1]
        add_text(key, value)
    elif args.list:
        list_texts()
    elif args.get:
        key = args.get[0]
        get_text(key)
    elif args.delete:
        key = args.delete[0]
        delete_text(key)
    else:
        parser.print_usage()


if __name__ == '__main__':
    main()
