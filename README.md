# Scheduler Notebook

This scheduler can add/delete any event through schedule command. All the events will be persisted.

## Before you run
####First, please cd into schedule folder.
####Second, export enviroment variable: ```export PROJECT_FOLDER=```
####Third, run```sh pip install -r requirements.txt``` and ```sh bash ./setUpTest.sh``` to make sure everything works well.
####Fourth, set alias alias ```sh schedule="python ./schedule_persist.py"```

## Usage
schedule add [name] [description] [priority] [due hour]
schedule get [name]
schedule delete [name]
schedule diplay [name]