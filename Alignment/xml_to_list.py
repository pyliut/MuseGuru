# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 17:05:00 2022

@author: pyliu
"""
import music21 as m21

def xml_to_list(xml):
    """Convert a music xml file to a list of note events

    Notebook: C1/C1S2_MusicXML.ipynb

    Args:
        xml (str or music21.stream.Score): Either a path to a music xml file or a music21.stream.Score

    Returns:
        score (list): A list of note events where each note is specified as
            ``[start, duration, pitch, velocity, label]``
    """

    if isinstance(xml, str):
        xml_data = m21.converter.parse(xml)
    elif isinstance(xml, m21.stream.Score):
        xml_data = xml
    else:
        raise RuntimeError('midi must be a path to a midi file or music21.stream.Score')

    score = []

    for part in xml_data.parts:
        instrument = part.getInstrument().instrumentName

        for note in part.flat.notes:

            if note.isChord:
                start = note.offset
                duration = note.quarterLength
                secs = note.seconds

                for chord_note in note.pitches:
                    pitch = chord_note.ps
                    volume = note.volume.realized
                    score.append([start, secs,duration, pitch, volume, instrument])

            else:
                start = note.offset
                duration = note.quarterLength
                pitch = note.pitch.ps
                volume = note.volume.realized
                secs = note.seconds
                score.append([start, secs, duration, pitch, volume, instrument])

    score = sorted(score, key=lambda x: (x[0], x[3]))
    return score