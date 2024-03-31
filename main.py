import truss
from pathlib import Path
import requests

tr = truss.load("./google_bert_truss")
command = tr.docker_build_setup(build_dir=Path("./google_bert_truss"))
print(command)
