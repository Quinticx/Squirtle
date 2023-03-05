# Squirtle - Save the Turtles!
![squirtle](https://github.com/Quinticx/Squirtle/blob/master/savetheturtles.png)

## Idea
Squirtle is a proof of concept for a real time turtle tracker that aims to save turtles lives by warning nearby fishing ships. The turtles GPS coordinates, along with GPS from fishing vessels, are sent in to a NOAA command center. The command center then determines if the turtle and the ship are too close and sends an audio and visual alarm to the ship. This would give the ship time to pull in their nets and allow for the turtle to pass safely by.

## Component(s)
3x ESP32 (1 onboard ship, 1 onboard turtle, 1 in command center)

## Demo and Uses
![whereturt](https://media.tenor.com/R-vPpSv1jlQAAAAC/where-are-the-turtles.gif)
Below is a demonstration of how the modules interface with each other. The ESP32 on the turtle is transmitting it's location to the command center module (attached to the computer). The ESP32 on the boat is both transmitting it's location to the command center and waiting to receive a "alert" from the command center in case of nearby turtles. When the turtle is in close proximity to the ship, the command center issues an audio and visual alert to the ship via an alarm that sounds and a turtle that pops up on the ships dashboard (represented by the LCD screen on the ESP32). 

**Insert demo of turtle getting close to ship**


Insert demo of GUI

## Issues and Challenges
![nemo](https://github.com/Quinticx/Squirtle/blob/master/finding-nemo-wrong.gif)

We had several issues throughout project development. 
1. The main sea turtle tracker (https://conserveturtles.org/stctrackingmap/?id=277) requires written permission from NOAA to utilize their live location data. This made our original idea, real time plotting of sea turtles over top of current ocean surface temperatures, impossible.
2. Interfacing between multiple microcontrollers via LoRa in a metal building. To solve this, we switched our modules to utilize bluetooth instead of LoRa to aid in communication. This, however, came with it's own challenges.


## Sea Turtle Fun Facts!
1. **Green sea turtles are what they eat!** Green sea turtles are unique among sea turtles in that they are primarily herbivores, eating mostly seagrasses and algae. This diet is what gives their cartilage and fat a greenish color (not their shells), which is where their name comes from.
2. **Sand temperature is very important.** The sex of sea turtles, like many other turtles, is determined by the temperature in the nest. Cooler incubation temperatures produce male hatchlings and warmer incubation temperatures produce female hatchlings. Temperatures that fluctuate between the two extremes will produce a mix of male and female hatchlings.
![turtle](https://files.worldwildlife.org/wwfcmsprod/images/Sea_Turtle_Hol_Chan_Marine_Reserve_WW1105958/story_full_width/11e3bxo822_Sea_Turtle_Hol_Chan_Marine_Reserve_WW1105958.jpg)
3. **One sea turtle species nests during the day.** Most sea turtles nest at night—Kemp’s ridleys are the only sea turtles that routinely nest during the day. 
4. **Leatherback sea turtles have existed in their current form since the age of the dinosaurs!** Leatherbacks are highly migratory, some swimming more than 10,000 miles a year between nesting and foraging grounds. They are also accomplished divers with the deepest recorded dive reaching nearly 4,000 feet—deeper than most marine mammals. They have spiny “papillae” lining their mouth and esophagus—these spines help them trap and consume their main prey species, jellyfish. 
5. **Sea turtles don’t retract into their shells.**  Unlike other turtles, sea turtles cannot retract their flippers and head into their shells. Their streamlined shells and large paddle-shaped flippers make them very agile and graceful swimmers. In the water, their rear flippers are used as rudders, for steering.
