# :page_with_curl: Postmortem
### Overview:
The objective of this project was to write a postmortem for a system outage or system issue as practice. The postmortem was about a made-up issue using a standard postmortem format to document the issues faced, the resolution, the timeline, and preventative measures in the future.
# :video_game: Arcuz (Java game)
I made [this](https://github.com/Ookanuki/Apo2-Proyect) fight game from scratch in my tirth semester in the university using java. Actually is full of bugs. In this ocasion I'll talk about a but that makes finish after some attacks.
## :date: Date:
2020-05-24
## :keyboard: Authors:
Jhonatan Arenas <cybernuki \ Ookanuki>
##  :red_circle: Status:
Not solved
## :page_facing_up: Issue Summary:
An issue was detected today at 7:35 pm. The game is done when the player reach the boss and keep touched space (attack action) button.  This made the player loose the game even with its full life and without hurts the boss. The root cause appears to be the boss' reach system that find the location of the player. Also, it appears to be related with the event pool designed who hasn't a restriction to deal with pressed keys.
## :clock930: Timeline:
05/24 7:30 pm -  I ran the game program. <br>
05/24 7:31 pm - I created a new match. <br>
05/24 7:33 pm - I reach the boss without being hurt. <br>
05/24 7:34 pm - I keep pressed space button to attack. <br>
05/24 7:35 pm - Game over alert appears and game is closed. <br>
## :bug: Root Cause:
After some input tests and debbuging, I found that the error happens due the research function that allows the monster get the player. As the function set boss' direction and then move n pixels, there are some directions that basically broke the logic of the setting. Moreover, due keeping pressed the space button is not controlled by a timer, this causes that even if the player is in front of the boss, systems do evaluations in a states where boss moves even if the logic says that is not allowed to move.
## :bar_chart: Preventive Measure:
Improve infrastructure of the code in order of reduce the number of issues but also to scale and debug.

Actions items:
-  Use design patters to representate the abstraction of the entities of the game
- Find or improve the research operation of the monsters players
- Implement an improvement system to the game.

## :wrench: Supporting information:
No supporting information at this time
