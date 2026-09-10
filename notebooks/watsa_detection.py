# Projet Watsa - AMMI 2026 - Victor
# MobileNetV2 leger pour Karawa offline
import tensorflow as tf
print("IA pour Watsa")
base = tf.keras.applications.MobileNetV2(input_shape=(128,128,3), include_top=False, weights='imagenet')
print("Modele pret -> conversion TFLite")
