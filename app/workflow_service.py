from .storage import details,log,save_plan,set_status
from orchestrator.classifier import classify_request
from orchestrator.planner import build_plan
from orchestrator.risk_engine import assess_risk
from orchestrator.routing import recommend_route
from orchestrator.automation_recommender import recommend_automations
from orchestrator.approval_workflow import transition
from orchestrator.simulator import next_state
def plan_workflow(wid):
    w=details(wid)
    if not w:return None
    c=classify_request(w["request_description"]);tasks=build_plan(c);risk=assess_risk(w["request_description"],tasks);route=recommend_route(c["classifier_key"],risk["risk_level"]);plan={"workflow_type":c["workflow_type"],"classification":c,"tasks":tasks,"risk":risk,"route":route,"automation_recommendations":recommend_automations(tasks,risk),"audit_status":"workflow_plan_created","disclaimer":"Simulation only; every recommendation is human-reviewable."};save_plan(wid,plan);log(wid,"classification",c["workflow_type"]);log(wid,"planned_tasks",f"{len(tasks)} tasks");log(wid,"risk_score",str(risk["risk_score"]));log(wid,"routing_decision",route["route_to"]);return plan
def decide(wid,target,note):
    w=details(wid)
    if not w:return None
    current=(w["plan"] or {}).get("risk",{}).get("approval_status","Draft")
    new=transition(current,target);w["plan"]["risk"]["approval_status"]=new;save_plan(wid,w["plan"],target.lower());log(wid,"approval_decision",new,note);return new
def simulate(wid):
    w=details(wid)
    if not w:return None
    needed=(w["plan"] or {}).get("risk",{}).get("approval_required",True);nxt=next_state(w["status"],needed);set_status(wid,nxt);return nxt
