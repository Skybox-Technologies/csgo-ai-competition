# Submission instructions

This file documents how to submit your solution to the csgo.ai challenge.

An example submission that always guesses that CTs win is provided in the `test-submission` folder.

## Location and deadline

You can upload your submission here: https://ai.skybox.gg

The submission site will be open from now until August 21st.

Please read the submission structure before submitting!

## Submission structure

Your submission should be a zip file containing the following:

- Your code, structured any way you prefer
- Either `README.txt` or `README.md`, which should contain your team name, contact
  information and any notes/documentation about your submission that you would
  like to share
- `run.sh`, which is described below
- Optional: `requirements.txt`, which can contain a number of python packages that will be placed in a virtualenv before running the code

The script `pack_submission.sh` can be used to create the zip file.

### `run.sh`

This file should be a shellcript (or other executable file) that takes 2 arguments:

- `input_file`: path to a single JSON file in the same format as the datasets
- `output_file`: path to a location where you should output the target variable, again in the same format

The output should be loadable by `pd.from_json` in the column `round_winner`. The target variable should be either `0/1` or `"CT"/"Terrorist"`.

### `requirements.txt`

A file that locks in your (python) dependencies. You can generate the file
manually or by using `pip freeze`. Ideally you should pin your dependencies
to specific versions and not include any that can be omitted.

See https://pip.pypa.io/en/stable/user_guide/#requirements-files for more details.

## Non-python submissions

If you're using another programming language than python, you should try to
make your submission as self-contained as possible.
This can be done in the following ways:

- Include a Nix-file called `shell.nix` which sets up an environment in which `run.sh` can be successfully run.
- Write detailed instructions that can be followed from a modern Ubuntu/Debian setup, ideally with commands/scripts to set up a working environment.

If in doubt then please open a ticket. If I cannot get your submission to run
in a timely manner then it will not be accepted.
