from controller import Robot

def run_robot(robot):

    time_step =  32
    max_speed = 6.28

    left_motor = robot.getMotor('left wheel motor')
    right_motor = robot.getMotor('right wheel motor')
    left_motor.setPosition(float('inf'))
    right_motor.setPosition(float('inf'))
    left_motor.setVelocity(0.0)
    right_motor.setVelocity(0.0)

    left_ir = robot.getDistanceSensor('ir0')
    left_ir.enable(time_step)
    right_ir = robot.getDistanceSensor('ir1')
    right_ir.enable(time_step)

    while robot.step(time_step) != -1:

        left_ir_value = left_ir.getValue()
        right_ir_value = right_ir.getValue()
        print("Left IR Value:", left_ir_value, "Right IR Value:", right_ir_value)
    
        left_speed = max_speed * 0.25
        right_speed = max_speed * 0.25

        if (left_ir_value > right_ir_value) and (140 < left_ir_value < 175):
            left_speed = -max_speed * 0.25
            
        elif (right_ir_value > left_ir_value) and (140 < right_ir_value < 175):
            right_speed = -max_speed * 0.25    

        left_motor.setVelocity(left_speed)
        right_motor.setVelocity(right_speed)

if __name__ == "__main__":
    my_robot = Robot()
    run_robot(my_robot)
