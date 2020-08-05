import sys
import pandas as pd

input_file, output_file = sys.argv[1], sys.argv[2]
df = pd.read_json(input_file)

# Always guess ct
targets = pd.DataFrame(
    {"round_winner": [0 for _ in range(df.shape[0])]})

# Write guesses to output
targets.to_json(output_file, orient="records")
