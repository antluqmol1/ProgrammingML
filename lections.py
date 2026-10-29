import math
import numpy as np
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

# ~~~~~~~~~~ LECTION 1 ~~~~~~~~~~~

def mean(values):
    total = 0
    for v in values:
        total += v
    return total / len(values)

def variance(values):
    m = mean(values)
    squared_diff_sum = 0

    for v in values:
        diff = v - m
        squared_diff_sum += math.pow(diff, 2)
    # Sample variance: divide by n - 1
    return squared_diff_sum / len(list)-1

def std_dev(values):
    return math.sqrt(variance(values))

def median(values):
    # Median requires the data to be ordered
    values = sorted(values)
    n = len(values)
    middle = n // 2

    if n%2 == 1:
        # Odd number of values -> middle value
        return values[middle]
    else:
        # Even number of values -> average of two middle values
        return (values[middle - 1] + values[middle]) / 2

l = [15, 15, 15, 15, 15, 15, 25, 50, 100]

print("Mean:", mean(l))
print("Variance:", variance(l))
print("Standard deviation:", std_dev(l))
print("Median:", median(l))


# ~~~~~~~~~~ LECTION 2 ~~~~~~~~~~~

def ssort(values):
    # Selection sort
    n=len(values)
    for i in range(n-1):
        min_index = i

        #Find the smallest value in the unsorted part
        for j in range(i, n):
            if values[j] <= values[i]:
                values[i], values[j] = values[j], values[i]
    return values

# l1 = [6,1,5,2,3,4]

# 1, 6, 5, 2, 3, 5, 4
# 1, 2, 5, 6, 3, 5, 4
# 1, 2, 3, 6, 5, 5, 4
# 1, 2, 3, 4, 5, 5, 6

def isort(values):
    # Insertion sort
    n=len(values)

    for i in range(1, n):
        #Compare the current value with previous values
        for j in range(i, 0, -1):
            if values[j] < values[j-1]:
                values[j], values[j-1] = values[j-1], values[j]
            else:
                #Previous values are already sorted
                break
    return values

def partitioning(values, beginning, ending):
    # Use the last element as the pivot
    pivot = values[beginning]

    # Index of the last value smaller than the pivot
    i = beginning - 1

    for j in range(beginning, ending):
        # Move values smaller than or equal to pivot to the left
        if values[j] < pivot:
            i += 1

            # Swap values
            values[i], values[j] = values[j], values[i]

    # Put pivot between the 2 partitions
    values[i + 1], values[ending] = values[ending], values[i + 1]

    # Return the final position of the pivot
    return i + 1


def qsort(values, beginning=0, ending=None):
    # First call: sort the whole list
    if ending is None:
        ending = len(values)-1

    # Base case: one or zero elements are already sorted
    if beginning < ending:
        # Partition the list around the pivot
        pivot_index = partitioning(values, beginning, ending)

        # Sort the left partition
        qsort(values, beginning, pivot_index - 1)

        # Sort the right partition
        qsort(values, pivot_index + 1, ending)

    return values

# Test sorting algorithms

l1 = [6, 1, 5, 2, 3, 4]

print("Selection sort:", ssort(l1.copy()))

l1 = [6, 1, 5, 2, 3, 4]
print("Insertion sort:", isort(l1.copy()))

l1 = [6, 1, 5, 2, 3, 4]
print("Quick sort:", qsort(l1.copy()))



# ~~~~~~~~~~~ REGRESSION ~~~~~~~~~~~

X = 2 * np.random.rand(100, 1)

# Linear relationship + Gaussian noise
y = 4 + 3 * X + np.random.randn(100, 1)


# ~~~~~~~~~~~ OOPD ~~~~~~~~~~~

class Cube:
    # Class attributes: shared by ALL cubes (double underscore = "private")
    __sides = 6
    __edges = 12

    def __init__(self, l):
        # Constructor: runs when creating a Cube. Invalid length -> default 1
        if l < 0:
            l = 1
        self.__length = l # Instance attribute: each cube has its own

    # Getter: read access to a private attribute (encapsulation)
    def getLength(self):
        return self.__length

    # Setter: same validation as the constructor
    def setLength(self, l):
        if l < 0:
            l = 1
        self.__length = l

    @classmethod
    def getSides(cls):      # Receives the class, not an instance
        return cls.__sides

    @staticmethod
    def isValid(length): #Needs neither self nor cls
        if length > 0:
            print("Valid edge length")
        else:
            print("Invalid value")

c = Cube(4)
print(Cube.getSides())  # 6 -> no need to pass Cube anymore
Cube.isValid(-1)        # Invalid value
c.isValid(4)            # Also works from an instance


class Hypercube:

    def __init__(self, n, l):
        self._dimension = n     # Single underscore = "protected" (convention)
        self._length = l

    def getDimension(self):
        return self._dimension

    def getLength(self):
        return self._length

    def setLength(self, l):
        self._length = l

    def whatAmI(self):
        print("I am a", self._dimension, "dimensional hypercube")

# Inheritance:

class Square(Hypercube):

    def __init__(self, l):
        super().__init__(2, l)        # Reuse the parent constructor
        # Hypercube.__init__(self, 2, l) # (Other option than super)
        self._edges = 4

    def getEdges(self):
        return self._edges

    def area(self):
        return self._length * self._length

    # Overriding: replaces the parent's method (polymorphism)
    def whatAmI(self):
        print("I am a square")

hc1 = Hypercube(5, 2)
hc1.whatAmI()                   # I am a 5 dimensional hypercube
print(hc1.getLength())          # 2

sq1 = Square(3)
sq1.whatAmI()                   # I am a square (overriden version)
print(sq1.getLength())          # 3 (inherited method)
print(sq1.area())               # 9

class Starfighter:
    def __init__(self, n, p, h, l):
        self.name = n
        self.pilot = p
        self.maxhullpoints = h
        self.hullpoints = h     # Starts at maximum
        self.location = l

    def goto(self, destination):
        self.location = destination

    def takeDamage(self, dmg):
        self.hullpoints = self.hullpoints - dmg
        if self.hullpoints <= 0:    # "<= 0": zero hull is also destroyed
            self.hullpoints = 0     # Never show negative hull points
            print(self.pilot, "ejected safely")

class Xwing(Starfighter):
    # Class attributes: same values for every X-wing
    maxshields = 50
    maxtorpedoes = 6
    lasers = 4

    def __init__(self, n, p, h, l):
        super().__init__(n, p, h, l)            # Parent attributes first
        self.torpedoes = Xwing.maxtorpedoes     # Extra X-wing attributes
        self.shields = Xwing.maxshields

    # Overriding: shields absorb damage first, the rest hits the hull
    def takeDamage(self, dmg):
        if dmg <= self.shields:
            self.shields -= dmg                  # Shields absorb everything
        else:
            overflow = dmg - self.shields        # Damage left after shields
            self.shields = 0
            super().takeDamage(overflow)         # Reuse parent's hull logic

xw = Xwing("Red Five", "Luke", 50, "Yavin 4")
xw.takeDamage(30)                  # shields 50 -> 20
xw.takeDamage(40)                  # shields 0, hull 50 -> 30
xw.takeDamage(40)                  # hull 0 -> "Luke ejected safely"


# K-MEANS
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Blob parameters (same as the book): 5 centers, one std per blob
blob_centers = np.array([[0.2, 2.3], [-1.5, 2.3], [-2.8, 1.8],
                         [-2.8, 2.8], [-2.8, 1.3]])
blob_std = np.array([0.4, 0.3, 0.1, 0.1, 0.1])

# X = features (unlabeled data), y = true blob ids (we ignore them: unsupervised)
x,y = make_blobs(n_samples=200, centers=blob_centers,
                 cluster_std=blob_std, random_state=7)

k = 5
kmeans = KMeans(n_clusters=k, n_init=10, random_state=42)
# n_init=10: runs 10 random initializations, keeps the best (lowest inertia)
y_pred = kmeans.fit_predict(x)

print(y_pred)                                # Cluster index (0..4) per instance
print(kmeans.cluster_centers_)               # Centroid coordinates (k x n_features)
print(kmeans.inertia_)                       # Sum of squared distances to the closest centroid
print(silhouette_score(x, kmeans.labels_))   # Quality in [-1, 1]; closer to 1 is better

# Hard clustering: assign NEW points to the closest centroid
X_new = np.array([[0, 2], [3, 2], [-3, 3], [-3, 2.5]])
print(kmeans.predict(X_new))
# Soft clustering: distance from each new point to every centroid
print(kmeans.transform(X_new).round(2))

# Choosing k: elbow method (look for the "bend" in inertia)
inertias = [KMeans(n_clusters=i, n_init=10, random_state=42).fit(x).inertia_
            for i in range(1, 10)]
print(inertias)

# OOPD FOR KMEANS
import matplotlib.pyplot as plt

# ~~~~~~~~~~~ PARENT CLASS (like Hypercube) ~~~~~~~~~~~
class Clusterer:
    _default_k = 3                      # Class attribute: shared fallback value

    def __init__(self, k):
        if k < 1:                       # Same validation idea as Cube
            k = Clusterer._default_k
        self._n_clusters = k            # Protected attributes (convention)
        self._X = None                  # Data, set when we call fit()
        self._labels = None             # Cluster id of each instance
        self._fitted = False

    def getK(self):
        return self._n_clusters

    def setK(self, k):
        if k < 1:
            k = Clusterer._default_k
        self._n_clusters = k
        self._fitted = False            # Old results no longer match the new k

    def getLabels(self):
        return self._labels

    def whatAmI(self):
        print("I am a generic clusterer with", self._n_clusters, "clusters")

    def fit(self, X):
        # Abstract method: each child class must implement its own algorithm
        raise NotImplementedError("Subclasses must implement fit()")

    def plot(self, ax=None):
        # Generic plot: instances colored by cluster (works for 2D data)
        if ax is None:
            ax = plt.gca()
        ax.scatter(self._X[:, 0], self._X[:, 1], c=self._labels,
                   cmap="viridis", s=20)
        ax.set_xlabel("$x_1$")
        ax.set_ylabel("$x_2$")
        return ax


# ~~~~~~~~~~~ CHILD CLASS (like Square) ~~~~~~~~~~~
class KMeansClusterer(Clusterer):

    def __init__(self, k, n_init=10, random_state=42):
        super().__init__(k)             # Reuse the parent constructor
        self._n_init = n_init           # Random initializations (keeps the best)
        self._random_state = random_state
        self._model = None              # The scikit-learn KMeans, created in fit()

    # Overriding: replaces the parent's method (polymorphism)
    def whatAmI(self):
        print("I am a K-Means clusterer with", self._n_clusters, "clusters")

    # Overriding: here the abstract method gets a real implementation
    def fit(self, X):
        self._X = X
        self._model = KMeans(n_clusters=self._n_clusters,
                             n_init=self._n_init,
                             random_state=self._random_state)
        self._labels = self._model.fit_predict(X)   # Hard clustering
        self._fitted = True
        return self                     # Allows chaining: KMeansClusterer(5).fit(X)

    def _checkFitted(self):
        if not self._fitted:
            raise RuntimeError("Call fit() first")

    def getCentroids(self):
        self._checkFitted()
        return self._model.cluster_centers_

    def getInertia(self):
        self._checkFitted()
        return self._model.inertia_     # Sum of squared distances to closest centroid

    def getSilhouette(self):
        self._checkFitted()
        return silhouette_score(self._X, self._labels)  # In [-1, 1], higher is better

    def predict(self, X_new):
        self._checkFitted()
        return self._model.predict(X_new)   # Assign new points to the closest centroid

    # Overriding + super(): extend the parent's plot instead of rewriting it
    def plot(self, ax=None):
        ax = super().plot(ax)           # Parent draws the colored instances
        c = self.getCentroids()
        ax.scatter(c[:, 0], c[:, 1], marker="X", s=200, c="red",
                   edgecolor="black", label="Centroids")
        ax.set_title(f"K-Means (k={self._n_clusters})")
        ax.legend()
        return ax

    def plotDecisionBoundaries(self, ax=None, resolution=500):
        # Predict the cluster of every point of a grid -> Voronoi regions
        self._checkFitted()
        if ax is None:
            ax = plt.gca()
        mins = self._X.min(axis=0) - 0.1
        maxs = self._X.max(axis=0) + 0.1
        xx, yy = np.meshgrid(np.linspace(mins[0], maxs[0], resolution),
                             np.linspace(mins[1], maxs[1], resolution))
        Z = self._model.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)
        ax.contourf(xx, yy, Z, alpha=0.25, cmap="viridis")
        self.plot(ax)                   # Instances and centroids on top
        ax.set_title("Decision boundaries (Voronoi)")
        return ax

    # Static method (like isValid): needs neither self nor cls
    @staticmethod
    def elbow(X, k_max=9, ax=None):
        # Elbow method: look for the bend where inertia stops dropping fast
        if ax is None:
            ax = plt.gca()
        ks = range(1, k_max + 1)
        inertias = [KMeans(n_clusters=k, n_init=10, random_state=42).fit(X).inertia_
                    for k in ks]
        ax.plot(ks, inertias, "bo-")
        ax.set_xlabel("$k$")
        ax.set_ylabel("Inertia")
        ax.set_title("Elbow method")
        return inertias

    # Class method (like getSides): receives the class, builds a ready-to-use dataset
    @classmethod
    def generate_blobs(cls, n_samples=200, random_state=7):
        centers = np.array([[0.2, 2.3], [-1.5, 2.3], [-2.8, 1.8],
                            [-2.8, 2.8], [-2.8, 1.3]])
        std = np.array([0.4, 0.3, 0.1, 0.1, 0.1])
        X, y = make_blobs(n_samples=n_samples, centers=centers,
                          cluster_std=std, random_state=random_state)
        return X, y                     # y = true ids (unused: unsupervised)


# ~~~~~~~~~~~ USAGE ~~~~~~~~~~~
X, y = KMeansClusterer.generate_blobs()
km = KMeansClusterer(5).fit(X)
km.whatAmI()                            # I am a K-Means clusterer with 5 clusters
print(km.getCentroids())
print("Inertia:", km.getInertia())
print("Silhouette:", km.getSilhouette())
print(km.predict(np.array([[0, 2], [-3, 3]])))

# Three plots side by side
fig, axes = plt.subplots(1, 3, figsize=(16, 4.5))
km.plot(axes[0])
km.plotDecisionBoundaries(axes[1])
KMeansClusterer.elbow(X, ax=axes[2])
plt.tight_layout()
plt.show()

# Some Exam Exercises

# OOPD:
import random


class Hypercube:
    def __init__(self, dimension, length_edges):
        self.dimension = dimension
        self.length_edges = length_edges

    def whatAmI(self):
        print("I am a hypercube with dimensionality: " + self.dimension)

class Square(Hypercube):
    def __init__(self, area, perimeter):
        super().__init__(2, 4)
        self.area = area
        self.perimeter = perimeter

class Starfighter:
    def __init__(self, name, pilot, location, max_hull_points):
        self.name = name
        self.pilot = pilot
        self.location = location
        self.max_hull_points = max_hull_points
        self.hull_points = max_hull_points

    def goto(self, location):
        self.location = location

    def takeDamage(self, amount):
        self.hull_points = self.hull_points - amount
        if self.hull_points <= 0:
            print(self.pilot + " ejected safely")

class Xwing(Starfighter):
    def __init__(self, name, pilot, location):
        super().__init__(name, pilot, location, 50)
        self.lasers = 4
        self.max_shield_units = 50
        self.max_torpedoes = 6
        self.current_shield_units = self.max_shield_units
        self.current_torpedoes = self.max_torpedoes

    def takeDamage(self, amount):
        self.current_shield_units = self.current_shield_units - amount
        if self.current_shield_units <= 0:
            rest = abs(self.current_shield_units)
            super().takeDamage(rest)

    def attack(self, star_fighter_target):
        if not isinstance(star_fighter_target, Starfighter):
            raise TypeError("target must be a Starfighter")
        else:
            print("fires on " + star_fighter_target.name)
            amount = self.lasers * 20
            star_fighter_target.takeDamage(amount)
            if star_fighter_target.hull_points <= 0:
                print(star_fighter_target.name + " destroyed")

    def trenchRun(self):
        self.current_torpedoes = self.current_torpedoes / 2
        t = [1,2,3]
        shot = random.choice(t)
        if shot == 1:
            print(self.pilot + " successfully destroys the Death Star! (Everyone escaped safely)")
        else:
            print(self.pilot + " misses the shot!")

class TieFighter(Starfighter):
    def __init__(self, name, pilot, location):
        super().__init__(name, pilot, location, 30)
        self.lasers = 2

    def attack(self, star_fighter_target, amount=30):
        if not isinstance(star_fighter_target, Starfighter):
            raise TypeError("target must be a Starfighter")
        else:
            print("fires on " + star_fighter_target.name)
            amount = self.lasers * amount
            star_fighter_target.takeDamage(amount)
            if star_fighter_target.hull_points <= 0:
                print(star_fighter_target.name + " destroyed")

class TieAdvanced(TieFighter):
    def __init__(self, name, pilot, location):
        super().__init__(name, pilot, location)
        self.max_hull_points = 60
        self.lasers = 2
        self.max_shield_units = 60
        self.current_shield_units = self.max_shield_units

    def takeDamage(self, amount):
        self.current_shield_units = self.current_shield_units - amount
        if self.current_shield_units <= 0:
            rest = abs(self.current_shield_units)
            self.hull_points = self.hull_points - rest
            if self.hull_points <= 0:
                print(self.pilot + " ejected safely")

    def attack(self, star_fighter_target, amount=50):
        super().attack(star_fighter_target, amount)

    def rechargeShields(self):
        self.current_shield_units = self.max_shield_units

    def forceSense(self, star_fighter_target):
        if not isinstance(star_fighter_target, Starfighter):
            raise TypeError("target must be a Starfighter")
        else:
            if self.pilot == "Darth Vader" and star_fighter_target.pilot == "Luke Skywalker":
                print("Darth Vader senses the force is strong with Luke Skywalke")
            elif self.pilot != "Darth Vader":
                print(self.pilot + "does not know how to use the force")
            else:
                print("Nothing is sensed")

a = Xwing("Red three", "Biggs Darklighter", "Yavin-4")
b = Xwing("Red five", "Luke Skywalker", "Yavin-4")
a.goto("Death Star")
b.goto("Death Star")

c = TieFighter("Beta one", "Mook1", "Death Star")
d = TieFighter("Beta two", "Mook2", "Death Star")

e = TieAdvanced("Alpha one", "Darth Vader", "Death Star")

e.attack(a)
e.forceSense(b)
b.trenchRun()

s = "Halka"
x = [[1,2], [3,2,4,2,5]]
print("a"*2)

# File handling:
def increaseCounter(filename):
    try:
        with open(filename, "r") as f:       # read the current number
            v = int(f.readline())            # ValueError if not a valid integer
    except FileNotFoundError:
        raise ValueError("file missing")     # same error type for both problems

    with open(filename, "w") as f:           # overwrite with number + 1
        f.write(str(v + 1) + "\n")


def fileCounter():
    filename = input("Filename: ")
    while input("Press enter to count.") == "":   # empty input = count again
        try:
            increaseCounter(filename)
        except ValueError:
            print("Counter error")

def findMul(s, c):
    if len(c) > 1:
        raise ValueError("c has to be of only 1 character")
    count = 0
    result = ""
    for ch in s:
        if ch == c:
            count += 1
            for _ in range(count):
                result += c
        else:
            result += ch
    return result

# fileCounter()
# findMul("abababab","b")

