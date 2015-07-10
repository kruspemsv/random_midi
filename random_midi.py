# File: random_midi.py
# Version: 1.0
#
# This program was created for randomizing MIDI notes. I found this very useful
# when mixing drums created on Guitar Pro in a DAW with a VST. Changing random
# MIDI notes like kick from 35 to 36 or snare from 40 to 38 creates a certain
# human feel.
#
# The program relies on the python midi library, which you can find here:
#     https://github.com/vishnubob/python-midi
# 
# Usage: random_midi.py <MIDI FILE> <ORIGINAL NOTE> <FINAL NOTE> [<FACTOR>]
#
# Very simple approach (at least in this version which you are using), 
# the program needs a valid MIDI file, two notes for randomization and a 
# factor number, which will dictate the frequency of changes/randominess.
# The higher the factor number goes, less changes will be made in the MIDI map.
# Using 0 as the factor number will lead a complete change from the original
# to final note.
#
# Author: Marcelo M. S. Varge (marcelo.varge@gmail.com)
#
import sys
import random

try:
    import midi
except ImportError:
    print "MIDI library was not found. Try downloading from here: https://github.com/vishnubob/python-midi"
    sys.exit(-1)

def usage():
    print "Usage: %s <MIDI FILE> <ORIGINAL NOTE> <FINAL NOTE> [<FACTOR>]" % sys.argv[0]
    sys.exit(-1)

if len(sys.argv) == 5:
    factor = int(sys.argv[4])
elif len(sys.argv) == 4:
    factor = 2
else:
    usage()

# Mapping parameters
midi_file  = sys.argv[1]
orig_note  = int(sys.argv[2])
final_note = int(sys.argv[3])

# Statistics variables
total   = 0
changes = 0

try:
    pattern = midi.read_midifile(midi_file)
except IOError:
    print "midi_file %s not found/without read permission" % midi_file
    sys.exit(-1)

for event in pattern[1]:
    if orig_note in event.data:
        total += 1
        if random.randint(0, factor) == 0:
            event.data[0] = final_note
            changes += 1

print "Total scanned notes: %d\nTotal changes: %d" % (total, changes)

midi_file_final = midi_file[:-4] + "_new" + midi_file[-4:]

midi.write_midifile(midi_file_final, pattern)

print "Create MIDI file: %s" % midi_file_final
