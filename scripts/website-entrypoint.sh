set -e

PYTHON="python -O"

export FLASK_APP=run.py
APP="exec ${PYTHON} run.py"


${APP} run --port ${FLASK_PUBLIC_PORT} --host "0.0.0.0"
