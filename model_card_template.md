# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
This is a classification model on census bureau data that uses various demographic features to determine if an 
individual has an income over $50,000. The model is trained on the Adult Dataset (census data).
## Intended Use
The model should be used to predict the salary of an individual based off various demographics from census data.
## Training Data
The census data was split into a train dataset and test dataset. The training dataset consisted of 80% of the original 
dataset. The model was then trained on the train dataset. It was preprocessed using one-hot encoding, which converted
the categorical features into numerical representations. 

## Evaluation Data
The census data was split into a train dataset and test dataset. The test dataset consisted of 20% of the original 
dataset. 

## Metrics
_Please include the metrics used and your model's performance on those metrics._

The model was evaluated using precision, recall, and F1 score. The values include: 
Precision: 0.7353 | Recall: 0.6378 | F1: 0.6831

## Ethical Considerations
Fairness should be considered as the model may perform differently across different demographic groups.
## Caveats and Recommendations
Hyperparamter tuning could be used to improve the model. This process finds the best combination of hyperparamter
values for a model. 