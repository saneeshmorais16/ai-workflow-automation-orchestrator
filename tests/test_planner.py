from orchestrator.planner import build_tasks
def test_tasks_are_structured():
    t=build_tasks("refund_review");assert len(t)>=3 and t[1]["dependency"]=="task-1" and any(x["requires_approval"] for x in t)
