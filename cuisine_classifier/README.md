# Cuisine Classifier - Proof of Concept

This project is part of Yummy Magazine's ML challenge, where given a recipe
the program classifies the cuisine that it most likely belongs to (there are 20 classes in total).

## Challenges of this project:

Data preprocessing:
We were provided a nominal dataset in a json file with a large amount of dictionaries, such as the following:

```
{
    "id": 2362,
    "cuisine": "mexican",
    "ingredients": [
        "green chile",
        "jalapeno chilies",
        "onions",
        "ground black pepper",
        "salt",
        "chopped cilantro fresh",
        "green bell pepper",
        "garlic",
        "white sugar",
        "roma tomatoes",
        "celery",
        "dried oregano"
    ]
}
```

One of the first challenges was to preprocess this data so to train our model. However, all the different recipes (dictionaries) had different number of ingredients. My first method of overcoming this problem, while finding a way to represent ingredients as numbers, was to use what we call "one-hot encoding". Using this method, I could represent the ingredients present in a recipe with a '1' and those that are not with a '0'. The most number of ingredients in a recipe was 65. Therefore, we would have the following:

```
{
    "id": 2362,
    "cuisine": "mexican",
    "ingredients": [0,1,0,0,0,1,0,0,1 ... 0,1]
}
```

As one might expect, this representation of the dataset would not favor our cuisine classification model. This method gave me a model score of 0.24. The number of ingredients were too variable and yielding a dataset dominated by 0's.

Therefore in order to overcome this, I started to think of a new approach where I could give value to what the ingredients are rather than just consider if they are present or not.

For that I coded [frerquency.py](./data/unprocessed/frequency.py) that gives me a list of top 10 ingredients that are specific and relevant to each cuisine and another list of ingredients that are crucial but repeated in at least two cuisines.

Next, I programmed [preprocess_original.py](./data/unprocessed/preprocess_original.py) that allowed me to create a preprocessed training dataset. This new dataset considered each ingredient of a recipe and categorize it in three features: class, region and subregion.

```
{
    "id": 2362,
    "cuisine": "mexican",
    "ingredients": [
        [0, 1, 15.5],
        [15, 0, 0],
        [0, 1, 3],
        [0, 1, 15.5],
        [14, 0, 0],
        [0, 1, 2],
        [0, 1, 14],
        [15, 0, 0],
        [4, 0, 0],
        [0, 1, 1.5],
        [15, 0, 0],
        [2, 0, 0],
    ]
}
```

This new way to represent the dataset drastically improved the accuracy. However, there is still more improvements that can be made.
