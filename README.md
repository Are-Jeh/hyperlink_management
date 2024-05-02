# hyperlink_management

An implementation of a US Patent (Detection and elimination for inapplicable hyperlinks: US US10042824B2)
which determines inapplicable and faulty hyperlinks based on several criteria

Implemented Latent semantic Indexing & Latent Dirichlet Allocation (unsupervised text analysis)

->The crawler will only crawl and scrape for text data and not for tables or images (separate modules to be generated for the same in V2). 

This project finds and removes hyperlinks that are unrelated or loosely related to the main page. It generates a new html file with removed links.
