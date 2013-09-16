#!/usr/bin/python

import sys
from fetcher import WBDataFetcher
from fetcher import Loader, CachingLoader
from fetcher import PostProcessor

USAGE_MESSAGE = '''You missed something:)
Usage: python fetch.py <country> <indicator>
Available indicators:
%s
'''

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print USAGE_MESSAGE % WBDataFetcher.get_available_indicators()
    else:
        loader = CachingLoader()
        pproc = PostProcessor()
        datafetcher = WBDataFetcher(loader, pproc)
        print datafetcher.fetch(sys.argv[1], sys.argv[2])