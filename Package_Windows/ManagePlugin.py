import threading
from Package_Windows.ProcessPlugin import ProcessPlugin

class ManagePlugin:
    def __init__(self, args):
        self.args = args
        self.plugins = ["windows.envars.Envars", "windows.pslist.PsList"]  # Liste des plugins

    def execute(self):
        start_thread = ProcessPlugin(self.args.file, self.args.path)
        threads = []

        for plugin in self.plugins:
            t = threading.Thread(target=start_thread.run, args=(plugin,))
            t.start()
            threads.append(t)

        for t in threads:
            t.join()
