# ssml-builder

## Installation

```
pip install ssml-builder
```

## Usage

1. Create a Speech object

```
from ssml_builder.core import Speech
speech = Speech()
```

2. Add text and tags to the Speech object

```
# add text
speech.say("hello world")
# add pause tag
speech.pause("10s")
# add prosody tag
speech.prosody("hello world", x-fast")
```

3. Return the the Speech object
```
speech.speak()
```


