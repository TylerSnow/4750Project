Run Program:<br>
>>-Program requires [scikit-learn](https://scikit-learn.org)<br>
>>-to run application user must direct themselves into the src folder using the terminal.<br>
>>-Then the user must run the command "python ui.py" which will prompt the application.<br><br>

Training:<br>
>>-to train models select the train tab at the top of the application.<br>
>>-From there select which model you wish to train and the respective dataset.<br>
>>-NOTE Program automatically overwrites the most recent training model for each algorithm.<br><br>

Testing:<br>
>>-Using the test tab at the top of the application the user must select what sets(multiple) they wish to test the models on.<br> 
>>-Then select the test button and wait for the tests to complete(May take a minute depending on size of testing sets).<br> 
>>-Once completed the results of each algorithms accuracy relative to each test set will be displayed in the grid at the bottom of the test tab.<br><br>

Adding Custom Sets:<br>
>>-If the user wishes to use their own custom data they should add them to (PathToProject/Project/Datasets/custom(1,2 or 3).<br>
>>-Sets must then be placed in the test or training folders depending on what the user wishes to use them for.<br>
>>-Sets must be given in the form of text files that are stored in folders named 'pos/' or 'neg/' depending on their sentiment.<br>
