# Static Countdown Timer
This is a little timer that pops up on the upper left corner or your screen and, from a preset time, counts down to zero and then dissapears.

## Configuration:
Use the css stylesheet found under `config/styles.css` to edit the appearance of the timer (color, font, size, ...)

Note: If you want to change the on screen position of the timer, modify the pop-up coordinates in the `src/StaticCountdownTimer.py` file.

## Use:
I use this timer within Streamer.bot with a "Run a Program" sub-action.

The bot switches to a target directory and, in a separate shell, runs:

```
.static_countdown_timer_venv\Scripts\python.exe .\src\StaticCountdownTimer.py <timer-title> <countdown-time>
```

The arguments to pass are, in order:
  - The timer title. If you want to include spaces in the title encase it between quotation marks.
  - The timer total countdown time in seconds. The timer will convert it to minutes and seconds automatically.

An example would be:
```
.static_countdown_timer_venv\Scripts\python.exe .\src\StaticCountdownTimer.py "Pretty timer" 120
```

Which would give:

<img width="388" height="137" alt="image" src="https://github.com/user-attachments/assets/d53d9612-b719-405b-8308-23066a8c03a3" />

