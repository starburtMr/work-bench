import asyncio

import pytest


def test_example_schema_trims_and_validates_names():
    from app.modules.example.presentation.schemas import ExampleRequest

    request = ExampleRequest(first_name=" jane ", last_name=" smith ")

    assert request.first_name == "jane"
    assert request.last_name == "smith"


def test_example_use_case_returns_greeting_message():
    from app.modules.example.application.use_cases import ExampleUseCases
    from app.modules.example.domain.entities import Example
    from app.modules.example.domain.value_objects import FullName

    example = Example(full_name=FullName(first_name="jane", last_name="smith"))

    result = asyncio.run(ExampleUseCases.hello(example))

    assert result.message == "Hello, Jane Smith!"


def test_example_entity_rejects_disallowed_demo_name():
    from app.modules.example.domain.entities import Example
    from app.modules.example.domain.value_objects import FullName
    from app.modules.shared.presentation.exceptions import DomainError

    with pytest.raises(DomainError):
        Example(full_name=FullName(first_name="john", last_name="doe"))
