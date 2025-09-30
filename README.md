# Malleable C2 Profile Generator

Python tool for generating Malleable C2 profiles for Cobalt Strike with customizable configurations.

> **WARNING:** For authorized security testing and red team operations only. Ensure you have proper authorization before deployment.

## Prerequisites

- Python 3.8+
- Cobalt Strike (licensed)

## Installation

Clone the repository:

```bash
git clone <your-repo-url>
cd c2_profile_generator
```

## Usage

Edit `c2_config.json` with your parameters, then generate:

```bash
python c2_profile_generator.py
```

### Command Options

```bash
python c2_profile_generator.py --config custom_config.json --output ./profiles
```

- `--config`: Path to configuration file (default: `c2_config.json`)
- `--output`: Output directory for generated profiles

## Configuration

Modify `c2_config.json` with your operational parameters:

- `profile_name`: Output filename for generated profile  
- `host`: C2 server domain or IP  
- `uris`: Array of GET request URIs  
- `post_uri`: POST endpoint for data exfiltration  
- `user_agent`: Client user agent string  
- `jitter`: Connection jitter percentage (timing randomization)  
- `sleep_time`: Beacon sleep time in milliseconds  
- `keystore`: Path to SSL certificate keystore  
- `keystore_password`: Keystore password  
- `metadata_prepend`: Metadata prepend string  
- `metadata_header`: HTTP header for metadata  
- `output_encoding`: Payload encoding method (`base64`, etc.)

> **Security Note:** Replace placeholder values in `c2_config.json` (especially `keystore_password`) with your actual credentials. Never commit real operational credentials to version control.

## Example Output

Generated profiles include:

- SSL/TLS certificate configuration  
- HTTP GET/POST request structures  
- Metadata handling and encoding  
- Process injection and evasion settings  
- Sleep and jitter configurations

## License

MIT License

## Contact

JiSec LLC

## Disclaimer

This tool is provided for educational and authorized security testing purposes only. Users are responsible for complying with all applicable laws and regulations. Unauthorized access to computer systems is illegal.
