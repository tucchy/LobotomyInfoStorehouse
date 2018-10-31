import os
<<<<<<< HEAD
from flaskr import app

port = os.environ.get("PORT","5000")

app.run()
#app.run(host = "0.0.0", port = int(port))
=======
from flaskr import app

port = os.environ.get("PORT","5000")

app.run(host = “0.0.0”, port = int(port))
>>>>>>> deaf5170b67f2fbaea7ec5638cdc36dc47b81ce0
