"""
Tutorial 00: LISC Overview
==========================

An overview of the LISC code organization and approach.
"""

###################################################################################################
#
# LISC Overview
# -------------
#
# LISC, or 'Literature Scanner', is a module for collecting and analyzing data and
# information from the scientific literature.
#
# In this overview tutorial, we will first explore the main aspects of LISC, and
# how it handles terms, data, files and requests.
#
# LISC serves as a wrapper around available application programmer interfaces (APIs)
# for interacting with databases that store scientific literature and related data.
#
# In this first overview, we will explore how LISC's code structure.
#

###################################################################################################
#
# Available Analyses
# ~~~~~~~~~~~~~~~~~~
#
# The functionality of LISC is dependent on the APIs that are supported.
#
# Currently supported external APIs include the NCBI EUtils, offering access to the Pubmed
# database, and the OpenCitations API, offering access to citation data.
#
# EUtils:
#   - Counts: collecting word co-occurence data, counting how often terms occur together.
#   - Words: collecting text data and meta-data from papers.
#
# OpenCitations:
#   - Cites: collecting citation data, counting the number of citations papers have
#

###################################################################################################
#
# LISC Objects
# ------------
#
# LISC is object oriented, meaning it offers and uses objects in order to handle
# search terms, collected data, and API requests.
#
# Here we will first explore the `Base` object, the underlying
# object structure for any data collections using search terms.
#
# Note that you will not otherwise use the `Base` object directly, but that it is the
# underlying object for the `Counts` and `Words` objects.
#

###################################################################################################

from lisc.objects.base import Base

###################################################################################################

# Initialize a base object
base = Base()

###################################################################################################
#
# Search Terms
# ------------
#
# For collecting papers and literature data, one first has to select search terms to
# find the literature of interest.
#
# Note that by default, all search terms as used as exact term matches.
#

###################################################################################################

# Set some terms
terms = [['chemistry'], ['biology']]

# Add terms to the object
base.add_terms(terms)

###################################################################################################

# Check the terms added to the base object
base.check_terms()

###################################################################################################
#
# Complex Search Terms
# --------------------
#
# So far, we have chosen some search terms, as single terms, to use as queries,
# and added them to our object.
#
# Sometimes we might want more than just particular search words. We might want to
# specify synonyms and/or use include inclusions or exclusion words.
#
# Synonyms
# ~~~~~~~~
#
# To include synonyms, just add more entries to the input list of terms.
#
# Synonyms are combined with the 'OR' operator, meaning results will
# be returned if they include any of the given terms.
#
# For example, the set of search terms ['brain', 'cortex'] is interpreted as:
# '("brain"OR"cortex")'.
#
# Note that being able to include synonyms is the reason each term entry is itself a list.
#
# Inclusion & Exclusion Words
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
# Sometimes we might need to control the results that we get, by including inclusion
# and exclusion words. Inclusions words are words that must also appear in the document
# for a result to be returned. Exclusions words are words that must not be included in a
# result in order for it to be returned.
#
# Inclusions words are combined with the 'AND' operator, meaning entries
# will only be included if they also include these words.
#
# For example, the search terms ['brain', 'cortex'] with the inclusion word ['biology']
# is interpreted as '("brain"OR"cortex")AND("biology")'.
#
# Exclusion words are combined with the 'NOT' operator, meaning entries
# will be excluded if they include these terms.
#
# For example, the search terms ['brain', 'cortex'] with the exclusion word ['body']
# is interpreted as '("brain"OR"cortex")NOT("body")'.
#
# Putting it all Together
# ~~~~~~~~~~~~~~~~~~~~~~~
#
# Synonyms, inclusion and exclusion words can all be used together. Note also that
# you can also specific synonyms for inclusion and exclusion words.
#
# For example, the following set of search term components:
#
# - search terms ['brain', 'cortex']
# - inclusion words ['biology', 'biochemistry']
# - exclusion words ['body', 'corporeal']
#
# All combine to give the seach term of:
#
# - `'("gene"OR"genetic)AND("biology"OR"biochemistry")NOT("body"OR"corporeal)'`
#
# Note that inclusion and exclusion words are should be lists of the same
# length as the number of search terms. Each inclusion and exclusion term
# is used for the corresponding search term.
#
# Now let's update our set of terms, to include some synonyms, inclusions and exclusions.
#

###################################################################################################

# Set up a list of multiple terms, each with synonyms
terms = [['gene', 'genetic'], ['cortex', 'cortical']]

# Add the terms
base.add_terms(terms)

###################################################################################################

# Set up inclusions and exclusions
#   Each is a list, that should be the same length as the number of terms
inclusions = [['brain'], ['body']]
exclusions = [['protein'], ['subcortical']]

# Add the inclusion and exclusions
base.add_terms(inclusions, 'inclusions')
base.add_terms(exclusions, 'exclusions')

###################################################################################################

# Check the loaded terms
base.check_terms()

###################################################################################################

# Check inclusion & exclusion words
base.check_terms('inclusions')
base.check_terms('exclusions')

###################################################################################################
#
# Note that each inclusion / exclusion term is mapped to it's associated search term
# based on it's index. Inclusion and exclusion word lists should also be the same length
# as the set of search terms. If there are no inclusions / exclusions for a given search
# term, leave it empty with an empty list.
#

###################################################################################################
#
# Labels
# ~~~~~~
#
# Since search terms with synonyms and exclusions are complex (have multiple parts), LISC
# will also create 'labels' for each search term, where the label for each term is the
# first item in each term list.
#

###################################################################################################

# Check the label for the current terms
base.labels

###################################################################################################
#
# LISC Objects
# ~~~~~~~~~~~~
#
# Though LISC offers an object-oriented approach, note that the core procedures available
# for scraping and analyzing data are implemented as stand-alone functions.
#
# The objects serve primarily to help organize the data and support common analyses.
#
# If you prefer, you can use the functions directly, in particular, for more custom approaches.
#
# See the examples page for some examples of using LISC directly with functions.
#

###################################################################################################
#
# Database Management
# -------------------
#
# When collecting and analysing literature, there can be a lot of data, and therefore
# a lot of files, to keep track of.
#
# For that reason, LISC offers a database structure. If you use this file structure,
# LISC functions can automatically load and save files to an organized output structure.
#

###################################################################################################

from lisc.utils.db import SCDB, create_file_structure

###################################################################################################

# Create a database file structure.
#   Note that when called without a path argument input,
#   the folder structure is made in the current directory.
db = create_file_structure()

###################################################################################################

# Check the file structure for the created database
db.check_file_structure()
