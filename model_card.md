# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  
**VibeSync 1.0**
---

## 2. Intended Use  

VibeSync 1.0 is designed to recommend songs based on a user's preferred genre, mood, and energy level. It assumes that users have clear preferences that can be represented through these features.

This recommender was created as a classroom simulation to demonstrate how content-based recommendation systems work. It is intended for learning and experimentation rather than real-world music streaming applications.
---

## 3. How the Model Works  

The recommender compares each song in the dataset to a user's preferences.

It looks at three features:
- Genre
- Mood
- Energy

Songs receive 40 points for a matching genre, 20 points for a matching mood, and up to 15 points based on how close the song's energy level is to the user's preferred energy.

After all songs are scored, they are sorted from highest score to lowest score. The songs with the highest scores are returned as recommendations.

Compared to the starter version, I added a weighted scoring system and included explanations showing why each song was recommended.
---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  


The dataset contains 20 songs. Each song includes information such as title, artist, genre, mood, energy, tempo, valence, danceability, and acousticness.

The current implementation uses genre, mood, and energy for scoring recommendations. One limitation is that the dataset is relatively small and some genres only have one example, which can reduce recommendation diversity.
---

## 5. Strengths  

The system works well when users have clear preferences for a genre and mood. It successfully distinguishes between different listening styles, such as high-energy pop, chill lofi, and intense rock.

The recommendations generally matched my expectations during testing. Songs that shared the user's preferred genre and mood consistently ranked near the top, showing that the scoring system captures basic musical similarity effectively.
---

## 6. Limitations and Bias 



This recommender may create a filter bubble because it strongly favors songs that match a user's existing genre preferences. Since genre contributes 40 points to the total score, songs from the preferred genre can rank highly even when other features differ significantly. The dataset is also relatively small and contains only a limited number of examples for some genres, which may reduce recommendation diversity. Additionally, the system does not currently validate user inputs, allowing unrealistic values to produce unexpected results. Finally, when a user requests a genre or mood that does not exist in the dataset, the recommender falls back to energy similarity rather than indicating that no strong matches were found.

---

## 7. Evaluation  

The recommender was tested using three normal user profiles and three edge-case profiles.

The normal profiles included High-Energy Pop, Chill Lofi, and Deep Intense Rock. The results generally matched expectations. Songs that matched both genre and mood consistently ranked at the top, while songs with similar energy values but different genres ranked lower.

For the High-Energy Pop profile, Sunrise City ranked first because it matched the user's preferred genre and mood while also having a similar energy level. For the Chill Lofi profile, Midnight Coding and Library Rain ranked highest due to strong matches across all scoring categories. For the Deep Intense Rock profile, Storm Runner ranked first because it closely matched the user's desired genre, mood, and energy.

Several edge-case tests revealed limitations. A profile requesting peaceful metal music still received Iron Verdict as the top recommendation even though its mood and energy differed significantly from the request. This occurred because genre contributes the largest portion of the score. An invalid energy value of 5.0 produced negative scores, showing that the system does not currently validate user inputs. A profile requesting a genre and mood not present in the dataset resulted in recommendations based almost entirely on energy similarity.

### Profile Comparisons

**High-Energy Pop vs. Chill Lofi**

The High-Energy Pop profile recommended upbeat songs such as Sunrise City and Gym Hero because they have high energy levels and match the user's preferred genre and mood. In contrast, the Chill Lofi profile recommended songs such as Midnight Coding and Library Rain because they have lower energy levels and match the user's preference for calmer music. This difference makes sense because the two profiles are looking for very different listening experiences.

**Chill Lofi vs. Deep Intense Rock**

The Chill Lofi profile favored relaxed, low-energy songs, while the Deep Intense Rock profile prioritized songs with intense moods and much higher energy levels. For example, Storm Runner ranked first for the rock profile because it matched both the desired genre and mood, while it did not appear near the top of the lofi recommendations. This shows that the recommender responds appropriately to changes in genre and mood preferences.

**High-Energy Pop vs. Deep Intense Rock**

Both profiles preferred energetic songs, but the recommendations differed because genre and mood have a large influence on the score. The pop profile ranked Sunrise City first due to its pop and happy characteristics, while the rock profile ranked Storm Runner first because it matched the rock and intense preferences. This demonstrates that energy alone does not determine the ranking.

### Notable Observation

Gym Hero appeared in multiple recommendation lists because it has a very high energy score and an intense mood. Even when it was not a perfect genre match, its energy level was close to what several users wanted, allowing it to rank well. This is a good example of how the scoring system balances genre, mood, and energy, but it also shows that highly energetic songs can appear frequently across different profiles.
---

## 8. Future Work  

- Add tempo and valence to the scoring system for more detailed recommendations.
- Validate user input to prevent unrealistic values from affecting results.
- Expand the dataset to include more songs, genres, and moods.
- Introduce collaborative filtering so recommendations can learn from multiple users.
- Create softer genre matching so related genres can receive partial credit instead of requiring exact matches.
---

## 9. Personal Reflection  

My biggest learning moment during this project was realizing how much the weighting of features affects recommendation results. Giving genre a large weight caused it to dominate many recommendations, even when other song characteristics did not match as closely.

AI tools were helpful for brainstorming scoring strategies, generating additional songs for the dataset, and identifying weaknesses in my recommendation logic. However, I still needed to review suggestions carefully and make sure they matched my implementation.

What surprised me most was how a relatively simple algorithm could still produce recommendations that felt reasonable. Even with a small dataset and only a few features, the system was able to generate results that matched different listening preferences.

This project helped me better understand how recommendation systems work and why real-world music platforms use much more complex data and algorithms.