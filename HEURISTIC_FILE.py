import os


def create_key(template, outtype=('nii.gz',), annotation_classes=None):
    if template is None or not template:
        raise ValueError('Template must be a valid format string')
    return template, outtype, annotation_classes


def infotodict(seqinfo):
    """Heuristic evaluator for determining which runs belong where

    allowed template 
s - follow python string module:

    item: index within category
    subject: participant id
    seqitem: run number during scanning
    subindex: sub index within group
    """

    # Modify this bit to include all the scans that you want to convert into BIDS.
    # This should be the format: VARIABLE_NAME = create_key('PATH/filename')
    variable_name = create_key('sub-{subject}/{session}/{datatype}/sub-{subject}_{session}_{filename}}') #change variable_name to the name according to the type of image. Filename would be the name following the BIDS structure according to the type of image.
    #examples:
    #t1w = create_key('sub-{subject}/{session}/anat/sub-{subject}_{session}_T1w')
    #run1 = create_key('sub-{subject}/{session}/func/sub-{subject}_{session}_task_run-1_bold')
    #distPA = create_key('sub-{subject}/{session}/fmap/sub-{subject}_{session}_dir-PA_epi')
    #distAP = create_key('sub-{subject}/{session}/fmap/sub-{subject}_{session}_dir-AP_epi')
    #B1k = create_key('sub-{subject}/dwi/sub-{subject}_{session}_B1k')
    ...
    
    # Now also add the new keys also here
    info = {variable_name: [],
            #examples:
            #t1w: [],
            #run1: [],
            #distPA: [],
            #distAP: [],
            #B1k: [],
            ...
           }

    for idx, s in enumerate(seqinfo):
	# Now add here a new "if" statement for the keys that were created above.
        if s.protocol_name == 'name': #enter the name of the assigned scanner image for each particular variable_name.
            info[variable_name] = [s.series_id]
        #examples:
        #if s.protocol_name == 'MPRAGE_1mm_new':
            #info[t1w] = [s.series_id]
        #if s.protocol_name == 'FeedBES_2mm_run1':
            #info[run1] = [s.series_id]
        #if s.protocol_name == 'FeedBES_correction_posBlip':
            #info[distAP] = [s.series_id]
        #if s.protocol_name == 'FeedBES_correction_negBlip':
            #info[distPA] = [s.series_id]
        #if s.protocol_name == 'MBep2d_diff_175iso_B1k_d32_blip':
            #info[B1k] = [s.series_id]
        ...       

    return info
