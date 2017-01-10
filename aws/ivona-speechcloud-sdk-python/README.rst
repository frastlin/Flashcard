Ivona SpeechCloud SDK
-------------------------------------

This package can be used as a client to the Ivona cloud-based speech synthesis solution.

There are two methods supported at the moment:

- CreateSpeech - doing actual speech synthesis
- ListVoices - listing available voices with simple filtering

The package allows user to define his own classes for performing http requests so it makes it easy to plug it into existing codebase.

Please see samples package for example usages.


Please install mock==1.0.1 for being able to run tests.

Execute following command to run tests:

python -m unittest discover -s tests