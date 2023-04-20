This program converts raw data found on APDMs Opal sensors (.apdm format) into HDF5 files that can be imported into Mobility Lab, or processed otherwise.

To obtain the latest version of the SDK, download the following archive:
http://share.apdm.com/libraries/release/apdm_sdk.zip

Also see for information:
https://support.apdm.com/hc/en-us/articles/360000817606-Does-APDM-provide-an-SDK-

On a Windows 10 machine I had issues with the native MSVC C compiler (it's not C99-compliant).
Instead, use another OS, or for Windows compiling, use Cygwin and GCC.

To install:
https://cygwin.readthedocs.io/en/latest/install/
setup-x86_64.exe --no-admin

Then to compile (with link against APDM SDK dll folder placed on C:/apdm_sdk):
cd C:\cygwin64\bin
gcc.exe -IC:/apdm_sdk/include -IC:/apdm_sdk/include/HDF -o <folder path>/convert_raw_apdm_file.exe <folder path>/convert_raw_apdm_file.c C:/apdm_sdk/libs/Windows/x64/apdm.dll

copy apdm.dll and cygwin1.dll to output folder.

To run:
./convert_raw_apdm_file.exe

To process different files, just point to different raw files in convert_raw_apdm_file.c and re-compile.