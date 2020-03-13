#!/usr/bin/env python3
from bs4 import BeautifulSoup

import requests
import os


def get_story_links():
    page = None
    with open( "examples/list-of-works.html" ) as file:
        html = file.read()
        page = BeautifulSoup( html, "html.parser" )

    links = page.find_all( "a", href = True )

    story_links = { }
    for link in links:
        if (link[ 'href' ].startswith( "fiction" )):
            story = link.text
            href = link[ 'href' ]

            story_links[ story ] = href

    return story_links


def get_story_text( link ):
    pass


def extract_title( link ):
    pass


if __name__ == '__main__':
    story_links = get_story_links()

    for sl in story_links:
        print( story_links[ sl ] )

# for link in story_links:
#     title = extract_title( link )
#     text = get_story_text( link )