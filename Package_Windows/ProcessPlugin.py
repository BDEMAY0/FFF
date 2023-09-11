import subprocess

class ProcessPlugin:
    def __init__(self, image_path, folder_vol_path):
        self.image_path = image_path
        self.folder_vol_path = folder_vol_path

    def run(self, plugin):
        cmd = ["python", f"{self.folder_vol_path}/vol.py", "-f", self.image_path, plugin]
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            print(f"Resultat pour {plugin}:\n")
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            print(f"Erreur lors de l'execution de la commande pour {plugin}: {e}")
            print(e.output)