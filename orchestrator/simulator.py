SEQUENCE=["created","planned","routed","waiting for approval","approved","completed"]
def next_state(current,approval_required=True):
    seq=SEQUENCE if approval_required else ["created","planned","routed","completed"]
    if current in {"blocked","escalated","completed"}:return current
    try:return seq[min(seq.index(current)+1,len(seq)-1)]
    except ValueError:return "blocked"
