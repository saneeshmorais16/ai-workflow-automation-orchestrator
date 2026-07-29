from orchestrator.routing import recommend_route
def test_route():assert recommend_route("refund_review","High")["route_to"]=="Finance Team"
def test_critical_route():assert recommend_route("ai_risk_review","Critical")["route_to"]=="Manager Review"
