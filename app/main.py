from contextlib import asynccontextmanager
import json
from fastapi import FastAPI,HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from .config import BASE_DIR,EVAL_PATH
from .database import initialize
from .schemas import ReviewRequest,WorkflowCreate
from .storage import create,details,list_workflows,set_status
from .workflow_service import decide,plan_workflow,simulate
from .dashboard_service import metrics
from orchestrator.evaluator import evaluate_cases
@asynccontextmanager
async def lifespan(app):initialize();yield
app=FastAPI(title="AI Workflow Automation Orchestrator",version="1.0.0",lifespan=lifespan);app.mount("/static",StaticFiles(directory=BASE_DIR/"app"/"static"),name="static")
@app.get("/",include_in_schema=False)
def index():return FileResponse(BASE_DIR/"app"/"static"/"index.html")
@app.get("/health")
def health():return {"status":"ok","mode":"local_simulation","real_automations":False,"llm_enabled":False}
@app.post("/workflows")
def new(req:WorkflowCreate):wid=create(req);return {"workflow_id":wid,"status":"created"}
@app.get("/workflows")
def all_workflows():return list_workflows()
@app.get("/workflows/{workflow_id}")
def one(workflow_id:int):
    w=details(workflow_id)
    if not w:raise HTTPException(404,"Workflow not found")
    return w
@app.post("/workflows/{workflow_id}/plan")
def plan(workflow_id:int):
    x=plan_workflow(workflow_id)
    if not x:raise HTTPException(404,"Workflow not found")
    return {"workflow_id":workflow_id,**x}
def review(workflow_id,target,req):
    try:x=decide(workflow_id,target,req.reviewer_note)
    except ValueError as e:raise HTTPException(409,str(e))
    if not x:raise HTTPException(404,"Workflow not found")
    return {"workflow_id":workflow_id,"approval_status":x}
@app.post("/workflows/{workflow_id}/approve")
def approve(workflow_id:int,req:ReviewRequest):return review(workflow_id,"Approved",req)
@app.post("/workflows/{workflow_id}/reject")
def reject(workflow_id:int,req:ReviewRequest):return review(workflow_id,"Rejected",req)
@app.post("/workflows/{workflow_id}/escalate")
def escalate(workflow_id:int,req:ReviewRequest):return review(workflow_id,"Escalated",req)
@app.post("/workflows/{workflow_id}/simulate")
def run_simulation(workflow_id:int):
    x=simulate(workflow_id)
    if not x:raise HTTPException(404,"Workflow not found")
    return {"workflow_id":workflow_id,"status":x,"simulation_only":True}
@app.get("/dashboard")
def dashboard():return metrics(list_workflows())
@app.post("/evaluate")
def evaluate():return evaluate_cases(json.loads(EVAL_PATH.read_text(encoding="utf-8-sig")))
