import os
import aad_token_validation

client_id = os.environ.get('CLIENT_ID', '<your-webapp-id-goes-here>')
tenant_id = os.environ.get('TENANT_ID', '<your-tenant-id-goes-here>')

def main():
    
    token = ""
    token_validation = aad_token_validation.aadTokenValidation(client_id, tenant_id)
    decoded, cache_info = token_validation.decode_token(token)
    print(decoded)
    print(cache_info)

if __name__ == "__main__":
    main()