import spacy
import joblib
from scipy.sparse import hstack
from memory_profiler import profile
nlp = spacy.load("en_core_web_sm")


def apply_pos(text):
    """ Returns List of PoS Tags as Strings"""
    doc = nlp(text)
    return [str(token.pos) for token in doc]


@profile
def process_output(text):
    """ Function that performs NLP prediction  """


    # Load the entire pipeline
    pipeline = joblib.load("ML_Models/svm_pipeline.pkl")

    # Convert data to String
    data = str(text)

    # Call POS Function
    pos_tags = apply_pos(data)

    # Combine body and POS tags
    features = data + ' ' + ' '.join(pos_tags)

    # Predictions
    prediction = pipeline.predict([features])
    print(prediction)

    return str(prediction[0])



