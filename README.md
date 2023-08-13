Full Name & Batch
Dashboard / Deployment Link
Project Title
Project Description
Conclusion
# Credit card churn/ Attrition project

### Kevin Roderick Hartanto  Batch: RMT-20

-[Deployment](https://huggingface.co/spaces/kevinrhx/creditcardchurn)

Description: 
---Bank have a problem in regard to their credit card users, in that some of them decied to no longer in need of a credit card or move to another bank to provide their credit card need, as such the bank decied to hire us data analyst/ engineer to see which customer are prone to chrun and how to further prevent such churn. As such we will analysed the data that bank provided customer information who own credit cards and and try to see why the customer are quitting, we will also create a machine learning program to detect customer churn.
This program will use machine learning model such as SVC or desicion tree to predict the attrition of the credit card customers; as such we will use this information to prevent further churning of customer.

We will use library like sklearn to build the model and matplotlib to create the graph.

## Conclusion
After a bit of exporlation on the data we have found several key point to be discuss further:

1. Most customer that churn have less revolving balance then the one who didn't
2. People with the highest income and the lowest income are the one that are more likely to churn
3. from what we see the people who are likely to churn are the one who has no use or little use for credit cards in general

I would reccomend a way to give the user more insentive for the user to use credit card such as a special discount for credit card user, so a collaberation with retail store or even online store might lessen the burden of churning customer 

In conclusion we can see the best model for this project would be the RandomForestClassifier, with high recall and accuracy skill, the result are also confident with the result of the model, we can then use this model to predict which customer are more likely to churn and presentr them with bonuses or discout for the payment to make sure they are less likely to churn.