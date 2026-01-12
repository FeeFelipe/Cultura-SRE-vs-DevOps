import pytest
from main import app

def test_health_up():
    with app.test_client() as client:
        response = client.get('/health')
        assert response.status_code == 200
        data = response.get_json()
        assert data['status'] == 'UP'
        assert 'service' in data
        assert 'version' in data
        assert 'timestamp' in data
