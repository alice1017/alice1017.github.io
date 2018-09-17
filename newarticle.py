#!/usr/bin/env python
# coding: utf-8

import sys
from datetime import datetime

ARTICLE_TEMPLATE = """---
layout: post
title:
tags: []
excerpt_separator: <!--more-->
---

<!--more-->
"""


def generate_filename(uri):

    date = datetime.now().date()
    year = date.year
    month = date.month
    day = date.day

    return "_posts/{0}-{1}-{2}-{3}.md".format(
        year, month, day, uri.replace(" ", "-")
    )


def main():

    uri = raw_input("What your new article URI? > ")
    article_filename = generate_filename(uri)

    with open(article_filename, "w") as fp:
        fp.write(ARTICLE_TEMPLATE)

    print "Generated the new article: {0}".format(article_filename)
    return 0


if __name__ == '__main__':

    sys.exit(main())
