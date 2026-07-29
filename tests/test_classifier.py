from orchestrator.classifier import classify_request
def test_ai_risk():assert classify_request("Review AI system model risk")["workflow_type"]=="AI Risk Review"
def test_general():assert classify_request("make this better")["workflow_type"]=="General Automation"
