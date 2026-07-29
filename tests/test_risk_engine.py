from orchestrator.risk_engine import assess_risk
def test_critical_risk():
    t=[{"requires_approval":True}];assert assess_risk("AI decision personal data access permission compliance payment",t)["risk_level"]=="Critical"
def test_ambiguous():assert "ambiguous_request" in assess_risk("do it",[])["risk_flags"]
