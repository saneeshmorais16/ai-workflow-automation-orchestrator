SIGNALS={"financial_action":["refund","payment","finance","money"],"customer_impact":["customer","support","ticket"],"personal_data":["personal data","employee","onboarding"],"access_permission":["access","permission","account"],"compliance_sensitivity":["compliance","regulation","risk review"],"ai_generated_decision":["ai decision","model decision","automated decision"]}
def assess_risk(text,tasks):
    low=text.lower();flags=[k for k,words in SIGNALS.items() if any(w in low for w in words)]
    ambiguous=len(text.split())<5
    if ambiguous:flags.append("ambiguous_request")
    approval=any(t["requires_approval"] for t in tasks)
    if flags and not approval:flags.append("missing_human_review")
    points=sum(2 if f in {"financial_action","personal_data","access_permission","compliance_sensitivity","ai_generated_decision"} else 1 for f in flags)
    level="Critical" if points>=6 else "High" if points>=3 else "Medium" if points>=1 else "Low"
    return {"risk_level":level,"risk_score":min(100,points*14),"risk_flags":flags,"approval_required":approval or level!="Low","approval_status":"Needs Review" if approval or level!="Low" else "Draft"}

