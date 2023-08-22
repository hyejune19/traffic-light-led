import os
import time

def export_gpio(gpio):
    gpio_path = f"/sys/class/gpio/gpio{gpio}"
    if not os.path.exists(gpio_path):
        try:
            with open("/sys/class/gpio/export", "w") as f:
                f.write(str(gpio))
        except IOError as e:
            print(f"Error exporting GPIO {gpio}: {e}")
            return False
    return True

def set_gpio_value(gpio, value):
    gpio_path = f"/sys/class/gpio/gpio{gpio}/value"
    with open(gpio_path, "w") as f:
        f.write(str(value))

def main():
    gpio_89 = 89
    gpio_90 = 90
    gpio_66 = 66

    if not export_gpio(gpio_89) or not export_gpio(gpio_90) or not export_gpio(gpio_66):
        return

    set_gpio_value(gpio_89, 0)
    set_gpio_value(gpio_90, 0)
    set_gpio_value(gpio_66, 0)

    try:
        while True:
            set_gpio_value(gpio_89, 1)
            time.sleep(5)

            set_gpio_value(gpio_89, 0)
            set_gpio_value(gpio_90, 1)
            time.sleep(2)

            set_gpio_value(gpio_90, 0)
            set_gpio_value(gpio_66, 1)
            time.sleep(5)

            set_gpio_value(gpio_66, 0)

    except KeyboardInterrupt:
        set_gpio_value(gpio_89, 0)
        set_gpio_value(gpio_90, 0)
        set_gpio_value(gpio_66, 0)

if __name__ == "__main__":
    main()
