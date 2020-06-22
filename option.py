import argparse

def parser():
    usage="pipenv run python filemain.py <firstarg(sentence or filename)>"
    parser=argparse.ArgumentParser(usage=usage)
    parser.add_argument("firstarg")

    return parser.parse_args()
