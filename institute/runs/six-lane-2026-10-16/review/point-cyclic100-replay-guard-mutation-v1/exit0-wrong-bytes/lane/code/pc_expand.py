from pathlib import Path
import sys
Path(sys.argv[2]).write_text("wrong certificate bytes\n")
