export FLASK_APP=server.py
debug_val=${1:-0}
export FLASK_DEBUG=$debug_val
flask run