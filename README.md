# 🛤️ e-puck Line Follower Robot (Webots Simulation)

This project features a line-following robot using the **e-puck platform**, simulated in **Webots**. The robot uses two downward-facing infrared sensors to detect a line and follow it based on reflectivity differences.

## ⚙️ Features

- **Threshold-based line-following behavior** using two ground-facing IR sensors (`ir0` and `ir1`).
- Simulated in **Webots**, a professional and open-source robot simulator.
- Uses **sensor feedback comparison** (not binary detection) to follow the path.
- **Simple and effective controller logic** using Python and Webots API.
- Designed for **smooth turning and real-time correction**.

## 📷 Sensor Setup

- `ir0`: Left ground sensor  
- `ir1`: Right ground sensor  
- Values indicate surface reflectivity (typically low on dark lines, higher on bright floor).

## 🧠 Algorithm

The line-following behavior is driven by comparing the two IR sensor values and acting when either sensor detects reflectivity **within a specific range** (140 to 175 in this case).

### Logic Flow

- Read analog values from both left (`ir0`) and right (`ir1`) IR ground sensors.
- Set both wheel speeds to a base forward speed.
- If:
  - **Left sensor value > Right**, and within threshold → steer **left** by reversing left wheel slightly.
  - **Right sensor value > Left**, and within threshold → steer **right** by reversing right wheel slightly.
- This creates a gentle correction to stay aligned with the line.

```python
if (left_ir_value > right_ir_value) and (140 < left_ir_value < 175):
    left_speed = -max_speed * 0.25  # Turn left

elif (right_ir_value > left_ir_value) and (140 < right_ir_value < 175):
    right_speed = -max_speed * 0.25  # Turn right
