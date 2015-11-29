#!/usr/bin/env python

import sys
import os


def lines2dict(lines):
    items = {}
    for n in lines:
        items[n.split('=')[0].split()[1]] = n.split()[2][:-1]
    return items

def print_items(items):
    for thing, thing2 in items.iteritems():
        print "{}\t\t{}".format(thing, thing2)

def main(args):
    #use with 'lzchris shortcut'
    if len(args) < 1:
        raise ValueError("You goofed. Usage: `lzchris shortcut`")

    if args[0] in ['-r', 'remove', '--remove']:
        needs_refresh = False
        with open(os.path.expanduser('~/.lzchris'), 'r') as fh:
            items = lines2dict(fh.readlines())
            if args[1] in items:
                del items[args[1]]
                needs_refresh = True
        if needs_refresh:
            with open(os.path.expanduser('~/.lzchris'), 'w') as fw:
                for shortcut, directory in items.iteritems():
                    fw.write('alias {}="cd {}"\n'.format(shortcut, directory))


    elif args[0] in ['-l', 'list', '--list']:
        with open(os.path.expanduser('~/.lzchris'), 'r') as fh:
            items = lines2dict(fh.readlines())
            print_items(items)

    else:
        shortcut = args[0]

        if len(args) > 1:
            directory = os.path.expanduser(args[1])
        else:
            directory = os.getcwd()

        with open(os.path.expanduser('~/.lzchris'), 'a+') as fh:
            fh.write('alias {}="cd {}"\n'.format(shortcut, directory))


if __name__ == '__main__':
    main(sys.argv[1:])
