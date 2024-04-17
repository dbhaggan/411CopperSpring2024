import rtmidi

# MIDI output port
midi_out = rtmidi.MidiOut()
available_ports = midi_out.get_ports()
if available_ports:
    midi_out.open_port(0)
else:
    midi_out.open_virtual_port("MyVirtualOutput")

# Send MIDI message (Note on)
note_on = [0x90, 60, 112]  # Note On message (channel 1, middle C, velocity 112)
midi_out.send_message(note_on)

# Send MIDI message (Note Off) after a delay
import time
time.sleep(1)  # Wait for 1 sec
note_off = [0x80, 60, 0]  # Note off messagee (channel 1, middle C, velocity 0)
midi_out.send_message(note_off)

# Close MIDI output port when finished
del midi_out
