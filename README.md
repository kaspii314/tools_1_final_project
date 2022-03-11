# The Metropolitan Museum of Art: Open Access CSVs

## Dataset & Motivation

The Metropolitan Museum of Art ("The Met") launched its <a href="https://www.metmuseum.org/about-the-met/policies-and-documents/open-access">Open Access Initiative</a> in February of 2017, releasing information on more than 470,000 artworks in its Collection for unrestricted commercial and noncommercial use. Per The Met's website: "The Open Access initiative represents an incredible body of ongoing work by curators, conservators, photographers, librarians, cataloguers, interns, and technologists over the past 151 years of the institution's history - new images and data are added each year. It is also an important statement about The Met's commitment to increasing access to the collection in a digital age. In the last four years, Open Access images and data have been viewed over 1.2 billion times and downloaded over 7 million times." 

This research project utilizes <a href="https://github.com/metmuseum/openaccess">The Met Open Access CSV</a>, which contains 52 manually cataloged attributes describing the artwork itself, artists, cultures, geographies, classifications, department, and gallery numbers. Additionally, the data file notes the year The Met took ownership of the artwork (Accession Year), as well as indicates if the artwork is a highlight piece, part of the <a href="https://www.metmuseum.org/toah/">Heilbrunn Timeline of Art History</a>, or in the public domain.

### The Met Open Access CSV Data Elements
* Object Number
* Is Highlight
* Is Timeline Work
* Is Public Domain
* Object ID
* Gallery Number
* Department
* Accession Year
* Object Name
* Title
* Culture
* Period
* Dynasty
* Reign
* Portfolio
* Constituent ID
* Artist Role
* Artist Prefix
* Artist Display Name
* Artist Display Bio
* Artist Suffix
* Artist Alpha Sort
* Artist Nationality
* Artist Begin Date
* Artist End Date
* Artist Gender
* Artist ULAN URL
* Artist Wikidata URL
* Object Date
* Object Begin Date
* Object End Date
* Medium
* Dimensions
* Credit Line
* Geography Type
* City
* State
* County
* Country
* Region
* Subregion
* Locale
* Locus
* Excavation
* River
* Classification
* Rights and Reproduction
* Link Resource
* Object Wikidata URL
* Metadata Date
* Repository
* Tags
* Tags AAT URL
* Tags Wikidata URL



## Research Questions

The primary research question of our project is: <i>Can we determine artwork features that make it likely to be a highlight piece?</i>

This main topic leads to several secondary questions:
* Which attributes represent the artwork's artist, time, geography, and medium? How can we turn these into meaningful features?
* Of all available attributes, which are the cleanest and most reliable?
* Artworks are unlikely to become highlight pieces if they are not displayed. Is there an attribute that can be used to determine if an artwork is displayed?
* Are there any outlier collections that should be analyzed separately?

We begin by answering our secondary research questions using all of the dataset's observations and attributes. The output of this preliminary analysis is a final dataset that is then used for data mining. Using Random Forest and other visualizations, we attempt to determine which features of this final dataset make it likely that an artwork is a highlight piece.



## Binder Link