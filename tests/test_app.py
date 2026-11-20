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

def test_operator_auth_required():
    assert client.get('/api/customers').status_code == 401
    assert client.post('/api/customers', json={'name': 'Demo'}).status_code == 401

def test_customer_assessment_lifecycle(monkeypatch):
    monkeypatch.setenv('OPERATOR_API_KEY', 'test-only-key')
    headers = {'X-Operator-Key': 'test-only-key'}
    customer = client.post('/api/customers', headers=headers, json={'name': 'Example Shop'})
    assert customer.status_code == 201
    customer_id = customer.json()['id']
    assert any(c['id'] == customer_id for c in client.get('/api/customers', headers=headers).json()['customers'])
    payload = {'customer_id': customer_id, 'module': 'ai-visibility', 'scope': 'Authorized brand visibility audit', 'authorization_reference': 'TEST-CONSENT-001'}
    created = client.post('/api/assessments', headers=headers, json=payload)
    assert created.status_code == 201
    assessment_id = created.json()['id']
    assert created.json()['status'] == 'draft'
    assert any(a['id'] == assessment_id for a in client.get('/api/assessments', headers=headers).json()['assessments'])
    assert client.post(f'/api/assessments/{assessment_id}/close', headers=headers).json()['status'] == 'closed'
    assert client.post('/api/assessments', headers=headers, json={**payload, 'module': 'unknown'}).status_code == 422
