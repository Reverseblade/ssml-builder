# ssml-builder

## Installation

```
pip install ssml-builder
```

## Usage
- Create Speech Object

```buildoutcfg
from ssml_builder.core import Speech

speech = Speech()
```

- Add text
```buildoutcfg
speech.add_text('sample text')
```

- Generate SSML
```buildoutcfg
speech.speak()
```

## Features
- This package supports the following SSML tags.
    - say_as
    - prosody
    - sub
    - lang
    - voice
    - pause
    - whisper
    - audio
    - emphasis
    - p

## Tag Examples
#### say_as
```buildoutcfg
speech = Speech()
speech.say_as(value='hello', interpret_as='spell-out')
speech.speak()
# <speak><say-as interpret-as="spell-out">hello</say-as><say-as interpret-as="spell-out">hello</say-as></speak>
```
#### prosody
```buildoutcfg
speech = Speech()
speech.prosody(value="sample sentence", rate='70%', pitch='+50%', volume='x-soft')
speech.speak()
# <prosody rate="70%" pitch="+50%" volume="x-soft">sample sentence</prosody
```
#### sub
```buildoutcfg
speech = Speech()
speech.sub(value="Al", alias="aluminum")
speech.speak()
# <sub alias="aluminum">Al</sub>
```
#### lang
```buildoutcfg
speech = Speech()
speech.lang(value="Paris", lang="fr-FR")
speech.speak()
# <lang xml:lang="fr-FR">Paris</lang>
```
#### voice
```buildoutcfg
speech = Speech()
speech.voice(value="I am not a real human.", name="Kendra")
speech.speak()
# <voice name="Kendra">I am not a real human.</voice>
```
#### pause
```buildoutcfg
speech = Speech()
speech.pause(time="3s", is_nested=True)
speech.speak()
# <break time="3s"/>
```
#### whisper
```buildoutcfg
speech = Speech()
speech.whisper("I am not a real human.")
speech.speak()
# <amazon:effect name="whispered">I am not a real human.</amazon:effect>
```
#### audio
```buildoutcfg
speech = Speech()
speech.audio('soundbank://soundlibrary/transportation/amzn_sfx_car_accelerate_01')
speech.speak()
# <audio src="soundbank://soundlibrary/transportation/amzn_sfx_car_accelerate_01" />
```
#### emphasis
```buildoutcfg
speech = Speech()
speech.add_text('I already told you I ')
speech.emphasis('really like', 'strong')
speech.add_text(' that person')
speech.speak()
# <speak>I already told you I <emphasis level="strong">really like</emphasis> that person</speak>
```
#### p
```buildoutcfg
speech = Speech()
speech.p("This is the first paragraph. There should be a pause after this text is spoken.")
speech.p("This is the second paragraph.")
# <speak><p>This is the first paragraph. There should be a pause after this text is spoken.</p><p>This is the second paragraph.</p></speak>
```


