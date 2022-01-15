from flask import Flask, redirect,request,render_template, url_for
import RPi.GPIO as GPIO
app = Flask(__name__)

@app.route("/lamba_ras")
def website():
    return render_template("index.html")
@app.route("/yak",methods=["POST","GET"])
def yak():
    GPIO.output(pin,GPIO.HIGH)
    return redirect(url_for("website"))

@app.route("/kapat",methods=["POST","GET"])
def kapat():
    GPIO.output(pin,GPIO.LOW)
    print("Kapat")
    return redirect(url_for("website"))

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

if __name__ == "__main__":
    app.run()