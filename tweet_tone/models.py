from tweet_tone import db


class Tweet(db.Model):
    # db.Integer should be replaced with Twitter ID -- picked up from form?
    id = db.Column(db.Integer, primary_key=True)
    tweet_id = db.Column(db.Integer, nullable=False)
    tweet_url = db.Column(db.String(), nullable=False)
    # in order: name of mood (string), intensity (integer)
    dom_tone = db.Column(db.String(), nullable=False)
    dom_intensity = db.Column(db.Integer, nullable=False)
    children = db.relationship('Child', backref='parent')

    def __repr__(self):
        return f"Tweet('{self.tweet_id}', '{self.dom_tone}', '{self.children}')"


class Child(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tweet_id = db.Column(db.Integer, db.ForeignKey('tweet.id'), nullable=False)
    parent = db.relationship('Tweet', backref='child')

    def __repr__(self):
        return f"Tweet('{self.tweet_id}')"
