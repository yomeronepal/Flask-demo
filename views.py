from settings import app


@app.route("/test/")
def test():
    return "This is just test"
