# R script for running constructed analog using ridge regression

# loading library
library(MASS)

###################################################################################################################
# PART A: CALIBRATION
###################################################################################################################
# reading the input text file for calibration
# as header=F, if there is any header it should be removed in the text file
# here each spatial image is read as a variable
calibration_data <- read.table("D:/data_research/ca_sst_forecast_R/sst_jan_f.txt", header=F)

# the variable names in text file are attached to the current workspace
attach(calibration_data)

# performing linear regression to determine the weights
regress <- lm.ridge(V25~V1+V2+V3+V4+V5+V6+V7+V8+V9+V10+V11+V12+V13+V14+V15+V16+V17+V18+V19+V20+V21+V22+V23+V24, data=calibration_data)

# storing the regression weights as a matrix
weights <- as.matrix(regress$coef)

# the variable names in text file are deattached from the current workspace
detach(calibration_data)

# writing the regression weights into a text file
write.table(weights, file="D:/data_research/ca_sst_forecast_R/weights.txt", row.names = T, col.names = F)
##################################################################################################################


##################################################################################################################
# PART B: PREDICTION
##################################################################################################################
# reading the input text file for prediction
# as header=F, if there is any header it should be removed in the text file
# here each spatial image is read as a variable
# note that the prediction text file should have one less image variable than the calibration text file
prediction_data <- read.table("D:/data_research/ca_sst_forecast_R/sst_feb.txt", header=F)

# storing the dimensions (rows and columns) of the prediction data into a matrix
dimension <- as.matrix(dim(prediction_data))

# storing the number of observations (ie. no of rows or no of pixels)
no_of_obs <- dimension[1,1]

# converting to a matrix
X <- as.matrix(prediction_data)

# prediction variable is determined by multiplying the image variables by the weights determined in calibration step 
# (i.e. finding Xb in regression where X is a matrix and b is a column vector)
prediction <- X %*% weights

# writing the prediction variable/image into a text file
write.table(prediction, file="D:/data_research/ca_sst_forecast_R/pred_2006_feb.txt", row.names = F, col.names = T)
##################################################################################################################
