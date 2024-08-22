# DVD Bouncing Logo Simulation

This Python script simulates a DVD logo bouncing around the screen, and provides a countdown of the number of bounces until it hits the corner. 

## Requirements

- Python 3.x
- `pygame` library


## Usage

To run the script, use the following command:

```bash
python dvd.py <window_width> <window_height> <logo_width> <logo_height> [--trace] [--ff]
```

### Arguments

- `window_width`: Width of the window in pixels.
- `window_height`: Height of the window in pixels.
- `logo_width`: Width of the DVD logo in pixels.
- `logo_height`: Height of the DVD logo in pixels.

### Optional Arguments

- `--trace`: Enable tracing the path of the DVD logo as it moves around the screen.
- `--ff`: Enable fast-forwarding of the simulation.

### Example

```bash
python dvd.py 1320 770 220 110 --trace --ff
```

This example runs the simulation in a 1320x770 window with a 220x110 logo, with path tracing and fast-forwarding enabled.

## Features

- **Color Change**: The logo changes colors upon hitting the edges.
- **Corner Hit Countdown**: The simulation displays the number of bounces left until the logo hits the corner.
- **Trace Mode**: Optionally trace the path of the DVD logo as it moves.
- **Fast-Forward**: Option to speed up the simulation.

## How It Works

- The script calculates the least common multiple (LCM) of the distances the logo needs to travel horizontally and vertically. This helps determine the number of steps before the logo hits the corner.
- The trace mode draws a line following the logo's movement, which can be enabled with the `--trace` option.

## Notes

- Ensure you have the necessary images (`dvd1.png`, `dvd2.png`, ..., `ultime.png`) in the same directory as the script.
- The simulation can be exited by closing the window.

## License

Free to use or edit

## Credits

This script was created as a fun demonstration of how to simulate the classic bouncing DVD logo with Python and Pygame. Enjoy!