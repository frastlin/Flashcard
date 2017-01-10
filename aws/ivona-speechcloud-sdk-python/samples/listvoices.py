#coding: utf-8
"""ListVoices example. There is an example to get german and polish voices and a direct URL.
"""

from ivonaspeechcloud.client import SpeechCloudClient
from ivonaspeechcloud.const import METHOD_GET, METHOD_POST
from ivonaspeechcloud.inputs import Voice
from ivonacredentials import ACCESS_KEY, SECRET_KEY

LANGUAGE_DE = "de-DE"
LANGUAGE_PL = "pl-PL"


def sample_list_voices():
    client = SpeechCloudClient(ACCESS_KEY, SECRET_KEY)

    res = client.list_voices(voice=Voice(language=LANGUAGE_PL), method=METHOD_GET)
    print(res.json)

    res = client.list_voices(voice=Voice(language=LANGUAGE_DE), method=METHOD_POST)
    print(res.json)

    print(client.list_voices_url(voice=Voice(language=LANGUAGE_PL)))


if __name__ == "__main__":
    sample_list_voices()
