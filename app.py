from flask import Flask, render_template, request

app = Flask(__name__, template_folder="templates")



if __name__ == "__main__":
    app.run()
    # app.run(debug=True)