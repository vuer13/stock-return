import spacy

nlp = spacy.load("en_core_web_sm")

def process_row(row):
    text = row["transcript"]
    date = str(row["date"])
    ticker = row["ticker"]

    doc = nlp(text)
    results = []

    for sent in doc.sents:
        s = sent.text.strip()
        if len(s.split()) >= 5 and not s.lower().startswith((
            "operator", "prepared remarks", "thank you", "your line is open"
        )):
            results.append({
                "text": s,
                "date": date,
                "ticker": ticker
            })

    return results