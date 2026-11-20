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

def test_offers_are_explicit_hypotheses():
    data = client.get('/api/offers').json()
    assert data['pricing_status'] == 'hypothesis'
    assert len(data['offers']) == 3
    assert all(o['requires_authorization'] for o in data['offers'])
    assert next(o for o in data['offers'] if o['id'] == 'ai-visibility')['recurring_usd'] == 300
