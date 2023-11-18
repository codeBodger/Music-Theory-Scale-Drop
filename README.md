# CISC-108-Final-Project
***

### Pitch
Boulders will fall from the top of the screen.  These boulders will have sheet
music of scales on them.  The user will have to use the keyboard to choose what
type of scale it is (Major/minor).  There will be a settings menu where the user
can choose which scales (Major, Natural minor, Harmonic minor, Melodic minor,
Mixolydian, Whole Tone, etc.), key signatures (Number of sharps/flats), clefs
(Treble, Bass, Alto, Tenor, etc.), and amount of ledger lines they want. If the
boulders land before the user has figured out what type of scale it is, they
loose 10 points.  One point is awarded for each scale correctly identified on
the first try.  Subsequent tries reduce the points awarded by 50%.  The arrow
keys are used to select different falling boulders, so that if/when there are
multiple falling at the same time, the user can tell the game which one they are
guessing.  

### Milestones
#### Milestone 1: *[Video Link](https://youtu.be/jAdGS6ejogo)*
- [x] Create a boulder class
  - [x] Create the boulders randomly at the top of the screen
  - [x] Make the boulders fall
  - [x] Allow the user to select different boulders using the L/R arrow keys
  - [x] When a boulder hits the bottom of the screen, decrease the score by 10
        and remove the boulder object
- [x] Create a scale class
  - [x] Store scale objects in boulder objects
  - [x] When a boulder is selected and a scale key is pressed, check if it
        corresponds with the right scale type.  If it does, remove the boulder
        and add the proper amount to the score.  If it doesn't (and a valid
        key was pressed), decrease the value of the boulder by 50%.  
  - [x] Generate the scale type, etc. randomly
- [x] For this milestone, we'll just display a list of note names without
      octave numbers.  

#### Milestone 2
- [x] Figure out some way to display the sheet music for the scales, given a
      type, starting note, and clef
  - [x] Ensure that the scales are displayed on top of the boulders
  - [x] Ensure that the scales fall with the boulders
  - [x] Ensure that scales fit within the specs of the default settings
- [x] Increase the speed that the boulders fall as the player gets more correct
- [x] If the player presses `escape`, end the game
- [x] Display the score to the user near the right of the screen
- [x] Display a list with the keys that correspond to each scale type below the
      score
- [x] Automatically generate the boulders, rather than requiring the player to
      press `space` to generate them
- [x] If the player presses `space`, pause the game and hide the scales

#### Milestone 3
- [ ] Create a settings menu
  - [ ] Allow the user to enter the settings menu
  - [ ] Allow the user to select different types of scale
  - [ ] Allow the user to select different clefs
  - [ ] Allow the user to select different key signatures
  - [ ] Allow the user to select different amounts of ledger lines
  - [ ] Allow the user to return from the settings menu
- [ ] Ensure that the scales fit within the specs of the user-defined settings
- [ ] There's no end condition in the game, but we'll allow the user to set one
      in the settings menu
- [ ] Note, the settings menu will be controlled using the number or arrow keys
      and the return key

***
### My Info
- Name: `Rowan Ackerman`
- Email: `rnackerm@udel.edu`
