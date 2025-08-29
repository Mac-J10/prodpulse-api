import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_product_metrics():
    async with AsyncClient(base_url="http://localhost:8000") as client:
        response = await client.get("/products/123/metrics/")
    assert response.status_code == 200yes