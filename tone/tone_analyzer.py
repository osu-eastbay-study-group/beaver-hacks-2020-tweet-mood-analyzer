import urllib
import requests
import json
import os.path


class ToneAnalyzer:
    """Class to analyze the Tone of a given string. Uses the IMB Watson
    Tone Analyzer API https://www.ibm.com/watson/services/tone-analyzer/
    to perform tone analysis. Works with a single API key/URL pair."""

    # CLASS CONSTANTS
    # ---------------
    # Specific to using general-purpose endpoint via the GET request method.
    _GET_METHOD_URL = '/v3/tone?version=2017-09-21&text='
    # Default name of JSON file to store tones.
    _DEFAULT_JSON_FILENAME = 'tones.json'

    def __init__(self, api_key, api_url, json_file=None):
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

        # TODO: Write exception class for filename validation.
        if json_file is not None:
            assert type(json_file) == str, "Provided filename is not a string!"

        self._json_file = (json_file if json_file is not None
                           else self._DEFAULT_JSON_FILENAME)

        # keys: strings, values: tone dict for string
        self._saved_tones = (self.load_tones_from_file()
                             if os.path.exists(self._json_file) else {})


    def analyze_tone(self, text):
        """Returns the tone analysis data of supplied text and stores it to reduce
        number of calls to API. If the text was already saved, returns existing
        data.

        Post-Conditions
        ---------------
        text' will be a key in `_saved_tones' with its tone analysis dictionary
        as its corresponding value.

        Parameters
        ----------
        text: str
            Text to analyze.

        Returns
        -------
        dict
            Tone analysis of the text.
        """
        if text not in self._saved_tones:
            self._save_tone(text)
        return self._saved_tones[text]

    def _save_tone(self, text):
        """Helper method.

        Calls the API on `text' and saves result to `_saved_tones'.

        Pre-conditions
        --------------
        `text' must not be a key of _saved_tones. In otherwords this should
        only call the API on text that has not yet been analyzed.

        Post-conditions
        ---------------
        `text' will be a key of _saved_tones with value equal to the
        corresponding tone dict.

        Parameters
        ----------
        text: str
            Text to perform tone analysis.

        Returns
        -------
        None
        """
        encoded_text = urllib.parse.quote(text)
        request_url = f'{self._api_url}{self._GET_METHOD_URL}{encoded_text}'
        response = requests.get(request_url, auth=('apikey', api_key))
        tone = json.loads(response.content.decode())
        self._saved_tones[text] = tone

    def save_tones_to_file(self, filename=None):
        out_filename = self._json_file if filename is None else filename
        with open(out_filename, 'w') as outfile:
            json.dump(self._saved_tones, outfile)

    def load_tones_from_file(self, filename=None):
        in_filename = self._json_file if filename is None else filename
        try:
            with open(in_filename, 'r') as infile:
                return json.load(infile)
        except FileNotFoundError:  # trying to open non-existent file
            print("Tone file does not exist. "
                  + f"All new tones will be saved to {self._json_file}.")
