def metrics(rows):
    risks={"Low":0,"Medium":0,"High":0,"Critical":0}
    for w in rows:
        if w.get("plan"):risks[w["plan"]["risk"]["risk_level"]]+=1
    return {"total_workflows":len(rows),"needs_review":sum(w["status"] in {"planned","waiting for approval"} for w in rows),"completed":sum(w["status"]=="completed" for w in rows),"risk_distribution":risks}
