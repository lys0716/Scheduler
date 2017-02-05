# Scheduler Notebook

This scheduler can add/delete any event through schedule command. All the events will be persisted.

## Before you run
* Make sure you pass the unit tests with following steps
* First, please cd into schedule folder.
* Second, export enviroment variable: ```export PROJECT_FOLDER=```
* Third, run```sh pip install -r requirements.txt``` and ```sh bash ./setUpTest.sh``` to make sure everything works well.
* Fourth, set alias alias ```sh schedule="python ./schedule_persist.py"```

## Usage
* ```sh schedule add [name] [description] [priority] [due hour]```
* ```sh schedule get [name] ```
* ```sh schedule delete [name] ```
* ```sh schedule diplay [name] ```
