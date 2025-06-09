# Movie Recommender System

This project is a **content-based movie recommender system** built in Python using the TMDB dataset, which contains over 5,000 movies. The goal is to help users discover movies similar to their favorites by analyzing movie metadata and features.

## Features

* Utilizes **content-based filtering** to recommend movies based on similarity to the user’s selected movie.
* Applies **vectorization techniques** to transform movie attributes into numerical representations for comparison.
* Built with popular Python libraries like **NumPy, Pandas, Scikit-learn** for data processing, and **Matplotlib, Seaborn** for visualization.
* Interactive and user-friendly interface developed using **Streamlit**, allowing users to easily input movie titles and view recommendations.
* Developed using **PyCharm** IDE.

## How It Works

The recommender analyzes movie features such as genres, keywords, cast, and crew, converting them into numerical vectors. It then calculates similarity scores between movies to suggest titles that are most alike to the user’s input, providing personalized and relevant recommendations.

## How to Use

1. Clone the repository and download the TMDB dataset (included).
2. Install required Python libraries (see requirements.txt if provided).
3. Run the Streamlit app using the command:

   ```bash
   streamlit run app.py
   ```
4. Enter a movie title in the interface and receive a list of recommended movies based on content similarity.

## Technologies Used

* Python (NumPy, Pandas, Scikit-learn, Matplotlib, Seaborn)
* Streamlit for the web interface
* PyCharm IDE for development
