import time

# Start the timer
start_time = time.time()

try:
    while True:
        # Calculate the elapsed time
        elapsed_time = int(time.time() - start_time)

        # Format the elapsed time as HH:MM:SS
        hours = elapsed_time // 3600
        minutes = (elapsed_time % 3600) // 60
        seconds = elapsed_time % 60

        # Display the timer in the terminal
        print(f'\rTimer: {hours:02}:{minutes:02}:{seconds:02}', end='')

        # Wait for 1 second before updating
        time.sleep(1)
except KeyboardInterrupt:
    print("\nTimer stopped.")
