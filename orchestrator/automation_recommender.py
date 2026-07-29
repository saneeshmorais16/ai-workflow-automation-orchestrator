def recommend_automations(tasks,risk):
    items=["data validation","routing","checklist generation","audit logging"]
    if risk["approval_required"]:items += ["approval request","notification"]
    if risk["risk_level"] in {"High","Critical"}:items.append("escalation")
    return [{"step":x,"mode":"simulation_only","human_review":x in {"approval request","escalation"}} for x in dict.fromkeys(items)]
