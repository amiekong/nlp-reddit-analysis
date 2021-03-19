from flask import Blueprint, Flask, g, jsonify, render_template, request, Response, redirect, url_for, send_from_directory
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
import os
import datetime
import webbrowser

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        subreddit = request.form.get("subreddit")
        if subreddit == "abuse_pre":
            return render_template('ldavis_prepared_pre_abuse.html')
            #return webbrowser.open("saved_topic_models/ldavis_prepared_pre_abuse.html", new=2)
        if subreddit == "abuse_mid":
            return render_template('ldavis_prepared_mid_abuse.html')
        if subreddit == "viol_pre":
            return render_template('ldavis_prepared_pre_violence.html')
        if subreddit == "viol_mid":
            return render_template('ldavis_prepared_mid_violence.html')
        if subreddit == "ptsd_pre":
            return render_template('ldavis_prepared_pre_ptsd.html')
        if subreddit == "ptsd_mid":
            return render_template('ldavis_prepared_mid_ptsd.html')
        if subreddit == "default":
            render_template('index.html')

    return render_template('index.html')


if __name__=='__main__':
    app.run(debug=True)
