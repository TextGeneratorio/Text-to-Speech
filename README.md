# speech generator
Generate speech in a wav file from text, for free with https://text-generator.io

# Setup

clone this repo

```bash
git clone git@github.com:TextGeneratorio/subtitle-generator.git 
cd subtitle-generator
```

Install dependencies

```bash
virtualenv .env
source .env/bin/activate
pip install -r requirements.txt
```

Usage

```bash
TEXT_GENERATOR_API_KEY=YOUR_API_KEY_HERE python speech_generator.py \
  --text "Hello world" \
  --output_file output.wav
```


### Key words

text to speech API

AI Text Generation

speech to text API
