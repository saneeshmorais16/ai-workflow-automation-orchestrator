TEMPLATES={
"support_triage":[("Validate ticket details","Support Analyst",False),("Assess severity and customer impact","Support Lead",True),("Route to resolution queue","Support Coordinator",False)],
"report_approval":[("Validate report inputs","Report Owner",False),("Review report accuracy","Manager Reviewer",True),("Record approval decision","Report Owner",True)],
"refund_review":[("Validate refund request","Support Analyst",False),("Check policy and financial amount","Finance Reviewer",True),("Record refund decision","Finance Approver",True)],
"hr_onboarding":[("Validate onboarding checklist","HR Coordinator",False),("Prepare access requirements","IT Coordinator",True),("Confirm manager approval","Hiring Manager",True)],
"it_access_request":[("Validate least-privilege need","IT Service Analyst",False),("Review access sensitivity","System Owner",True),("Record access approval","IT Approver",True)],
"ai_risk_review":[("Review system purpose","AI Governance Reviewer",False),("Check data sensitivity","Data Owner",True),("Confirm human oversight control","Product Owner",True)],
"data_quality_review":[("Profile synthetic dataset","Data Analyst",False),("Review quality exceptions","Data Steward",True),("Approve remediation plan","Data Owner",True)],
"document_processing":[("Validate document intake","Document Operations",False),("Review extracted fields","Human Reviewer",True),("Approve structured output","Process Owner",True)],
"general_automation":[("Clarify request scope","Operations Analyst",True),("Draft safe workflow","Process Owner",True),("Approve simulation","Manager Reviewer",True)]}
def build_tasks(key):
    out=[]
    for i,(name,owner,approval) in enumerate(TEMPLATES.get(key,TEMPLATES["general_automation"]),1):out.append({"task_id":f"task-{i}","task_name":name,"description":f"Simulated step: {name.lower()}.","owner_role":owner,"dependency":None if i==1 else f"task-{i-1}","status":"pending","due_priority":"high" if approval else "normal","requires_approval":approval})
    return out
def build_plan(classification):return build_tasks(classification["classifier_key"])
