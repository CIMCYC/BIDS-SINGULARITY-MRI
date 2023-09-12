CONVERT MRI (FMRI, DWI...) DATA TO BIDS FORMAT
 
Steps to use this repository: 
1. Download the Docker container: https://www. docker. com. 
Docker is an open source platform that allows us to create, deploy, and run applications in containers. A container is a lightweight, stand-alone software unit that contains everything needed to run an application, including codes, libraries, dependencies, and system configurations. 

2. Download the heudiconv  image https://heudiconv.readthedocs.io/en/latest/installation.html. 
A Docker image is a package or template that contains everything you need to run an application in an isolated and reproducible in a Docker environment. In our case, the heudiconv image contains everything you need to convert the DICOMS to NIfTI format (BIDS compatible) and then create the structure corresponding to the BIDS format. 

3. Modify the HEURISTIC_FILE. py. 
The file you can find in this repository is the configuration file needed to convert to BIDS format. Here, you would have to enter the names of the folders and files corresponding to the BIDS format structure according to the characteristics of your experiment. In addition, it is necessary to enter the protocol name of the different images obtained with the scanner, and link them with variables. 
 
4. Modify what appears in quotation marks in the following code according to your data to run it on the terminal: 
docker run --rm -it \ 
-v 'C:\Users\User\Documents\MRI\dicoms\01\ses-01:/dicoms' \ #write the path where you  have your dicoms on your computer followed by ‘:/' and the name that you want to assign it to the folder where you will work inside docker, any one. 
-v 'C:\Users\Usuario\Documents\MRI/:/dataheu' \ #write the path where you have your configuration file on your computer followed by ‘:/' and the name that you want to assign it to the folder where you will put it inside docker, any one. 
-v 'C:\Users\User\Documents\MRI\BIDS/:/output' \ #write the path where you want to export your BIDS on your computer followed by ‘:/' and the name that you want to assign it to the folder where you are going to do it inside docker, any one. 
nipy/heudiconv:latest \ #call the docker image used as code to go to BIDS format. 
-s '01' \ #participant number (not letters). 
-d dicoms/{subject} \  
--ses '01' \ #session number 
-f dataheu/HEURISTIC_ARCHIVE. py \ #path of the configuration file on our computer. 
-c dcm2niix -b \ #NIfTI converter. 
-o /output --minmeta 
 
All the images of the same participant must be together, they cannot be classified in folders according to each type of protocol.
It is advisable to name the participant folder as 001, 002..., because it is easier for the code to rename the subject folders if they are only numerical values. The heuristic file already does the renaming according to the BIDS structure. 
If you work on Windows, almost certainly, you will have to write everything on one line by removing the '\' slashes for it to run. 