
#!/usr/bin/env python3

# -*- coding: utf-8 -*-

import requests

from bs4 import BeautifulSoup


def content ( site: str ) -> list :

    if not site.startswith ( 'https://' ) :

        site = 'https://' + site

    resp = requests.get ( site )

    if resp.status_code != 200 :

        print ( '\nError - Uri\n' )

        exit ( 1 )

    soup = BeautifulSoup ( resp.text, 'html5lib' )

    soup = soup.find_all ( 'a', attrs = { 'class': 'question-hyperlink' } )

    links = list ()

    for title in soup :

        links.append ( '<a href = "https://pt.stackoverflow.com{0}" target = "_blank" title = "{1}">{1}</a>' \
                    .format ( title ['href'], title.contents [0] ) )

    return links


def page ( site: str ) -> None :

    tag = '\n\n\t\t\t\t\t'.join ( content ( site ) )

    with open ( 'Stack.html', 'w' ) as arch :

        cmd = '''<!DOCTYPE html>

        <html lang = "pt-br">

            <head>

                <meta charset = "utf-8">

                <title>Stack Over Flow</title>

                <meta name = "description" content = "Trending of Stack Over Flow">

                <link rel = "stylesheet" href = "Flow.css"/>

            </head>

            <body>

                <nav>

                    <a title = "Stf"><img src = "http://i.imgur.com/epc4MwU.png" alt = "Stf" style = "width: 3em; height: 3em;"></a>

                    {tags}

                </nav>

            </body>

        <html>'''.format ( tags = tag )

        arch.write ( str ( cmd ) )


# page ( 'https://pt.stackoverflow.com/?tab=featured' )

page ( 'https://stackoverflow.com/?tab=featured' )
