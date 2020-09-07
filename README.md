# ACM Research Coding Challenge (Fall 2020)

## No Collaboration Policy

**You may not collaborate with anyone on this challenge.** You _are_ allowed to use Internet documentation. If you _do_ use existing code (either from Github, Stack Overflow, or other sources), **please cite your sources in the README**.

## Submission Procedure

Please follow the below instructions on how to submit your answers.

1. Create a **public** fork of this repo and name it `ACM-Research-Coding-Challenge`. To fork this repo, click the button on the top right and click the "Fork" button.
2. Clone the fork of the repo to your computer using . `git clone [the URL of your clone]`. You may need to install Git for this (Google it).
3. Complete the Challenge based on the instructions below.
4. Email the link of your repo to research@acmutd.co with the same email you used to submit your application. Be sure to include your name in the email.

## Question One

![Image of Cluster Plot](ClusterPlot.png)
<br/>
Given the following dataset in `ClusterPlot.csv`, determine the number of clusters by using any clustering algorithm. **You're allowed to use any Python library you want to implement this**, just document which ones you used in this README file. Try to complete this as soon as possible.

Regardless if you can or cannot answer the question, provide a short explanation of how you got your solution or how you think it can be solved in your README.md file.

## RESPONSE

Python libraries installed: pandas, matplotlib, scikit-learn

Existing code taken from the following sources (with some modifications):

Ankit Prasad's K-Means Clustering Algorithm at https://medium.com/code-to-express/k-means-clustering-for-beginners-using-python-from-scratch-f20e79c8ad00

Vik Paruchuri's K-Means Clustering Algorithm at https://www.dataquest.io/blog/k-means-clustering-us-senators/

To solve this problem, I first did some research online on clustering algorithms, since I haven't had much experience with Python or machine learning.

Looking at the given cluster plot, my first thought was that it looked like 2 clusters of data points separated by a gap along the y-axis. The clearest solution for me was an algorithm that grouped clusters based on the proximity of data points to each other, with no need to consider outliers. In other words, if a lot of data points were close together, they would go in the same cluster. I ended up choosing a K-Means clustering algorithm, using means instead of medians due to the lack of outliers in the given data.

I eventually settled with a cluster (centroid) count of 3 instead of 2 due to the top cluster being less dense than the bottom one, which is why the top cluster was split apart and identified as 2 separate clusters by the K-Means algorithm. I then implemented it by importing the relevant Python libraries.