import argparse

def parse_args():
    p = argparse.ArgumentParser(description="Cosas")
    p.add_argument("-s","--saludo", required=True, help="Ruta al CSV de entrada")
    p.add_argument("-c","--chiste", required=False, help="Chiste")

    return p.parse_args()

args = parse_args()
print(args.saludo)
if args.chiste:
    print(args.chiste)