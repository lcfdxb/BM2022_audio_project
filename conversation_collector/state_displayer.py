import toolings


class StateDisplayer:
    def __init__(self):
        self.truth = toolings.get_truth()

    def display_message(self, message="No Message"):
        print("Displaying Message: " + message)
        # TODO
        return None
