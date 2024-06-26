from pydantic_settings import BaseSettings


class DBSettings(BaseSettings):
    NAME: str

    @property
    def connection_string(self):
        return f'sqlite:///{self.NAME}'


class AppConfig(BaseSettings):
    database: DBSettings

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
        env_nested_delimiter = '__'
