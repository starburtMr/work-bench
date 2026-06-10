def test_app_registers_core_routes():
    from app.app import app

    paths = {route.path for route in app.routes}

    assert "/health/" in paths
    assert "/api/v1/example/" in paths
    assert "/api/v1/authentication/login/" in paths
    assert "/api/v1/user/" in paths


def test_openapi_registers_security_schemes():
    from app.app import app

    schema = app.openapi()

    assert "BearerAuth" in schema["components"]["securitySchemes"]
    assert "ApiKeyAuth" in schema["components"]["securitySchemes"]
