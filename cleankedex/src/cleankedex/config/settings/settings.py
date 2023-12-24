from starlette.config import Config


config = Config()


class Settings:
    """Settings class containing configuration parameters for the Cleankedex project."""

    PROJECT_NAME: str = config("PROJECT_NAME", cast=str, default="Cleankedex")
    PROJECT_VERSION: str = config("PROJECT_VERSION", cast=str, default="1.0.0")

    LOG_LEVEL: str = config("LOG_LEVEL", cast=str, default="DEBUG").upper()

    SQLALCHEMY_DATABASE_URI = config(
        "SQLALCHEMY_DATABASE_URI",
        cast=str,
        default="postgresql://guest:guest@localhost:5432/pokedex",
    )

    # Database finsesse
    POOL_SIZE = config("POOL_SIZE", cast=int, default=5)
    MAX_OVERFLOW = config("MAX_OVERFLOW", cast=int, default=-1)
    POOL_PRE_PING = config("POOL_PRE_PING", cast=bool, default=True)
    ECHO = config("ECHO", cast=bool, default=False)
    POOL_RECYCLE_IN_SECONDS = config("POOL_RECYCLE_IN_SECONDS", cast=int, default=3600)
    ECHO_POOL = config("ECHO_POOL", cast=bool, default=False)
    POOL_RESET_ON_RETURN = config("POOL_RESET_ON_RETURN", cast=str, default="rollback")
    POOL_TIMEOUT_IN_SECONDS = config("POOL_TIMEOUT_IN_SECONDS", cast=int, default=30)
    POOL = config("POOL", cast=str, default="~sqlalchemy.pool.QueuePool")

    PERF_COUNTER_ACTIVE = config("PERF_COUNTER_ACTIVE", cast=bool, default=True)
    PERF_COUNTER_USE_LOGGER = config("PERF_COUNTER_USE_LOGGER", cast=bool, default=True)
    PERF_EXTENDED_INFO = config("PERF_EXTENDED_INFO", cast=bool, default=True)


settings: Settings = Settings()
