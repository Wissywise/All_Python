current_mode = 1  # 1: Normal Mode, 2: Power Saving Mode, 3: Performance Mode

if current_mode == 1:
    print("Device is operating in Normal Mode.")
elif current_mode == 2:
    print("Device is operating in Power Saving Mode.")
elif current_mode == 3:
    print("Device is operating in Performance Mode.")
else:
    print("Invalid mode")