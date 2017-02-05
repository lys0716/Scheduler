alias schedule="python ./schedule_persist.py"
pyTest test_schedule.py
#get the configuration
#remove the persist file according to file name
perisstFile=$(awk -F "=" '/persist_path/ {print $2}' $PROJECT_FOLDER/config/prd.cfg)
rm $PROJECT_FOLDER/$perisstFile