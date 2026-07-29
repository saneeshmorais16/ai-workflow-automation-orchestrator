import json
from .database import connect
def log(workflow_id,action,details="",note=""):
    with connect() as db:db.execute("INSERT INTO audit_log(workflow_id,action,details,reviewer_note) VALUES(?,?,?,?)",(workflow_id,action,details,note))
def create(data):
    with connect() as db:
        cur=db.execute("INSERT INTO workflows(title,request_description,requester,business_area,priority) VALUES(?,?,?,?,?)",(data.title,data.request_description,data.requester,data.business_area,data.priority));wid=cur.lastrowid;db.execute("INSERT INTO timeline(workflow_id,status) VALUES(?,?)",(wid,"created"))
    log(wid,"intake","Synthetic workflow request recorded");return wid
def list_workflows(workflow_id=None):
    q="SELECT * FROM workflows";p=()
    if workflow_id:q+=" WHERE workflow_id=?";p=(workflow_id,)
    with connect() as db:rows=[dict(r) for r in db.execute(q+" ORDER BY workflow_id DESC",p)]
    for r in rows:r["plan"]=json.loads(r.pop("plan_json")) if r.get("plan_json") else None
    return rows
def save_plan(wid,plan,status="planned"):
    with connect() as db:db.execute("UPDATE workflows SET workflow_type=?,plan_json=?,status=? WHERE workflow_id=?",(plan["workflow_type"],json.dumps(plan),status,wid));db.execute("INSERT INTO timeline(workflow_id,status) VALUES(?,?)",(wid,status))
def set_status(wid,status,note=""):
    with connect() as db:db.execute("UPDATE workflows SET status=? WHERE workflow_id=?",(status,wid));db.execute("INSERT INTO timeline(workflow_id,status) VALUES(?,?)",(wid,status))
    log(wid,"status_changed",status,note)
def details(wid):
    rows=list_workflows(wid)
    if not rows:return None
    with connect() as db:aud=[dict(x) for x in db.execute("SELECT * FROM audit_log WHERE workflow_id=? ORDER BY id",(wid,))];timeline=[dict(x) for x in db.execute("SELECT status,created_at FROM timeline WHERE workflow_id=? ORDER BY id",(wid,))]
    return {**rows[0],"audit_log":aud,"timeline":timeline}
