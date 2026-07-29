from orchestrator.simulator import next_state
def test_timeline():assert next_state("created")=="planned"
def test_terminal():assert next_state("completed")=="completed"
