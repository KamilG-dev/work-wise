from redis import Redis

from config import Config

class RedisManager:
    PREFIX = "__fjo__"
    _connection: Redis = None

    def __init__(self):
        self._connection = Redis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)

    def block_token(self, token: str):
        key = f'{self.PREFIX}tokenblocked__{token}'
        self._connection.set(key, 1, ex=Config.JWT_ACCESS_TOKEN_EXPIRES)

    def token_blocked(self, token: str) -> bool:
        key = f'{self.PREFIX}tokenblocked__{token}'
        return self._connection.exists(key)

redis_client = RedisManager()