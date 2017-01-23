# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 00:26:10 2016

@author: ajaver
"""
import os

from MWTracker.helper.tracker_param import tracker_param
from MWTracker.helper.runMultiCMD import runMultiCMD, print_cmd_list

from MWTracker.processing.ProcessWormsLocal import ProcessWormsLocalParser
from MWTracker.processing.batchProcHelperFunc import getDefaultSequence, walkAndFindValidFiles
from MWTracker.processing.CheckFilesForProcessing import CheckFilesForProcessing

def processMultipleFiles(walk_args, check_args,
                         videos_list, only_summary, max_num_process, refresh_time):
    #get the list of valid videos
    if not videos_list:
        valid_files = walkAndFindValidFiles(**walk_args)
    else:
        with open(videos_list, 'r') as fid:
            valid_files = fid.read().split('\n')
            valid_files = [os.path.realpath(x) for x in valid_files]
    
    files_checker = CheckFilesForProcessing(**check_args)

    cmd_list = files_checker.filterFiles(valid_files)
    
    if not only_summary:
        # run all the commands
        print_cmd_list(cmd_list)

        runMultiCMD(
            cmd_list,
            local_obj = ProcessWormsLocalParser,
            max_num_process = max_num_process,
            refresh_time = refresh_time)

def compressMultipleFilesFun(
        video_dir_root,
        mask_dir_root,
        tmp_dir_root,
        json_file,
        pattern_include,
        pattern_exclude,
        max_num_process,
        refresh_time,
        only_summary,
        is_copy_video,
        videos_list):

    param = tracker_param(json_file)
    analysis_checkpoints = getDefaultSequence('Compress',
                                             is_single_worm=param.is_single_worm)
    
    walk_args = {'root_dir':video_dir_root, 
                 'pattern_include' : pattern_include,
                  'pattern_exclude' : pattern_exclude}
    
    check_args = {'video_dir_root': video_dir_root,
                  'mask_dir_root': mask_dir_root,
                  'results_dir_root' : mask_dir_root,
                  'tmp_dir_root' : tmp_dir_root,
                  'json_file' : json_file,
                  'analysis_checkpoints': analysis_checkpoints,
                  'is_copy_video': is_copy_video}

    processMultipleFiles(walk_args, check_args,
                         videos_list, only_summary, max_num_process, refresh_time)

def trackMultipleFilesFun(
        mask_dir_root,
        results_dir_root,
        tmp_dir_root,
        json_file,
        pattern_include,
        pattern_exclude,
        max_num_process,
        refresh_time,
        force_start_point,
        end_point,
        only_summary,
        use_manual_join,
        videos_list):
        
    # calculate the results_dir_root from the mask_dir_root if it was not given
    if not results_dir_root:
        results_dir_root = getResultsDir(mask_dir_root)

    param = tracker_param(json_file)
    analysis_checkpoints = getDefaultSequence('Track', 
                                             is_single_worm=param.is_single_worm)
    if use_manual_join:
          #only execute the calculation of the manual features
          analysis_checkpoints = analysis_checkpoints + ['FEAT_MANUAL_CREATE']
          
    _removePointFromSide(analysis_checkpoints, force_start_point, 0)
    _removePointFromSide(analysis_checkpoints, end_point, -1)
    
    
    
    walk_args = {'root_dir':mask_dir_root, 
                 'pattern_include' : pattern_include,
                  'pattern_exclude' : pattern_exclude}
    
    check_args = {'video_dir_root': mask_dir_root,
                  'mask_dir_root': mask_dir_root,
                  'results_dir_root' : results_dir_root,
                  'tmp_dir_root' : tmp_dir_root,
                  'json_file' : json_file,
                  'analysis_checkpoints': analysis_checkpoints,
                  'is_copy_video': True}

    processMultipleFiles(walk_args, check_args,
                         videos_list, only_summary, max_num_process, refresh_time)




def getResultsDir(mask_dir_root):
    # construct the results dir on base of the mask_dir_root
    subdir_list = mask_dir_root.split(os.sep)

    for ii in range(len(subdir_list))[::-1]:
        if subdir_list[ii] == 'MaskedVideos':
            subdir_list[ii] = 'Results'
            break
    # the counter arrived to zero, add Results at the end of the directory
    if ii == 0:
        subdir_list.append('Results')

    return (os.sep).join(subdir_list)

def _removePointFromSide(list_of_points, point, index):
    assert (index == 0) or (index == -1)
    if point:
        #move points until 
        while list_of_points and \
        list_of_points[index] != point:
            list_of_points.pop(index)
    if not list_of_points:
        raise ValueError("Point {} is not valid.".format(point))

def test_compressMultipleFilesFun():
    from ProcessMultipleFilesParser import CompressMultipleFilesParser
    
    cmp_dflt = CompressMultipleFilesParser.dflt_vals
    cmp_dflt['pattern_include'] = '*.avi'
    cmp_dflt['json_file'] = '/Users/ajaver/Documents/GitHub/Multiworm_Tracking/Tests/Data/test_2/test2.json'
    
    video_dir_root = '/Users/ajaver/Documents/GitHub/Multiworm_Tracking/Tests/Data/test_2/RawVideos/'
    mask_dir_root = '/Users/ajaver/Documents/GitHub/Multiworm_Tracking/Tests/Data/test_2/RawVideos/Masks/'
    
    compressMultipleFilesFun(video_dir_root, mask_dir_root, **cmp_dflt)

def test_trackMultipleFilesFun():
    from ProcessMultipleFilesParser import TrackMultipleFilesParser
    
    track_dflt = TrackMultipleFilesParser.dflt_vals
    track_dflt['pattern_include'] = '*.hdf5'
    track_dflt['json_file'] = '/Users/ajaver/Documents/GitHub/Multiworm_Tracking/Tests/Data/test_2/test2.json'
    
    #video_dir_root = '/Users/ajaver/Documents/GitHub/Multiworm_Tracking/Tests/Data/test_2/RawVideos/'
    mask_dir_root = '/Users/ajaver/Documents/GitHub/Multiworm_Tracking/Tests/Data/test_2/RawVideos/Masks/'
        
    trackMultipleFilesFun(mask_dir_root, **track_dflt)

if __name__ == '__main__':
    test_trackMultipleFilesFun()
