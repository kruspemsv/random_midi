# random_midi.py
MIDI Human/Randomizer Program

File: random_midi.py
Version: 1.0

This program was created for randomizing MIDI notes. I found this very useful
when mixing drums created on Guitar Pro in a DAW with a VST. Changing random
MIDI notes like kick from 35 to 36 or snare from 40 to 38 creates a certain
human feel.

The program relies on the python midi library, which you can find here:
https://github.com/vishnubob/python-midi
 
Usage: random_midi.py MIDI FILE ORIGINAL NOTE FINAL NOTE FACTOR

Very simple approach (at least in this version which you are using), 
the program needs a valid MIDI file, two notes for randomization and a 
factor number, which will dictate the frequency of changes/randominess.
The higher the factor number goes, less changes will be made in the MIDI map.
Using 0 as the factor number will lead a complete change from the original
to final note.

Author: Marcelo M. S. Varge (marcelo.varge@gmail.com)
