def test_settings_loads_parseable_skeleton_defaults():
    from app.core.settings import settings

    assert settings.APPLICATION_TITLE == "FastAPI DDD Backend Skeleton"
    assert settings.APPLICATION_ENVIRONMENT_DEBUG is True
    assert str(settings.POSTGRESQL_ASYNC_DATABASE_URL).startswith(
        "postgresql+asyncpg://fastapi_ddd:"
    )
    assert settings.SECURITY_ALLOW_METHODS == [
        "GET",
        "POST",
        "PATCH",
        "DELETE",
        "OPTIONS",
    ]
