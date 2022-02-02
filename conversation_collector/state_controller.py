import toolings


class StateController:
    def __init__(self):
        self.truth = toolings.get_truth()

    def should_record(self):
        # TODO
        return True

    def ack_recording_began(self):
        # TODO
        return None
