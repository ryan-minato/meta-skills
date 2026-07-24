from functools import lru_cache
from typing import Literal

from pydantic import BaseModel, Field
from pydantic_settings import (
    BaseSettings,
    PydanticBaseSettingsSource,
    SettingsConfigDict,
    TomlConfigSettingsSource,
)

Backend = Literal["local", "s3", "huggingface"]
ProductStage = Literal["profile", "clean", "integrate", "final", "quarantine"]


class SourceSettings(BaseModel):
    name: str
    backend: Backend
    uri: str
    version: str | None = None
    etag: str | None = None
    checksum: str | None = None
    schema_version: str


class ProductSettings(BaseModel):
    name: str
    backend: Backend
    uri: str
    stage: ProductStage
    inputs: list[str] = Field(min_length=1)
    schema_version: str


class QualitySettings(BaseModel):
    critical_rules: list[str] = Field(min_length=1)
    row_rejection_policy: Literal["quarantine"]
    quarantine_product: str


class LoggingSettings(BaseModel):
    level: str = "INFO"


class ModelSettings(BaseModel):
    repository: str
    revision: str
    local_path: str | None = None


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_nested_delimiter="__",
        extra="forbid",
        toml_file="config/project.toml",
    )

    project_name: str
    random_seed: int = 0
    sources: list[SourceSettings] = Field(min_length=1)
    products: list[ProductSettings] = Field(min_length=1)
    quality: QualitySettings
    logging: LoggingSettings = LoggingSettings()
    model: ModelSettings | None = None

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> tuple[PydanticBaseSettingsSource, ...]:
        return (
            init_settings,
            env_settings,
            dotenv_settings,
            TomlConfigSettingsSource(settings_cls),
            file_secret_settings,
        )


@lru_cache
def get_settings() -> Settings:
    return Settings()
