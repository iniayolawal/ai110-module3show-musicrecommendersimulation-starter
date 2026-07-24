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
* 

These features help describe the style, feeling, and intensity of a song.

### UserProfile Information

Each `UserProfile` stores a user's preferred:

* Genre
* Mood
* Energy level


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

```
Loaded songs: 20

====================
High-Energy Pop
====================
Sunrise City - Score: 74.55
Because: genre match (+40), mood match (+20), similar energy (+14.5)

Gym Hero - Score: 53.80
Because: genre match (+40), similar energy (+13.8)

Rooftop Lights - Score: 33.65
Because: mood match (+20), similar energy (+13.7)

Concrete Dreams - Score: 15.00
Because: similar energy (+15.0)

Circuit Bloom - Score: 14.25
Because: similar energy (+14.3)


====================
Chill Lofi
====================
Midnight Coding - Score: 74.70
Because: genre match (+40), mood match (+20), similar energy (+14.7)

Library Rain - Score: 74.25
Because: genre match (+40), mood match (+20), similar energy (+14.2)

Focus Flow - Score: 55.00
Because: genre match (+40), similar energy (+15.0)

Spacewalk Thoughts - Score: 33.20
Because: mood match (+20), similar energy (+13.2)

Coffee Shop Stories - Score: 14.55
Because: similar energy (+14.5)


====================
Deep Intense Rock
====================
Storm Runner - Score: 74.85
Because: genre match (+40), mood match (+20), similar energy (+14.8)

Gym Hero - Score: 34.55
Because: mood match (+20), similar energy (+14.5)

Iron Verdict - Score: 33.95
Because: mood match (+20), similar energy (+14.0)

Neon Pulse - Score: 14.40
Because: similar energy (+14.4)

Concrete Dreams - Score: 14.25
Because: similar energy (+14.2)


Top recommendations:

Storm Runner - Score: 74.85
Because: genre match (+40), mood match (+20), similar energy (+14.8)

Gym Hero - Score: 34.55
Because: mood match (+20), similar energy (+14.5)

Iron Verdict - Score: 33.95
Because: mood match (+20), similar energy (+14.0)

Neon Pulse - Score: 14.40
Because: similar energy (+14.4)

Concrete Dreams - Score: 14.25
Because: similar energy (+14.2)
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

This project helped me understand how recommendation systems transform user preferences into ranked suggestions. By building a content-based recommender from scratch, I learned how song features such as genre, mood, and energy can be converted into numerical scores that determine which songs are recommended. I also saw how the choice of feature weights can significantly influence results. For example, giving genre a high weight made it one of the strongest factors in determining recommendations.

Another important lesson was that even simple algorithms can produce recommendations that feel personalized. At the same time, testing edge cases showed the limitations of a basic recommender. The system could become biased toward familiar genres, struggle with unknown preferences, and produce unexpected results when given invalid inputs. These experiments helped me better understand why real-world recommendation systems use larger datasets, additional features, user feedback, and more sophisticated algorithms to improve accuracy and diversity.



