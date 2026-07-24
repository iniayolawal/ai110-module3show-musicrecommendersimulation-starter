# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Explain your design in plain language.

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
- What information does your `UserProfile` store
- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend


This project uses a content-based recommendation system to suggest songs based on a user's musical preferences. Instead of looking at what other users enjoy, the system compares the attributes of each song to a user's preferred attributes and recommends the closest matches.

### Song Features

Each `Song` in the system stores:

* Genre
* Mood
* Energy
* Tempo (BPM)

These features help describe the style, feeling, and intensity of a song.

### UserProfile Information

Each `UserProfile` stores a user's preferred:

* Genre
* Mood
* Energy level
* Tempo (BPM)

These preferences represent the type of music the user wants to hear.

### Algorithm Recipe

The recommender evaluates every song in the dataset and assigns a score based on how closely it matches the user's preferences.

Scoring rules:

* Genre match: up to 40 points
* Mood match: up to 20 points
* Energy similarity: up to 15 points
* Tempo similarity: up to 15 points
* Valence similarity: up to 10 points

Genre and mood are used as categorical features, while energy, tempo, and valence are compared to the user's target values. Songs that are closer to the user's preferred values receive higher scores.

After every song receives a score, the songs are ranked from highest score to lowest score. The recommender then returns the top-scoring songs as recommendations.

### Potential Biases

Because this is a content-based recommendation system, it may favor songs that closely match a user's existing preferences. Songs from different genres may be ranked lower even if they share similar moods or musical characteristics. This could reduce music discovery and create a filter bubble where users are repeatedly recommended similar types of songs.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:
## Sample Recommendation Output

```text
Loaded songs: 20

Top recommendations:

Sunrise City - Score: 74.70
Because: genre match (+40), mood match (+20), similar energy (+14.7)

Gym Hero - Score: 53.05
Because: genre match (+40), similar energy (+13.1)

Rooftop Lights - Score: 34.40
Because: mood match (+20), similar energy (+14.4)

Circuit Bloom - Score: 15.00
Because: similar energy (+15.0)

Concrete Dreams - Score: 14.25
Because: similar energy (+14.3)
```

```
# e.g.:
# User profile: genre=indie, mood=chill, energy=low
# Recommendations:
#   1. ...
#   2. ...
#   3. ...
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



