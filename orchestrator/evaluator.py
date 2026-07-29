from .classifier import classify_request
from .planner import build_plan
from .risk_engine import assess_risk
from .routing import recommend_route

def evaluate_cases(cases):
    results=[]
    for c in cases:
        classification=classify_request(c["request"]);tasks=build_plan(classification);risk=assess_risk(c["request"],tasks);route=recommend_route(classification["classifier_key"],risk["risk_level"])
        checks={"classification":classification["workflow_type"]==c["expected_type"],"task_completeness":len(tasks)>=3 and all(t.get("owner_role") for t in tasks),"risk":risk["risk_level"]==c["expected_risk"],"routing":route["route_to"]==c["expected_route"],"approval":risk["approval_required"]==c["approval_required"]}
        results.append({"name":c["name"],"checks":checks,"passed":all(checks.values())})
    return {"cases":results,"pass_rate":round(sum(x["passed"] for x in results)/max(1,len(results)),3),"regression_passed":all(x["passed"] for x in results)}
