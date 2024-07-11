CONVERT MRI (FMRI, DWI...) DATA TO BIDS FORMAT
 
Steps to use this repository: 
1. Download the Docker container: https://www. docker. com. 
Docker is an open source platform that allows us to create, deploy, and run applications in containers. A container is a lightweight, stand-alone software unit that contains everything needed to run an application, including codes, libraries, dependencies, and system configurations. 

2. Download Singularity: https://www.nipreps.org/apps/singularity/

3. Download the heudiconv image: https://heudiconv.readthedocs.io/en/latest/installation.html. 
A Docker image is a package or template that contains everything you need to run an application in an isolated and reproducible in a Docker environment, via Singularity (it is needed). In our case, the heudiconv image contains everything you need to convert the DICOMS to NIfTI format (BIDS compatible) and then create the structure corresponding to the BIDS format. 
Run this line in Terminal: singularity pull docker://nipy/heudiconv:latest.

3. Modify the HEURISTIC_FILE.py. 
The file you can find in this repository is the configuration file needed to convert to BIDS format. Here, you would have to enter the names of the folders and files corresponding to the BIDS format structure according to the characteristics of your experiment. In addition, it is necessary to enter the protocol name of the different images obtained with the scanner, and link them with variables. 
 
4. Modify what appears in quotation marks in the following code according to your data to run it on the terminal: 
singularity run --cleanenv 
-B /home/user/Documents/study/:/base  # write the path where you have your configuration file on your computer 
-e /home/user/heudiconv_latest.sif # write the path where is heudiconv image
-d /home/user/Documents/study/dicoms/{subject}/ses-{session}/*.dcm  # write the path where you  have your dicoms on your computer
-o /home/user/Documents/study/BIDS/  # write the path where you want to export your BIDS on your computer
-f /home/user/Documents/study/heuristic_file.py  # python script or built-in heuristic
-c dcm2niix # conversion program
-s 01 # subject ID
-ss 01 # session number
-b %  output in BIDS format
--minmeta # includes only required
metadata in the JSON file
--overwrite # overwrites old results

 
All the images of the same participant must be together, they cannot be classified in folders according to each type of protocol.
It is advisable to name the participant folder as 001, 002..., because it is easier for the code to rename the subject folders if they are only numerical values. The heuristic file already does the renaming according to the BIDS structure. 
If you work on Windows, almost certainly, you will have to write everything on one line to run. If you use Linux, you have to write everything in a row on the same line and separated by only one space (It is writing in different lines to explain it better).

For any questions you can write to pilarsanpe@ugr.es or mariaruizromero@ugr.es