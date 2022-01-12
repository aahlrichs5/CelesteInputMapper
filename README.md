# CelesteInputMapper

A program that reads inputs and converts them to keystrokes for the game Celeste.
Run the program's main file and begin inputting commands to make Madeline move. Be sure to tab into the game within the sleep time window so that commands will be registered by the game. When finished with the program input 'Q' to terminate it.

# Movement Commands

- wr | wl
  - Walks right or left
- dar | dal
  - Dashes right or left
- daur | daul
  - Dashes up and right or up and left
- dadr | dadl
  - Dashes down and right or down and left
- ju | jr | jl
  - Jumps up, left, or right
- h
  - Holds the current position (pauses input)
- gw
  - Grabs walls until futher notice
- rw
  - Releases grab on a wall

# Menu Commands

- retry
  - Retrys the current room
- restart
  - Restarts the chapter
- skip
  - Skips the current dialogue or cutscene
- map
  - Goes to the map screen
- save
  - Saves the game
- c
  - Presses the 'C' key to confirm in menus
- d
  - Presses the 'd' key to go back in menus
- up
  - Presses the up arrow to navigate menus
- down
  - Presses the down arrow to navigate menus
- q
  - Quits the program with normal termination

# Example Movement Commands

- Time in movements
  - All movements without times are default 30 frames (0.5 seconds)
  - By adding a number you may specify the amount of frames to do the move for
- wl
  - Walks left for 30 frames
- daur 60
  - Dashes up and right for 60 frames
- wl,h, ju 10,daur,gw
  -Walks left, holds position, jumps up for 10 frames, dashes up and right, and grabs wall
