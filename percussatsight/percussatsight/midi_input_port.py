import rtmidi

def callback(message, timestamp):
    print("MIDI message received:", message)

midi_in = rtmidi.MidiIn()
midi_in.set_callback(callback)

available_ports = midi_in.get_ports()
if available_ports:
    midi_in.open_port(0)
else:
    midi_in.open_virtual_port("virtualInput")
