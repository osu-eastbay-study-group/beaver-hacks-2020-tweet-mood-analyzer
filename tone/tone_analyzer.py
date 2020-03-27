from urllib import parse
import requests
import json


class ToneAnalyzer:
    """Class to analyze the Tone of a given string. Uses the IMB Watson
    Tone Analyzer API https://www.ibm.com/watson/services/tone-analyzer/
    to perform tone analysis. Works with a single API key/URL pair."""

    def __init__(self, api_key, api_url):
        """
        Create object of type ToneAnalyzer for a specific API key and URL pair.
        """
        self._api_key = api_key
        self._api_key = api_url
        self._saved_tones = {}  # keys: strings, values: tone dict for string
