# -*- coding: utf-8 -*-
"""
Diese Datei sollte nicht verändert werden und wird von uns gestellt und zurückgesetzt.

Skript testet das neu trainierte Modell


@author: Maurice Rohr
"""

from predict import predict_labels
from wettbewerb import load_references, save_predictions


ecg_leads,ecg_labels,fs,ecg_names = load_references('../test/') # Importiere EKG-Dateien, zugehörige Diagnose, Sampling-Frequenz (Hz) und Name                                                # Sampling-Frequenz 300 Hz

predictions = predict_labels("model.npy",ecg_leads,fs,ecg_names)

save_predictions(predictions) # speichert Prädiktion in CSV Datei