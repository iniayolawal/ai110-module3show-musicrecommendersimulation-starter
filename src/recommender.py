import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Load songs from a CSV file into a list of dicts."""
    songs: List[Dict] = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Skip blank/whitespace-only rows.
            if not row.get("id") or not row["id"].strip():
                continue
            songs.append({
                "id": int(row["id"]),
                "title": row["title"],
                "artist": row["artist"],
                "genre": row["genre"],
                "mood": row["mood"],
                "energy": float(row["energy"]),
                "tempo_bpm": float(row["tempo_bpm"]),
                "valence": float(row["valence"]),
                "danceability": float(row["danceability"]),
                "acousticness": float(row["acousticness"]),
            })
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Score a single song against user preferences, returning (score, reasons)."""
    score = 0.0
    reasons: List[str] = []

    # Genre match = +40 points
    if user_prefs["genre"] == song["genre"]:
        score += 40
        reasons.append("genre match (+40)")

    # Mood match = +20 points
    if user_prefs["mood"] == song["mood"]:
        score += 20
        reasons.append("mood match (+20)")

    # Energy similarity = up to 15 points
    energy_points = 15 * (1 - abs(song["energy"] - user_prefs["energy"]))
    score += energy_points
    reasons.append(f"similar energy (+{round(energy_points, 1)})")

    return (score, reasons)

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Score, rank, and return the top k song recommendations for a user."""
    recommendations: List[Tuple[Dict, float, str]] = []

    # Score every song and build a readable explanation from its reasons.
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = ", ".join(reasons)
        recommendations.append((song, score, explanation))

    # Sort by score, highest first, and return the top k.
    ranked = sorted(recommendations, key=lambda rec: rec[1], reverse=True)
    return ranked[:k]
