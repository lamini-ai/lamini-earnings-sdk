
import jsonlines
import gzip

def main():
    test_set_transcripts = load_test_set_transcripts()

    filtered_transcripts = filter_transcripts(test_set_transcripts)

    save_transcripts(filtered_transcripts)

def load_test_set_transcripts():
    path = "/app/lamini-earnings-sdk/data/golden_test_set.jsonl"

    with jsonlines.open(path) as reader:
        return list(reader)

def filter_transcripts(test_set_transcripts):
    path = "/app/lamini-earnings-sdk/data/earnings-transcripts.jsonl.gz"

    with gzip.open(path, "rt") as file:
        return list(filter_transcripts_by_ticker(file, test_set_transcripts))

def filter_transcripts_by_ticker(file, test_set_transcripts):

    ticker_set = set(transcript["ticker"] for transcript in test_set_transcripts)

    with jsonlines.Reader(file) as reader:
        for transcript in reader:
            if transcript["ticker"] in ticker_set:
                yield transcript

def save_transcripts(transcripts):
    path = "/app/lamini-earnings-sdk/data/test_set_transcripts.jsonl"

    with jsonlines.open(path, "w") as writer:
        writer.write_all(transcripts)

main()

