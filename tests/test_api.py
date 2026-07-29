from fastapi.testclient import TestClient
from app.main import app
def test_health():
    with TestClient(app) as c:assert c.get('/health').json()["real_automations"] is False
def test_workflow_plan_audit_dashboard():
    with TestClient(app) as c:
        x=c.post('/workflows',json={"title":"Refund review","request_description":"Handle customer refund payment requests safely","requester":"Synthetic","business_area":"Finance","priority":"high"});assert x.status_code==200;wid=x.json()["workflow_id"];p=c.post(f'/workflows/{wid}/plan');assert p.status_code==200 and len(p.json()["tasks"])==3;d=c.get(f'/workflows/{wid}').json();assert len(d["audit_log"])>=5 and d["timeline"][-1]["status"]=="planned";assert c.get('/dashboard').json()["total_workflows"]>=1
def test_evaluation():
    with TestClient(app) as c:
        r=c.post('/evaluate');assert r.status_code==200 and r.json()["regression_passed"]
