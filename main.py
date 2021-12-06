import os
import aad_token_validation

client_id = os.environ.get('CLIENT_ID', '')
tenant_id = os.environ.get('TENANT_ID', '')
audience = os.environ.get('AUDIENCE', '')

def main():
    
    token = ""
    token_validation = aad_token_validation.aadTokenValidation(client_id, tenant_id, audience)
    decoded, cache_info = token_validation.decode_token(token)
    print(decoded)

    print("Cache")
    print(cache_info)

if __name__ == "__main__":
    main()