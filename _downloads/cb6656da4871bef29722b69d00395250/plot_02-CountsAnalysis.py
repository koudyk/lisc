"""
Tutorial 02: Counts Analysis
============================

Analyzing scraped co-occurence data.
"""

###################################################################################################
#
# Counts Analyses
# ---------------
#
# This tutorial explores the built in utilities for exploring & analyzing counts data.
#

###################################################################################################

from lisc.utils.db import SCDB
from lisc.utils.io import load_object

from lisc.plts.counts import *

###################################################################################################

# Reload the counts object from the last tutorial
counts = load_object('tutorial_counts', SCDB('lisc_db'))

###################################################################################################
#
# The `Counts` object has some helper methods to explore the collected data.
#
# First lets check the number of counts per term list.
#

###################################################################################################

# Look at the collect counts data for the first set of terms
counts.check_data(data_type='counts', dim='A')

###################################################################################################

# Look at the collect counts data for the second set of terms
counts.check_data(data_type='counts', dim='B')

###################################################################################################
#
# Normalization & Scores
# ----------------------
#
# The Counts co-occurence data collection gives us a raw data matrix of the number of
# papers in with terms co-occur, as well as counts of the number of total papers using
# each term.
#
# Once we have this, we often will want to calculate either normalized co-occurence
# measures, and/or some kind of similarity score.
#
# To normalize the data, we can divide the co-occurence counts by the number of papers
# per term. This allows us the examine and analyze, for example, the proportions of papers
# that include particular co-occurence patterns.
#
# We can also calculate some kind of association index or score. For example, the
# `Jaccard index <https://en.wikipedia.org/wiki/Jaccard_index>`_ is a standard meassure
# for measuring the similarity of samples, and is also available to compute and use.
#
# When using the counts object, both of these measures are available, through the
# `compute_score` method. You can indicate which kind of score (normalization or association)
# index) as an input to the method.
#

###################################################################################################

# Compute a normalization of the co-occurence data
counts.compute_score('normalize', dim='A')

###################################################################################################

# Check out the computed normalization
print(counts.score)

###################################################################################################
#
# The normalization is the number of papers with both terms, divided by the number of
# papers for each term alone. It can therefore be interpreted as a proportion of papers
# with term `a` that also have term `b`, or as `a & b / a`.
#
# Note that when using two different terms lists, you have to choose which list of
# terms to normalize by. That is controlled by the 'dim' input.
#
# In this case, we have calculated the number normalized data as the proportion of
# papers for each anatomical term that include each perception term.
#

###################################################################################################

# Compute the association index
counts.compute_score('association')

###################################################################################################

# Check out the computed score
print(counts.score)

###################################################################################################
#
# The Jaccard index is a normalized measure of similarity, bounded between 0 and 1.
#
# One benefit of the Jaccard index is that you do not have to choose a terms list
# to normalize by - the calulated measure considers both terms lists.
#

###################################################################################################
#
# Plotting and Clustering for Counts Data
# ---------------------------------------
#
# Co-occurence data is basically a matrix of numbers reflecting the relationship between terms.
#
# LISC provides some plot function to visualize the co-occurence data, as a matrix.
#
# In addition to plotting the data, we can also do clustering analysis and visualizations,
# that attempt to find structure in the data. LISC also offers some common clustering
# approaches to sort and visualize collected co-occurence data.
#

###################################################################################################

# Plot a matrix of the association index data
plot_matrix(counts.score, counts.terms['B'].labels, counts.terms['A'].labels)

###################################################################################################

# Plot a clustermap of the association index data
plot_clustermap(counts.score, counts.terms['B'].labels, counts.terms['A'].labels)

###################################################################################################

# Plot a dendrogram, to cluster the terms
plot_dendrogram(counts.score, counts.terms['B'].labels)
