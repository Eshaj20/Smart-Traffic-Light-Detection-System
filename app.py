from flask import Flask, render_template, jsonify
import threading
import time
from detect_traffic import detect_traffic_lights, get_light_color
from camera import capture_video
from vehicle_control import move_vehicle

app = Flask(__name__)

# Global variable to store the current traffic light color
current_color = "Red"  # Default to Red

def video_thread():
    cap = capture_video()
    while True:
        ret, frame = cap.read()  # Capture frame
        if not ret:
            break

        # Detect traffic light color
        results = detect_traffic_lights(frame)
        global current_color
        current_color = get_light_color(results)

        # Control vehicle movement based on the color
        move_vehicle(current_color)

        # Display frame (optional)
        cv2.imshow('Traffic Light Detection', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to quit
            break

    cap.release()
    cv2.destroyAllWindows()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/status')
def get_status():
    return jsonify({"traffic_light": current_color})

if __name__ == '__main__':
    # Start the video capture thread
    threading.Thread(target=video_thread, daemon=True).start()
    app.run(host='0.0.0.0', port=5000)
