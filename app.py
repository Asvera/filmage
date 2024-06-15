from flask import Flask, request, send_file ,jsonify
from filter import apply_filter

app = Flask(__name__)

filter_available = [
    "blur" ,
    "contour" ,
    "detail" ,
    "edge_enhance" ,
    "edge_enhance_more" ,
    "emboss" ,
    "find_edges" ,
    "sharpen" ,
    "smooth" ,
    "smooth_more" ,
]

@app.route("/",methods=["GET","POST"])
def index():
    # res = "helo"
    res = {
        "filter_available": filter_available,
        "usage" : { "http_method" : "POST" , "URL" : "/<filter_available>/" },
    }
    return jsonify(res)

@app.post("/<filter>")
def image_filter(filter):
    if filter not in filter_available:
        res = {"error":"incorrect filter"}
        return jsonify(res)

    file = request.files["Image"]
    if not file:
        res = { "error" : "no file provided" }
        return jsonify(res)

    filted_image = apply_filter(file,filter)
    return send_file(filted_image,mimetype="image/JPEG")


if __name__ == "__main__":
    app.run()

