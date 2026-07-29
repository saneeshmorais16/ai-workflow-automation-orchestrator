ALLOWED={"Draft":{"Needs Review","Approved"},"Needs Review":{"Approved","Rejected","Escalated"},"Approved":{"completed"},"Rejected":set(),"Escalated":{"Approved","Rejected"}}
def transition(current,target):
    if target not in ALLOWED.get(current,set()):raise ValueError(f"Invalid approval transition: {current} -> {target}")
    return target
