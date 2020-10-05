#!/usr/bin/python

import glob
import json
import re
import string

def main():
    icons = glob.glob("./material-design-icons/*/1x_web/ic_*_black_48dp.png")
    res = []
    for icon in icons:
        uid = re.search('ic_([a-z0-9_]+)_black_48dp.png', icon).group(1)
        title = string.replace(uid, "_", " ")
        subtitle = re.search('/([a-z]+)/1x_web', icon).group(1)
        res.append((icon, uid, title, subtitle))
    print json.dumps({'items': [{'uid': uid, 'title': title, 'subtitle': subtitle, 'arg': uid, 'icon': {'path': icon}} for icon, uid, title, subtitle in res]})

if __name__ == '__main__':
    main()
