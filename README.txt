		Finale build 
# For run this build need:
  - run Docker Toolbox
  - run oracle Default VM
  - From docker toolbox cd ../../
  - cd users/administrator/finale/
  - From docker toolbox run Docker-compse up 

Final_test
		Source Code Management

Git
https://github.com/romant010/Finale.git
Default
(Auto)
		Build Triggers

Poll SCM
Schedule  */30 * * * * (Each 30 min)

		Build Environment
Use secret text(s) or file(s)

		Build

Command: docker-compose up -d
	 python 1step.py

