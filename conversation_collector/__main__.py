from orchestrator import Orchestrator


def respawn_orchestrator():
    global orchestrator
    orchestrator = Orchestrator(oid=oid)
    print("Spawned new orchestrator " + str(orchestrator.id))


oid = 0
orchestrator = Orchestrator(oid=oid)

while True:
    try:
        orchestrator.work()
    except Exception as e:
        print("Recycling orchestrator " + str(orchestrator.id) + " due to exception: " + str(e))
        oid += 1
        respawn_orchestrator()
