import os
from flaskr import app

port = os.environ.get("PORT","5000")

app.run(host = “0.0.0”, port = int(port))