from pathlib import Path
from enum import Enum
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


SITE_URL = 'https://'
BASE_DIR = Path(__file__).resolve().parent


class Mode(Enum):
    prod = 'prod'
    dev = 'dev'


class Base(BaseSettings):
    MODE: Mode = Field(default = Mode.prod)
    model_config = SettingsConfigDict(env_file=BASE_DIR / ".env")


class CORSSettings(Base):
    ALLOW_METHODS: list[str] = ['GET', 'POST', 'PATCH', 'DELETE']
    ALLOW_HEADERS: list[str] = ['*']

    @property
    def ORIGINS(self) -> list[str]:
        return [SITE_URL] if self.MODE == Mode.prod else ['*']


class DBSettings(Base):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    @property
    def ECHO(self) -> bool:
        return self.MODE != Mode.prod

    @property
    def DB_URL(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"


class AuthJWT(Base):
    private_key: Path = BASE_DIR.parent / "certs" / "jwt-private.pem"
    public_key: Path = BASE_DIR.parent / "certs" / "jwt-public.pem"
    ALGORITHM: str = 'RS256'


class Settings:
    auth_jwt: AuthJWT = AuthJWT()
    cors: CORSSettings = CORSSettings()
    db: DBSettings = DBSettings()


settings = Settings
