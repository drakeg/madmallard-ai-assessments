from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    assert client.get('/health').json()['status'] == 'ok'

def test_modules():
    modules = client.get('/api/modules').json()['modules']
    assert len(modules) == 3
    assert {m['id'] for m in modules} == {'time-leak', 'ai-visibility', 'lead-response'}

def test_dashboard():
    assert 'Mad Mallard AI Assessments' in client.get('/').text
