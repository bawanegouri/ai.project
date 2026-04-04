from flask import Flask, render_template, request

app = Flask(__name__)

# Rule-based crop recommendation
def recommend_crop(soil, rainfall, season):

    if soil == "black" and rainfall == "high":
        return "Cotton"

    elif soil == "red" and rainfall == "medium":
        return "Groundnut"

    elif soil == "alluvial" and season == "rabi":
        return "Wheat"

    elif soil == "clay" and rainfall == "high":
        return "Rice"

    elif soil == "Black Soil" and season == "Kharif":
        return "Maize"
    
    elif soil == "Alluvial Soil" and rainfall == "High":
        return "Sugarcane"
    
    elif soil == "Red Soil" and season == "Summer":
        return "Millet"
    
    elif soil == "Clay Soil" and season == "Kharif":
        return "Soybean"
    else:
        return "No suitable crop found"


@app.route("/", methods=["GET","POST"])
def home():

    crop = ""

    if request.method == "POST":

        soil = request.form["soil"]
        rainfall = request.form["rainfall"]
        season = request.form["season"]

        crop = recommend_crop(soil, rainfall, season)

    return render_template("index.html", crop=crop)


if __name__ == "__main__":
    app.run(debug=True)