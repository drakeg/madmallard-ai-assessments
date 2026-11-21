from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from app.records import router, Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Mad Mallard AI Assessments", version="0.0.1")

app.include_router(router)

MODULES = [
    {"id": "time-leak", "name": "Time Leak", "source": "ActivityWatch", "status": "planned"},
    {"id": "ai-visibility", "name": "AI Visibility", "source": "Elmo", "status": "planned"},
    {"id": "lead-response", "name": "Lead Response", "source": "Browser Use", "status": "planned"},
]

# Indicative offer prices from the source video; hypotheses, not validated sales.
OFFERS = [
    {"id": "time-leak", "assessment_usd": 999, "recurring_usd": None, "requires_authorization": True},
    {"id": "ai-visibility", "assessment_usd": 999, "recurring_usd": 300, "requires_authorization": True},
    {"id": "lead-response", "assessment_usd": 999, "recurring_usd": None, "requires_authorization": True},
]

@app.get('/api/offers')
def offers():
    return {"offers": OFFERS, "pricing_status": "hypothesis", "currency": "USD"}

@app.get('/health')
def health():
    return {"status": "ok", "phase": "sprint-0"}

@app.get('/api/modules')
def modules():
    return {"modules": MODULES}

@app.get('/', response_class=HTMLResponse)
def home():
    cards = ''.join(f'<article><h2>{m["name"]}</h2><p>{m["source"]}</p><span>Integration planned</span></article>' for m in MODULES)
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Mad Mallard AI Assessments</title><style>body{{font:16px system-ui;background:#101827;color:#f8fafc;margin:0}}main{{max-width:1050px;margin:auto;padding:3rem 1.5rem}}.grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:1rem}}article{{background:#1e293b;border:1px solid #475569;border-radius:12px;padding:1.5rem}}span{{color:#fbbf24}}p{{color:#cbd5e1}}</style></head><body><main><h1>Mad Mallard AI Assessments</h1><p>Operator dashboard · Sprint 0 foundation · No client data collected</p><div class="grid">{cards}</div><p>Health: <a style="color:#93c5fd" href="/health">/health</a> · API: <a style="color:#93c5fd" href="/api/modules">/api/modules</a> · Docs: <a style="color:#93c5fd" href="/docs">/docs</a></p></main></body></html>'''
