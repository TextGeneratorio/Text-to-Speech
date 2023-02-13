import argparse

import requests
import os

API_KEY = os.getenv("TEXT_GENERATOR_API_KEY")
if API_KEY is None:
    raise Exception(
        "Please set TEXT_GENERATOR_API_KEY environment variable, login to https://text-generator.io to get your API key")
headers = {"secret": API_KEY}


def create_speech(text, output_file):
    audio_params = {
        "text": text,
        "speaker": "Male fast",
    }
    response = requests.post("https://api.text-generator.io/api/v1/generate_speech", json=audio_params, headers=headers)
    binary_file_response = response.content
    with open(output_file, "wb") as f:
        f.write(binary_file_response)

# create_speech("Text-Generator.io is bringing the cost of intelligence toward zero.", "test.wav")
if __name__ == "__main__":
    # video_url and output_file are required
    parser = argparse.ArgumentParser(
        description="Generate speech from text"

    )
    parser.add_argument("--text", type=str, required=True)
    parser.add_argument("--output_file", type=str, required=True)
    args = parser.parse_args()
    create_speech(args.text, args.output_file)
