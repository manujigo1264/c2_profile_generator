import json
import os
import logging
import sys

def load_config(config_file):
    """Load configuration from a JSON file."""
    try:
        with open(config_file, 'r') as file:
            config = json.load(file)
        return config
    except FileNotFoundError:
        logging.error(f"Configuration file not found: {config_file}")
        raise
    except json.JSONDecodeError:
        logging.error(f"Error decoding JSON from the file: {config_file}")
        raise

def generate_malleable_c2_profile(config):
    """Generate a Malleable C2 profile based on the provided configuration."""
    try:
        profile = f"""
# Malleable C2 Profile
#
# This profile is generated to configure C2 communications with customized HTTP GET/POST requests,
# metadata handling, URI rules, and SSL/TLS configurations.

set host "{config.get('host', 'default_host')}";

https-certificate {{
    set keystore "{config.get('keystore', 'default.keystore')}";
    set password "{config.get('keystore_password', 'default_password')}";
}}

http-get {{
    set uri {str(config.get('uris', ['/default-uri'])).replace("'", '"')};
    
    client {{
        header "Host" "{config.get('host', 'default_host')}";
        header "User-Agent" "{config.get('user_agent', 'default_user_agent')}";
        header "Accept" "*/*";
        header "Referer" "http://{config.get('host', 'default_host')}/";
        metadata {{
            netbios;
            prepend "{config.get('metadata_prepend', 'default_prepend')}";
            header "{config.get('metadata_header', 'default_header')}";
        }}
    }}
    
    server {{
        header "Content-Type" "application/octet-stream";
        header "Connection" "Keep-Alive";
    }}
}}

http-post {{
    set uri "{config.get('post_uri', '/default-post-uri')}";
    
    client {{
        id {{
            netbios;
        }}
        
        output {{
            {config.get('output_encoding', 'base64')};
        }}
    }}
    
    server {{
        header "Content-Type" "application/octet-stream";
        output {{
            {config.get('output_encoding', 'base64')};
        }}
    }}
}}

stage {{
    set sleep_mask "true";
    set cleanup "true";
    set userwx "false";
}}

process-inject {{
    set startrwx "false";
    set userwx "false";
}}

post-ex {{
    set obfuscate "true";
    set cleanup "true";
}}

# Sleep and Jitter configuration
set jitter "{config.get('jitter', 'default_jitter')}";
set sleeptime "{config.get('sleep_time', 'default_sleep_time')}";
"""

        # Write the profile to a file
        profile_path = os.path.join(os.getcwd(), f"{config.get('profile_name', 'default_profile')}.profile")
        with open(profile_path, "w") as file:
            file.write(profile)
        
        logging.info(f"Malleable C2 profile generated: {profile_path}")

    except KeyError as e:
        logging.error(f"Missing configuration key: {e}")
        raise

# Example usage
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    config_file = "c2_config.json"
    try:
        config = load_config(config_file)
        generate_malleable_c2_profile(config)
    except Exception as e:
        logging.error(f"Failed to generate profile: {e}")
        sys.exit(1)
