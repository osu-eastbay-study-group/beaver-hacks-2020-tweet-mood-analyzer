from urllib import parse
import requests
import json


class ToneAnalyzer:
    """Class to analyze the Tone of a given string. Uses the IMB Watson
    Tone Analyzer API https://www.ibm.com/watson/services/tone-analyzer/
    to perform tone analysis. Works with a single API key/URL pair."""

    # CLASS CONSTANTS
    # ---------------
    # Specific to using general-purpose endpoint via the GET request method.
    _GET_METHOD_URL = '/v3/tone?version=2017-09-21&text='

    def __init__(self, api_key, api_url):
        """Create object of type ToneAnalyzer for a specific API key and URL
        pair.

        Parameters
        ----------
        api_key: str
            API key from https://www.cloud.ibm.com.
        api_url: str
            API URL from https://www.cloud.ibm.com.
        """
        self._api_key = api_key
        self._api_url = api_url
        self._saved_tones = {}  # keys: strings, values: tone dict for string

    def analyze_tone(self, text):
        if text not in self._saved_tones:
            self._save_tone(text)
        return self._saved_tones[text]

    def _save_tone(self, text):
        encoded_text = urllib.parse.quote(text)
        request_url = f'{self._api_url}{self._GET_METHOD_URL}{encoded_text}'
        response = requests.get(request_url, auth=('apikey', api_key))
        tone = json.loads(response.content.decode())
        self._saved_tones[text] = tone
