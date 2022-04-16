import traceback
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
        print("!!")
        print("!!!")
        print("Recycling orchestrator " + str(orchestrator.id) + " due to exception: " + str(e))
        traceback.print_exc()
        print("!!!")
        print("!!")
        oid += 1
        respawn_orchestrator()
