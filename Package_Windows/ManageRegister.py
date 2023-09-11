import threading
from ProcessRegister import ProcessRegister

class ManageRegister:
    def __init__(self, args):
        self.args = args
        self.register = ["'...'"]  # Liste des clés de registre

    def execute(self):
        start_thread = ProcessRegister(self.args.file, self.args.path)
        threads = []

        for reg in self.register:
            t = threading.Thread(target=start_thread.run, args=(reg,))
            t.start()
            threads.append(t)

        for t in threads:
            t.join()

