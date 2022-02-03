PROJECTS_DIR=~/Johnathan/Projects
MOODLE_DIR=${PROJECTS_DIR}/Moodle_Grade_Automation
DATA_DIR=${PROJECTS_DIR}/grade_data


.PHONY: download

download: ${DATA_DIR}/grade_data.csv 
	python3 ${MOODLE_DIR}/app.py

