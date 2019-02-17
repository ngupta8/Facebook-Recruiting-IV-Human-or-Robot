from flask import Flask,render_template,url_for,request,Markup
from flask_material import Material

# EDA PKg
import pandas as pd 
import numpy as np 

# ML Pkg
from joblib import load


# Visualization
from bokeh.plotting import figure
from bokeh.embed import components

app = Flask(__name__)
Material(app)

# Load the features file
bids_df = pd.read_csv("data/feature_of_all_train_df_clean.csv")
feature_names = bids_df.columns[0:-1].values.tolist()


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/preview')
def preview():
    df = pd.read_csv("data/bids.csv")
    return render_template("preview.html", df_view=df)


@app.route('/', methods=["POST"])
def analyze():
    print(request.form)
    if request.method == 'POST':
        bid_count = request.form['bid_count']
        country_count = request.form['country_count']
        ip_count = request.form['ip_count']
        average_distinct_country_per_auction = request.form['average_distinct_country_per_auction']
        average_distinct_dev_per_auction = request.form['average_distinct_dev_per_auction']
        average_distinct_merc_per_auction = request.form['average_distinct_merc_per_auction']
        average_bids_per_auction = request.form['average_bids_per_auction']
        num_auction = request.form['num_auction']
        num_auction_won = request.form['num_auction_won']
        percentage_win = request.form['percentage_win']
        avg_bids_auction = request.form['avg_bids_auction']
        competitors = request.form['competitors']

        # Clean the data by convert from unicode to float 
        sample_data = [bid_count,country_count,
                       ip_count,average_distinct_country_per_auction,
                       average_distinct_dev_per_auction,
                       average_distinct_merc_per_auction,
                       average_bids_per_auction,num_auction,
                       num_auction_won,percentage_win,
                       avg_bids_auction,competitors]
        clean_data = [float(i) for i in sample_data]
        model_choice = 'KNN'
        # # Reshape the Data as a Sample not Individual Features
        ex1 = np.array(clean_data).reshape(1,-1)

        knn_model = load('data/knn.joblib')
        result_prediction = knn_model.predict(ex1)
        # # Reloading the Model
        # if model_choice == 'dtree':
        #     logit_model = load('data/dtree.joblib')
        #     result_prediction = logit_model.predict(ex1)
        # elif model_choice == 'knnmodel':
        #     knn_model = load('data/dtree.joblib')
        #     print(ex1)
        #     result_prediction = knn_model.predict(ex1)
        # elif model_choice == 'svmmodel':
        #     knn_model = load('data/dtree.joblib')
        #     result_prediction = knn_model.predict(ex1)

    return render_template('index.html',bid_count=bid_count,
                           country_count=country_count,
                           ip_count=ip_count,
                           average_distinct_country_per_auction=average_distinct_country_per_auction,
                           average_distinct_dev_per_auction=average_distinct_dev_per_auction,
                           average_distinct_merc_per_auction=average_distinct_merc_per_auction,
                           average_bids_per_auction=average_bids_per_auction,
                           num_auction=num_auction,
                           num_auction_won=num_auction_won,
                           percentage_win=percentage_win,
                           avg_bids_auction=avg_bids_auction,
                           competitors=competitors,
                           clean_data=clean_data,
                           result_prediction=int(result_prediction),
                           model_selected=model_choice)


@app.route('/eda')
def eda():
    current_feature_name = request.args.get("feature_name")
    if current_feature_name is None:
        current_feature_name = "bidder_id"

    # Create the plot
    plot = create_figure(current_feature_name, 10)

    # Embed plot into HTML via Flask Render
    script, div = components(plot)
    eda_feature_names = ['bid_counts', 'bid_counts_by_auction', 'merchandise_count_by_auction', 'ip_counts_by_auction']
    return render_template("eda.html", script=script, div=div,
                           feature_names=eda_feature_names, current_feature_name=current_feature_name)


# Create the main plot
def create_figure(current_feature_name, bins):
    p = figure(plot_height=600, plot_width=600,
               title='Histogram of Bids Count',
               x_axis_label=current_feature_name,
               y_axis_label='Bids Count')

    grouped_df = pd.DataFrame(bids_df.groupby(['bidder_id']).size().reset_index(name="bid_count")).dropna()
    grouped_df.drop(grouped_df['bid_count'].idxmax())

    feature_as_list = list(grouped_df.loc[1:, "bid_count"].astype('float'))
    arr_hist, edges = np.histogram(feature_as_list, bins=10, density=True)
    # Add a quad glyph
    p.quad(top=arr_hist, bottom=0, left=edges[:-1], right=edges[1:],
           fill_color="navy", line_color="red", alpha=0.5)

    return p


if __name__ == '__main__':
    app.run(debug=True)
