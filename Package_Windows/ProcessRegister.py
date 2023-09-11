import subprocess

class ProcessRegister:
    def __init__(self, image_path, folder_vol_path):
        self.image_path = image_path
        self.folder_vol_path = folder_vol_path

    def run(self, register):
        cmd = ["python", f"{self.folder_vol_path}/vol.py", "-f", self.image_path, "windows.registry.printkey.PrintKey", "--key", register]
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            print(f"Resultat pour {register}:\n")
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            print(f"Erreur lors de l'execution de la commande pour {register}: {e}")
            print(e.output)