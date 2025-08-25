# a little web scraper

## Assumptions
I pretended this scraper was to retrieve information about competing products so I choose to retrieve only name, price and the product rating. This ignores other information Costco provides such as availability, dimensions, etc.

## Future Nice to Haves
I'm unsure how long the api key I received will remain valid. If it does expire, a nice to have would be a way to retrieve a new api key automatically.

Currently, I generate the output files into the root folder. It would be nice to generate them into a subfolder but I didn't feel like creating a new variable to store the absolute path to the subfolder for this.

This scraper only queries products for my local Costco warehouse (and online products for mainland US, I think). I could probably make that variable if I had a lot more time to figure out their api parameters. whloc is the warehouse location but I haven't figured out loc. I only know loc is a required parameter. 