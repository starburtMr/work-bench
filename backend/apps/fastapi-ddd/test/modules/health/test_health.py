import asyncio


def test_health_use_case_returns_ok_status():
    from app.modules.health.application.enums import HealthType
    from app.modules.health.application.use_cases import HealthUseCases

    health = asyncio.run(HealthUseCases.health())

    assert health.status == HealthType.OK
