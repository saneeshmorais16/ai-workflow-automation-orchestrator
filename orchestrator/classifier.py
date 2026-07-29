TYPES={
"support_triage":["support","ticket","incident","escalation"],"report_approval":["report","approve","sign-off"],"refund_review":["refund","reimburse","payment"],"hr_onboarding":["onboarding","new starter","employee","hr"],"it_access_request":["access permission","account access","system access"],"ai_risk_review":["ai system","model","algorithm","ai risk"],"data_quality_review":["data quality","validation","dataset"],"document_processing":["document","extract","invoice","contract"]}
DISPLAY={k:k.replace("_"," ").title() for k in TYPES};DISPLAY["ai_risk_review"]="AI Risk Review";DISPLAY["hr_onboarding"]="HR Onboarding";DISPLAY["it_access_request"]="IT Access Request"
def classify_request(text):
    low=text.lower();scores={k:sum(x in low for x in terms) for k,terms in TYPES.items()};kind=max(scores,key=scores.get)
    return {"workflow_type":DISPLAY[kind] if scores[kind] else "General Automation","classifier_key":kind if scores[kind] else "general_automation","confidence":round(min(.98,.45+.15*scores[kind]),2) if scores[kind] else .3,"matched_signals":[x for x in TYPES.get(kind,[]) if x in low]}


