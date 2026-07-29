ROUTES={"support_triage":"Support Team","report_approval":"Manager Review","refund_review":"Finance Team","hr_onboarding":"HR Team","it_access_request":"IT Team","ai_risk_review":"AI Governance Team","data_quality_review":"Data Team","document_processing":"General Operations","general_automation":"General Operations"}
def recommend_route(key,risk_level):
    team=ROUTES.get(key,"General Operations")
    if risk_level=="Critical":return {"route_to":"Manager Review","routing_reason":f"Critical risk requires manager oversight before {team} processing."}
    return {"route_to":team,"routing_reason":f"Request signals align with the {team} operating domain."}
