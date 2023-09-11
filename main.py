import argparse
from Package_Windows.ManagePlugin import ManagePlugin
from Package_Windows.ManageRegister import ManageRegister

def main():
    # Initialisation du parser d'arguments
    parser = argparse.ArgumentParser(description="FFF - Find Forensic Faster.")
    parser.add_argument("-f", "--file", required=True, help="Chemin vers le fichier dump à analyser.")
    parser.add_argument("-p", "--path", default="volatility3",
                        help="Chemin vers le dossier qui contient vol.py de Volatility. Par défaut: 'volatility3-develop'")
    parser.add_argument("-os", "--ostype", default="windows",
                        help="Le type du système d'exploitation: 'windows' ou 'linux'.'")

    args = parser.parse_args()

    if args.ostype == 'windows':
        register = ManageRegister(args)
        # register.execute()
        plugins = ManagePlugin(args)
        plugins.execute()

    elif args.ostype == 'linux':
        print("en cours de travaux")
        #putsomecode

    else:
        print("Wrong ostype")


if __name__ == "__main__":
    main()
