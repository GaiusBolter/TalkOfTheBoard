######################################################
#                                                    #
#       TalkOfTheBoard - 0.0.1                       #
#                                                    #
#       by:     Splendid                             #
#                                                    #
#                                                    #
######################################################

from urllib.request import urlopen


def connected(url="http://duckduckgo.com"):
    try:
        urlopen(url)
        return True
    except:
        return False


def boardUp(boardURL):
    try:
        urlopen(boardURL)
        return True
    except:
        return False