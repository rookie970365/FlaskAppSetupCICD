"""
jkkkkjdsfcxvmm
"""
from flask import Flask, request, render_template

from views.products import products_app

app = Flask(__name__)  # __name__ имя текущего модуля

app.config.update(
    ENV="development",
    SECRET_KEY="sdkjnslkdfgnajrsgoiqejrogj3qo4itgj",
)

app.register_blueprint(products_app, url_prefix="/products")


def print_request():
    """
    LLLLLLLLLLLLLL
    :param
    :return:
    """
    print("request:", request)
    print("request.method", request.method)
    print("request.path", request.path)


@app.route("/")
def hello_world():
    """
    LLLLLLLLLLLLLL
    :param
    :return:
    """
    return render_template("index.html")
    # return render_template("base.html")


@app.route("/hello/")
@app.route("/hello/<name>/")
def hello_view(name: str = None):
    """
    LLLLLLLLLLLLLL
    :param
    :return:
    """
    print_request()
    if name is None:
        name = request.args.get("name", "")
    name = name.strip()  # убираем пробелы слева и справа
    if not name:
        name = "World"
    return {"message": f"Hello {name}!"}


@app.route("/items/<int:item_id>/", endpoint='get_item')
def get_item(item_id: int):
    """
    LLLLLLLLLLLLLL
    :param item_id:
    :return:
    """
    return {
        "item": {"id": item_id},
    }


@app.route("/items/<item_id>/")
def get_item_string(item_id: str):
    """
    LLLLLLLLLLLLLL
    :param item_id:
    :return:
    """

    return {
        "item_id": item_id.upper(),
    }


#
# # @app.route("/hello/<name>/")
# # def hello_name(name: str):
# #     return {"message": f"Hello {name}!"}
#


if __name__ == "__main__":
    app.run(debug=True)
