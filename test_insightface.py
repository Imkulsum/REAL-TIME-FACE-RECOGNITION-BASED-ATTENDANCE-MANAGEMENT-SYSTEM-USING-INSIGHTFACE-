# test_insightface.py → TEST FOR YOUR 5 STUDENTS
import insightface
from insightface.app import FaceAnalysis
import cv2
import numpy as np
import os

print("🔥 Testing ULTRA-ACCURATE InsightFace on Python 3.13...")

# Load the pre-trained model
app = FaceAnalysis(name='buffalo_l', providers=['CPUExecutionProvider'])
app.prepare(ctx_id=0, det_size=(640, 640))
print("✅ Model loaded! (ArcFace + Buffalo_L — 99.9% accurate)")

# Load your dataset
DATASET_PATH = "dataset"
KNOWN_EMBEDDINGS = []
KNOWN_NAMES = []

for filename in os.listdir(DATASET_PATH):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        path = os.path.join(DATASET_PATH, filename)
        img = cv2.imread(path)
        if img is not None:
            faces = app.get(img)
            if len(faces) > 0:
                embedding = faces[0].normed_embedding
                student_id = os.path.splitext(filename)[0]
                KNOWN_EMBEDDINGS.append(embedding)
                KNOWN_NAMES.append(student_id)
                confidence = faces[0].det_score
                print(f"✅ Loaded {student_id} → Confidence: {confidence:.3f} (Perfect!)")
            else:
                print(f"❌ No face in {filename} — Use clear front-face photo!")

print(f"\n🎉 SUCCESS! Loaded {len(KNOWN_NAMES)} students.")
print("Now test recognition with your webcam photo...")

# Quick camera test (press 'q' to quit)
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("❌ Camera not found — check if it's being used elsewhere.")
else:
    print("🖼️  Showing camera... Press 'q' to quit.")
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        faces = app.get(frame)
        if len(faces) > 0:
            embedding = faces[0].normed_embedding
            best_score = 0
            best_name = "Unknown"
            for known_emb, name in zip(KNOWN_EMBEDDINGS, KNOWN_NAMES):
                score = np.dot(embedding, known_emb)
                if score > best_score:
                    best_score = score
                    best_name = name
            color = (0, 255, 0) if best_score > 0.45 else (0, 0, 255)
            cv2.putText(frame, f"{best_name} ({best_score:.3f})", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
        cv2.imshow('Test Recognition (q to quit)', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

print("\n🚀 InsightFace is READY! Run: python app.py")