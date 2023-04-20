import os 
import h5py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Extract sensor data
def extract_sensor_into_frame(sensor, label, types, axes):

    # Extract data from each sensor and store column-wise
    frame_columns = []
    frame_column_names = []
    for data_type in types:
        for axis in axes:
            sensor_data = f['Sensors'][sensor][data_type]
            axis_number = axes.index(axis)
            sensor_data_axis = pd.DataFrame(sensor_data[:,axis_number])
            column_name = "%s/%s/%s" % (label, data_type, axis)
            frame_columns.append(sensor_data_axis)
            frame_column_names.append(column_name)

    # Concatenate sensor data into a dataframe and store metadata as column names
    sensor_frame = pd.concat(frame_columns, axis=1)
    sensor_frame.columns = frame_column_names
    return sensor_frame

# We're going to go through the HDF5 file, extract relevant data, plot it
if __name__ == "__main__":
    
    data_file = "data/28_oct.h5"

    print("Processing file %s" % (os.path.basename(data_file)))

    # Open h5 file for reading
    with h5py.File(data_file, 'r') as f:

        # Get all sensors in the dataset
        sensor_list = f['Sensors']
        
        # Go through each sensor and swap
        for sensor in sensor_list:

            # Placement is found in label 1
            label = f['Sensors'][sensor]['Configuration'].attrs['Label 1'].decode('ascii')

            # Extract the following data and axes from sensor
            types = ["Accelerometer", "Gyroscope", "Magnetometer"]
            axes = ["x", "y", "z"]
            sensor_frame = extract_sensor_into_frame(sensor, label, types, axes)

            # Plot acc data
            plot_data = True
            if plot_data:
                acc_data = sensor_frame.iloc[:,0:3].to_numpy()
                print(acc_data.shape)
                xaxis = np.arange(0,acc_data.shape[0])
                plt.plot(xaxis, acc_data[:,0])
                plt.plot(xaxis, acc_data[:,1])
                plt.plot(xaxis, acc_data[:,2])
                plt.title(label)
                plt.show()  


    print("All done")
