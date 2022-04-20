import logging
import traceback
import files_manager
from orchestrator import Orchestrator


def respawn_orchestrator():
    global orchestrator
    orchestrator = Orchestrator(oid=oid)
    logging.warning("Spawned new orchestrator " + str(orchestrator.id))


oid = 0
orchestrator = Orchestrator(oid=oid)
log_file_path = files_manager.get_new_log_file_path(files_manager.get_new_file_name_no_ext())
logging.basicConfig(filename=log_file_path, filemode='w', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', force=True)
logging.info("Init.")

while True:
    try:
        orchestrator.work()
    except Exception as e:
        logging.error("Recycling orchestrator " + str(orchestrator.id) + " due to exception: " + str(e))
        traceback.print_exc()
        # clean up
        orchestrator.audioPlayer.start_playing()
        orchestrator.audioPlayer.terminate()
        orchestrator.audioRecorder.terminate()
        # restart
        oid += 1
        respawn_orchestrator()
