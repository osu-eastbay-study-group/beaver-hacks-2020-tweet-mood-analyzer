import requests
import json
import html
import urllib


class OEmbedFinder:
    OEMBED_LINK = 'https://publish.twitter.com/oembed'

    @staticmethod
    def get_oembed(tweet_link):
        """Get the data of a Twitter oEmbed in the form of a dict.

        Also unquotes the HTML code before returning the oEmbed dict.

        Parameters
        ----------
        tweet_link: str
            Standard hyperlink of a tweet.

        Returns
        -------
        dict
            Data associated with the oEmbed.
        """
        response = requests.get(OEmbedFinder.OEMBED_LINK,
                                params=(('url', tweet_link),))
        oembed = json.loads(response.content.decode())

        # Process the 'html' to plain text without any escapes.
        oembed['html'] = urllib.parse.unquote(oembed['html'])

        # TODO: Remove remaining '\n' after </blockquote> and </script>.

        return oembed


if __name__ == '__main__':
    # Example usage
    tweet_link = 'https://twitter.com/RegexCrossword/status/1185017497482719233'
    oembed = OEmbedFinder.get_oembed(tweet_link)

    # Print the embedded HTML
    print(html.unescape(oembed['html']))  # Doesn't quite unescape it.
