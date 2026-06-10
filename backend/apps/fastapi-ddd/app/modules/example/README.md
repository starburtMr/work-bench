# Example Module

This module is the complete DDD reference flow for the skeleton.

Use it to understand how a request moves through:

1. `presentation/schemas.py` for input and output models.
2. `presentation/routers.py` for HTTP routing and dependency wiring.
3. `domain/value_objects.py` and `domain/entities.py` for domain rules.
4. `domain/mappers.py` for schema-domain conversion.
5. `application/use_cases.py` for orchestration.

Keep this module generic. It should teach the skeleton's layering style without becoming a product-specific feature.
