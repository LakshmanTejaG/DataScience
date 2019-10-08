# K-Means Clustering

#Importing the dataset
setwd("~/ML/Part 4 - Clustering/Section 24 - K-Means Clustering")
dataset <- read.csv('Mall_Customers.csv')
#View(dataset)
dataset <- dataset[4:5]
#View(X)

# Using elbow method to calculate optimal number for cluster
set.seed(6)
wcss <- vector()
for (i in 1:10) wcss[i] <- sum(kmeans(dataset, i)$withinss)
plot(1:10, 
     wcss, 
     type = 'b', 
     main = paste('Elbow'), 
     xlab = 'money spent',
     ylab = 'Earnings')

# Fitting K-Means to dataset
set.seed(39)
KMeans <- kmeans(dataset, centers = 5, iter.max = 300, nstart = 10)
KMeansClus <- KMeans$cluster

#Visualization of the clusers
library('cluster')
clusplot(dataset,
         KMeansClus,
         lines = 0,
         shade = TRUE,
         color = TRUE,
         labels = 2,
         plotchar = FALSE,
         span = TRUE,
         main = paste('K-Means Clustering'),
         xlab = 'Money spent',
         ylab = 'Money Earn')
