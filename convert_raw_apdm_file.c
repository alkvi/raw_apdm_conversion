#include "apdm.h"
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[])
{
    printf("This program will process raw APDM files into HDF5 files.\n");

    if (argc < 3) {
        printf("Usage: %s <output_file> <input_file1> <input_file2> ...\n", argv[0]);
        return 1;
    }

    apdm_recording_info_t recording_info;
    const char delimiter[] = ",";
    apdm_progress_t current_progress;

    // Set the output file path
    const char *file_out = argv[1];

    // Prepare arrays to go into the processing function
    char **all_files = &argv[2];
    int num_files = argc - 2;

    // Set log level to INFO
    int r = apdm_set_log_level(2);
    printf("Set log level, status %d, '%s'\r\n", r, apdm_strerror(r));

    // Get file signature
    // APDM_EXPORT int apdm_process_raw(char **file_in, char **calibration_file, int nFiles, const char *file_out,  
    // const bool store_raw, const bool store_si, const bool format_hdf, const bool compress, char csv_delimiter, apdm_progress_t *progress);

    // Example for one file
    //char *raw_file_path = "../data/apdm_raw_01_nov/XI-001974-0432_2022.11.01-10.16.26.apdm";
    //int r = apdm_read_raw_file_info(raw_file_path, &recording_info);
    //printf("Opened raw file, status %d, '%s'\r\n", r, apdm_strerror(r));
    //r = apdm_process_raw(&raw_file_path, NULL, 1, file_out, false, true, true, false, *delimiter, &current_progress);

    // For a list of files
    r = apdm_process_raw(all_files, NULL, 3, file_out, false, true, true, false, *delimiter, &current_progress);
    printf("Processed raw file, status %d, '%s'\r\n", r, apdm_strerror(r));

    return 0;
}