import jwt
from aadtoken import get_public_key, get_jwks


class aadTokenValidation(self):
    def __init__(self, model, client_id, tenant_id):
        self.client_id = client_id
        self.tenant_id = tenant_id

    def decode_token(self, token):

        issuer = 'https://sts.windows.net/{tenant_id}/'.format(tenant_id=self.tenant_id)

        public_key = get_public_key(token)
        public_key = get_public_key(token)
        public_key = get_public_key(token)
        decoded = jwt.decode(token,
                            public_key,
                            verify=True,
                            algorithms=['RS256'],
                            audience=[self.client_id],
                            issuer=issuer)
                        
        return decoded, get_jwks.cache_info()

