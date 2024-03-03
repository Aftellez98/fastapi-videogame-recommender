from fastapi import FastAPI
import pandas as pd
import pickle
import uvicorn
from mangum import Mangum

app = FastAPI()
handler = Mangum(app)

@app.get("/predictvideogames")
def recommend_games(user_id: int, n_recommendations: int = 5, percentiles:bool = False):

    if percentiles==True:
        # Load the model
        with open('models/my_model_user_percentile.pkl', 'rb') as file:
            loaded_model = pickle.load(file)
    else:
        # Load the model
        with open('models/my_model_proportion.pkl', 'rb') as file:
            loaded_model = pickle.load(file)

    # Load the game data
    df = pd.read_csv('src/context/videogames.csv', sep=';', names=['UserId', 'VideoGame', 'Purchase', 'HoursPlayed'], index_col=False)

    # Find the games the user has not played yet
    not_played = df.loc[~df['VideoGame'].isin(df.loc[df['UserId'] == user_id, 'VideoGame'])]['VideoGame'].unique()

    # Predict ratings for all those games
    predictions = [loaded_model.predict(user_id, game) for game in not_played]

    # Sort the predictions by estimate in descending order and get the top n_recommendations
    ranked_games = sorted(predictions, key=lambda x: x.est, reverse=True)[:n_recommendations]

    # Returns the names (ids) of the top n_recommendations games
    return [pred.iid for pred in ranked_games]

@app.get("/users")
def get_user_ids():
   
    df = pd.read_csv('src/context/videogames.csv', sep=';', names=['UserId', 'VideoGame', 'Purchase', 'HoursPlayed'], index_col=False)
    users = df['UserId'].unique().tolist()

    return users

if __name__ == "__main__":
   uvicorn.run(app, host="0.0.0.0", port=8080)
