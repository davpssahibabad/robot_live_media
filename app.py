from flask import Flask, render_template, Response, request, redirect, url_for
# ... rest of your imports and GPIO / camera setup ...

app = Flask(__name__)

@app.route('/')
def home():
    # UP cities list + robot description
    return render_template('home.html')

@app.route('/ghaziabad', methods=['GET', 'POST'])
def ghaziabad():
    if request.method == 'POST':
        action = request.form.get('light_action')
        if action == 'on':
            GPIO.output(HEADLIGHT_PIN, GPIO.HIGH)
        elif action == 'off':
            GPIO.output(HEADLIGHT_PIN, GPIO.LOW)
        return redirect(url_for('ghaziabad'))

    motion_detected = GPIO.input(PIR_PIN) == GPIO.HIGH
    amb_temp = thermal.get_amb_temp()
    obj_temp = thermal.get_obj_temp()

    return render_template(
        'ghaziabad.html',
        motion=motion_detected,
        amb_temp=f"{amb_temp:.1f}",
        obj_temp=f"{obj_temp:.1f}",
        headlight_on=GPIO.input(HEADLIGHT_PIN) == GPIO.HIGH
    )

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

# ... rest of app.py (patrol loop, cleanup, app.run) ...
