from backend.const import proxy as const


class ProxyDTO:
    def __init__(self, user_name: str, password: str, proxy_address: str, port: int):
        self.user_name = user_name
        self.password = password
        self.proxy_address = proxy_address
        self.port = port


"""
: raise InvalidProxyException: if the proxy is invalid
"""


class ProxyDTOBuilder:
    @staticmethod
    def build(data: dict) -> ProxyDTO:

        user_name = data[const.FIELD_USERNAME]
        password = data[const.FIELD_PASSWORD]
        proxy_address = data[const.FIELD_PROXY_ADDRESS]
        port = data[const.FIELD_PORT]
        is_valid = data[const.FIELD_VALID]

        if not is_valid:
            raise InvalidProxyException(f"Invalid proxy: {user_name}@{proxy_address}:{port}")

        return ProxyDTO(
            user_name,
            password,
            proxy_address,
            port
        )


class InvalidProxyException(Exception):
    def __init__(self, message):
        super().__init__(message)
