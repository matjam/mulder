from mulder import app
from mulder.controller import index


app.add_url_rule("/", "index", index)
