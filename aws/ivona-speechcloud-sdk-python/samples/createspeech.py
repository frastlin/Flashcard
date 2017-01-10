#coding: utf-8
"""Create speech example. It performs several request using GET and POST methods. There is an example of generating
direct URL as well.
"""

from ivonaspeechcloud.client import SpeechCloudClient
from ivonaspeechcloud.const import METHOD_GET, METHOD_POST, RES_HEADER_TTS_REQUEST_CHARACTERS, \
    RES_HEADER_TTS_REQUEST_ID, RES_HEADER_REQUEST_ID
from ivonaspeechcloud.inputs import Voice
from ivonacredentials import ACCESS_KEY, SECRET_KEY

LANGUAGE_DE = "de-DE"
LANGUAGE_EN = "en-GB"
LANGUAGE_PL = "pl-PL"

GERMAN_TEXT = "Ich bin glücklich."
ENGLISH_TEXT = "I am happy."
POLISH_TEXT = "Jestem szczęśliwy."

FILE_PATH_POST_DE = "tmp/speech_post_de.mp3"
FILE_PATH_POST_EN = "tmp/speech_post_en.mp3"
FILE_PATH_GET_PL = "tmp/speech_get_pl.mp3"


def sample_create_speech():
    client = SpeechCloudClient(ACCESS_KEY, SECRET_KEY)

    # GET request with language filtering (PL)
    res = client.create_speech(POLISH_TEXT, voice=Voice(language=LANGUAGE_PL), method=METHOD_GET)
    with open(FILE_PATH_GET_PL, "wb") as f:
        for chunk in res.chunks:
            f.write(chunk)

    # POST request with language filtering (DE)
    res = client.create_speech(GERMAN_TEXT, voice=Voice(language=LANGUAGE_DE),
                               method=METHOD_POST)
    # the method get direct url to the speech
    print ("REQ_URL", client.create_speech_url(GERMAN_TEXT, voice=Voice(language=LANGUAGE_DE)))
    with open(FILE_PATH_POST_DE, 'wb') as f:
        for chunk in res.chunks:
            f.write(chunk)

    # POST request with language filtering (EN)
    res = client.create_speech(ENGLISH_TEXT, voice=Voice(language=LANGUAGE_EN),
                               method=METHOD_POST)
    with open(FILE_PATH_POST_EN, 'wb') as f:
        for chunk in res.chunks:
            f.write(chunk)

    print("RESPONSE INFO FOR THE LAST REQUEST: ")
    print("\tCHARACTERS USED: " + res.headers[RES_HEADER_TTS_REQUEST_CHARACTERS])
    print("\tTTS REQUEST ID: " + res.headers[RES_HEADER_TTS_REQUEST_ID])
    print("\tREQUEST ID" + res.headers[RES_HEADER_REQUEST_ID])


if __name__ == "__main__":
    sample_create_speech()
