#   PyPI Dependencies: requests
# Usage (commandline): $ python tone_analyzer.py https://twitter.com/RegexCrossword/status/<tweet-num>

import requests
import json
import urllib
import sys


class OembedFinder:
    """Class to handle calls to Twitter oEmbedded API. SHOULD NOT BE
    INSTANTIATED as contains only static methods."""

    OEMBED_LINK = 'https://publish.twitter.com/oembed'

    @staticmethod
    def get_oembed(tweet_link):
        """Get the data of a Twitter oembed in the form of a dict.

        Also unquotes the HTML code before returning the oembed dict.

        Parameters
        ----------
        tweet_link: str
            Standard hyperlink of a tweet.

        Returns
        -------
        dict
            Data associated with the oembed.
        """

        # TODO: Add input validation for tweet_link?

        response = requests.get(OembedFinder.OEMBED_LINK,
                                params=(('url', tweet_link),))
        oembed = json.loads(response.content.decode())

        # Process the 'html' to plain text without any escapes.
        oembed['html'] = urllib.parse.unquote(oembed['html'])

        # TODO: Remove remaining '\n' after </blockquote> and </script>.

        return oembed


if __name__ == '__main__':
    # Command line usage:
    # python oembed.py https://www.your-passed-site-here.com

    # For usage in IDE/Editor
    # -------------------------
    # url_base = 'https://twitter.com/RegexCrossword/status/'
    # url_num = '1185017497482719233'
    # tweet_link = url_base + url_num

    # For usage as command line script
    # --------------------------------
    tweet_link = sys.argv[1]

    # -----------------------------------------------------------------------------
    # Print the data of the specified oembed.
    oembed_data = OembedFinder.get_oembed(tweet_link)

    # Print the oembed Data
    for key, val in oembed_data.items():
        print(f'\n{key}:\n', repr(f'{val}'), sep='')
