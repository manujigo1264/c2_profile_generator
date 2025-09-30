# Malleable C2 Profile Generator

Python tool for generating Malleable C2 profiles for Cobalt Strike with customizable configurations.

## Prerequisites

- Python 3.8+
- Cobalt Strike (licensed)

## Installation
```bash
git clone <your-repo-url>
cd c2_profile_generator
Usage
Edit c2_config.json with your parameters, then generate:
bashpython c2_profile_generator.py
Options:
bashpython c2_profile_generator.py --config custom_config.json --output ./profiles
Configuration
Modify c2_config.json:

profile_name: Output filename
host: C2 domain
uris: GET request URIs
post_uri: POST endpoint
user_agent: Client user agent
jitter: Connection jitter percentage
sleep_time: Beacon sleep time (ms)
keystore: SSL certificate path
output_encoding: Payload encoding

License
MIT License
Contact
JiSec