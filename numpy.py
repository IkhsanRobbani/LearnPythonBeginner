#gunanya ketika punya list/array berat dan tinggi badan dan kita nentuin bmi
#bmi = berat / tinggi ** 2, utk ngitung biasa gk bisa langsung semua perlu elemen satu satu.
# Create list baseball
baseball = [180, 215, 210, 210, 188, 176, 209, 200]

# Import the numpy package as np
import beginner.numpy as np

# Create a numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out type of np_baseball
print(type(np_baseball))


#namun pengoperasian dg numpy atau konvensional beda, cthnya penjumlahan list
tinggi = [1,2,3,4,5]
berat = [20,30,40,50,60]
print(tinggi+berat)         #hasilnya 1,2,3,4,......,50,60
np_tinggi=np.array(tinggi)
np_berat=np.array(berat)
print(np_berat+np_tinggi)   #hasilnya 21,32,43,54,65

#latihan
# height_in and weight_lb are available as regular lists

# Import numpy
import beginner.numpy as np
height_in=[2.7,3.0,2.8,2.9]
weight_lb=[50,51,53,52,55,54]
# Create array from height_in with metric units: np_height_m
np_height_m = np.array(height_in) * 0.0254

# Create array from weight_lb with metric units: np_weight_kg
np_weight_kg = np.array(weight_lb)*0.453592

# Calculate the BMI: bmi
bmi= np_weight_kg/np_height_m**2

# Print out bmi
print(bmi)
#---------------------------------------------------------------
# height_in and weight_lb are available as a regular lists

# Import numpy
import beginner.numpy as np

# Calculate the BMI: bmi
np_height_m = np.array(height_in) * 0.0254
np_weight_kg = np.array(weight_lb) * 0.453592
bmi = np_weight_kg / np_height_m ** 2

# Create the light array, mencari orang dengan bmi dibawah 21
light=bmi<21
bmi[light]

print(bmi[light])

#np_baseball.shape/ method shape berguna utk mengetahui ukuran matriks dr array
#melakukan operasi array
import beginner.numpy as np
np_mat = np.array([[1, 2],
                   [3, 4],
                   [5, 6]])
np_mat * 2
np_mat + np.array([10, 10])
np_mat + np_mat
print(np_mat)

#STATISTIKA DG NUMPY
y=[1,2,3,4,5]
mean=np.mean(y)
median=np.median(y)