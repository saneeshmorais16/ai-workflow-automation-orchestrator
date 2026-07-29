from orchestrator.audit import audit_event
def test_audit_shape():assert audit_event("intake","safe demo")["action"]=="intake"
