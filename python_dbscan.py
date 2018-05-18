import numpy as np
import random as rand
import matplotlib.pyplot as plt
from sklearn.datasets import make_moons, make_circles
from sklearn.datasets.samples_generator import make_blobs

# simulate data to be clustered
# for the actual functions scroll down further.

# moons example, works best with eps = 0.2, r = 5
X,y = make_moons(n_samples = 400, noise = 0.05, random_state = 5)

fig = plt.figure()

plot1 = fig.add_subplot(3,2,1)
plot1.scatter(X[:,0], X[:,1], marker = "o")
plot1.set_title("Original Data")

# main
results = my_dbscan(X, 0.2, 5)

#plot the data
plot2 = fig.add_subplot(3,2,2)
plot2.scatter(X[:,0], X[:,1], c = results, marker = "o")
plot2.set_title("Resulting Clusters")

# blobs example, works best with eps = 0.3, r = 10
centers = [[1,1],[-1,-1],[1,-1]]
X, labels_true = make_blobs(n_samples = 750, centers = centers, cluster_std = 0.4, random_state = 0)

plot3 = fig.add_subplot(3,2,3)

plot3.scatter(X[:,0], X[:,1], marker = "o")

# main
results = my_dbscan(X, 0.3, 10)

#plot the data
plot4 = fig.add_subplot(3,2,4)
plot4.scatter(X[:,0], X[:,1], c = results, marker = "o")

# enclosed circles example, works best with eps = 0.2, r = 5
X, y = make_circles(n_samples = 600, noise = 0.05, factor = 0.5)

plot5 = fig.add_subplot(3,2,5)

plot5.scatter(X[:,0], X[:,1], marker = "o")
plot5.set_xlabel("x coordinates")
plot5.set_ylabel("y coordinates")

# main
results = my_dbscan(X, 0.2, 5)

#plot the data
plot6 = fig.add_subplot(3,2,6)
plot6.scatter(X[:,0], X[:,1], c = results, marker = "o")
plot6.set_xlabel("x coordinates")
plot6.set_ylabel("y coordinates")

fig.show()


#
# Finds the point type for a specified point in our data
#
# param: point, a specified point from a data array
# param: data, a 2d numpy array
# param: eps, the radius of the circle surrounding point
# param: r, the minimum number of points needed within eps-ball to be core point
# param: neighbors, when true this returns a list of neighbors
#
# return: the point type (1,0) and, when requested, a list of neighbors
#
def point_type(point, data, eps, r, pointType = False, neighbors = False):
    
    n,m = np.shape(data)
    count = 0
    core = 0
    neigh_list = []
    
    for i in range(n):
        
        # check distance between point and all data
        dist = 
        
        # if this distance is less than a specified eps
        # increase count 
        # append data point index to a list of neighbors
        if dist < eps:
            
            
            
            
    # if your count is at least
    # the minimum number of points for a core point
    # mark point as a core
    if count >= r:
        
           
        
    # return both the point type and
    # the list of neighbors only if requested
    if neighbors == True and pointType == True:
        
        return core, neigh_list
    
    # return only the neighbors   
    elif neighbors == True and pointType == False:
        
        return neigh_list
        
    # return only the point type
    elif neighbors == False and pointType == True:
        
        return core
        
#
# a recursive function.  This function explores a core point's neighbors, and if any of those neighbors are core points, we explore those neighbors, etc.
#
# param: neigh, a list of neighbor's indices as they sit in Y
# param: Y, the data array containing data points, cluster assignments, visited status, etc. 
# param: eps, the radius of your circle region
# param: r, the minimum number of points required for a core point
# param: clstr, the current cluster number
#
# returns an updated Y array
#        
def analyzeNeighbors(neigh, Y, eps, r, clstr):
    
    n = len(neigh)
    
    # for each neighbor
    for j in range(n):
        
        point = Y[neigh[j], 0:2]
        
        # give it the current cluster value
        Y[neigh[j],4] = 
        
        # if the point has been unvisited
        # mark as visited so we don't come back afterward
        if Y[neigh[j],2] != 1:
            
            Y[neigh[j],2] = 
            
            # determine the point's type and its neighbors
            Y[neigh[j],3], nei = 
            
            # then this neighbor is a core point (i.e. other points are reachable from it including itself)
            if Y[neigh[j],3] == 1:
                
                # mark as reachable
                Y[j,5] = 
                # and update Y by analyzing its neighbors
                # i.e. recursion
                Y = analyzeNeighbors()
            
            # if not a core point, skip for now
            else:
                
                continue
        # if visited, skip        
        else: 
        
            continue
    
    return Y
    
#
# searches the neighbors of a point to determine whether they belong to a cluster
# if the neighbors belong to a cluster, the point is a border point and needs the same assignment
#
# param: neighbors, a list of indices
# param: Y, the data array containing data points, cluster assignments, visited status, etc.
#
# returns a single cluster assignment
#    
def neighborCluster(neighbors, Y):
    
    clu = -1
    
    # search all neighbors
    for i in neighbors:
        
        # if any of the points have a cluster assignment
        # we return that cluster assignment
        if Y[i,4] != -1:
            
            clu = 
            #break
            
    
    return clu

#
# uses a density-based method to find clusters
#
# param: data, the data array of points
# param: eps, the radius of your circle region
# param: r, the minimum number of points required for a core point
#
# returns the cluster assignment of each point
#
def my_dbscan(data, eps, r):
    
    n_smpls, n_ftrs = np.shape(data)
    clstr = 0
    
    # vstd is a vector such that 1 will indicate whether a point
    # has been visited
    vstd =  np.zeros([n_smpls,1])
    # tp is a vector such that 1 will indicate whether a point
    # is a core point, -1 will indicate whether a point is noise,
    # and 0 will indicate whether the point is a border point
    tp = np.ones([n_smpls,1]) * (-1)
    # assgnClstr is a vector of -1's but will change to a nonnegative number
    # for the individual cluster assignment
    assgnClstr = np.ones([n_smpls,1]) * (-1)
    # rchbl is a vector that will state whether a point is reachable from a
    # core point, this will help distinguish border points from noise points
    # since border points may not be core
    rchbl = np.zeros([n_smpls,1])
    
    # pre-processing data by adding 4 columns to the data array
    Y = np.hstack([data, vstd, tp, assgnClstr, rchbl])
    
    for i in range(n_smpls):
        
        point = Y[i,0:2]
        
        # if this point has been unvisited
        if Y[i,2] == 0:
            
            # mark as visited
            Y[i,2] = 
            
            # determine whether core or noise
            # find its epsilon neighbors
            Y[i,3], neigh = point_type(point, data, eps, r, pointType = True, neighbors = True)
        
            # if the current point is a core point
            # then mark it as reachable
            if Y[i,3] == 1:
            
                Y[i,5] = 1
                # assign a cluster to the core point
                Y[i,4] = 
                # determine the cluster type, point type of the reachable points
                Y = analyzeNeighbors( )
                # increase the number of clusters
                clstr += 1
            
            # if the point is not a core point, skip for now
            else:
            
                continue
                    
        # if the point was visited, skip for now        
        else:
            
            continue
            
    # check the points not marked reachable
    for i in range(n_smpls):
        
        point = Y[i,0:2]
        
        # if the non-core point is not marked reachable
        # i.e. it's a border point or noise poitn
        if Y[i,5] == 0:
            
            # find the neighbors
            neigh2 = point_type(point, data, eps, r, pointType = False, neighbors = True)
            # determine if neighbors have a cluster assignment
            c = neighborCluster( )
            
            # if the neighbors have a cluster assignment
            # then the current point is a border point
            # and should get the same assignment as its neighbors
            if c != -1:
                
                Y[i,4] = 
            
            # if the neighbors did not have a cluster assignment
            # then the current point is a noise point and gets
            # its own cluster assignment
            else:
                
                Y[i,4] = 
            
        else:
            
            continue
                
    return Y[:,4]