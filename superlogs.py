from __future__ import print_function
import re
from os.path import isfile
from sys import stdin, stderr, version_info
import codecs

__version__ = '1.0'
stop_seq = u'</body></xfmf>$'
stop = re.compile(stop_seq)


def streams(filenames, stdin_if_empty=True):
    if filenames:
        for fname in filenames:
            if isfile(fname):
                with open(fname, 'rb') as f:
                    yield f
    elif stdin_if_empty:
        yield stdin


def records(stream):
    buf = u''

    for l in stream:
        if not isinstance(l, str) or version_info < (3,0) :
            l = l.decode('utf-8', errors='replace')
        buf += l
        if stop.search(l):
            yield buf
            buf = u''


def version():
    return 'supertools v. %s (c) AkondLab' % __version__


def info(*args, **kwargs):
    kwargs['file'] = stderr
    print (*args, **kwargs)
