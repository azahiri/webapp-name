
@app.route("/") #@ sign before function is decorater/ it tells you what route you are going to add to the root url
def index():
    return render_template("index.html")


@app.route("/hello/")
@app.route("/hello/<name>")
def hello(name=None):
    if name:
        name = name.upper()
    return render_template("hello.html", name=name)


@app.route("/calc/", methods=["GET", "POST"])
def calculate():
    if request.method == "POST":
        a = request.form["a"]
        
        # root_1, root_2 = quadratic(a, b, c)
        result = []
        if result:
            return render_template(
                "calculator_result.html", a=a, result = result
            )
        else:
            return render_template("calculator_form.html", error=True)
    return render_template("calculator_form.html", error=None)
