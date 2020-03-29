from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class TwitterLinkForm(FlaskForm):
    twitter_link = StringField('twitter_link', validators=[DataRequired()],
                               render_kw={"placeholder":
                                          "https://twitter.com/pkdie0/status/"
                                          + "1241592065600995334"})
    SubmitField = SubmitField('Analyze mood')
