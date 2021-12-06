import jwt
from aadtoken import get_public_key, get_jwks


class aadTokenValidation():
    def __init__(self, client_id, tenant_id, audience):
        self.client_id = client_id
        self.tenant_id = tenant_id
        self.audience = audience
        self._token_decoded = None

    def decode_token(self, token):

        issuer = 'https://sts.windows.net/{tenant_id}/'.format(tenant_id=self.tenant_id)

        public_key = get_public_key(token)
        # public_key = get_public_key(token)
        # public_key = get_public_key(token)
        self._decoded = jwt.decode(token,
                            public_key,
                            verify=True,
                            algorithms=['RS256'],
                            audience=[self.audience],
                            issuer=issuer)
                        
        return self._decoded, get_jwks.cache_info()

    def get_token(self):
        return self._token_decoded

    def get_token_roles(self):
        return self._token_decoded.get('roles')

    def get_token_user(self):
        return self._token_decoded.get('upn')

    
