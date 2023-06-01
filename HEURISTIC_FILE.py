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
    ...

    
    # Now also add the new keys also here
    info = {variable_name: [],
            ...
           }

    for idx, s in enumerate(seqinfo):
	# Now add here a new "if" statement for the keys that were created above.
        if s.protocol_name == 'name': #enter the name of the assigned scanner image for each particular variable_name.
            info[variable_name] = [s.series_id]
        ...       

    return info
