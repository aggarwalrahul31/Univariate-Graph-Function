
# coding: utf-8

# #### Base :A function which will give histogram and boxplot for numerical variables and bar plots for categorical variables
#    - Exports graph to curent directory,if directory is not specified even if  the directory entered is wrong.
#    - Exports graph for all the columns if column names are not specified.
#    - If the column name specifed is wrong then it exports the graph for only correct column labels.
#    - If all the column labels are wrong it exports the graph for all the column labels.

# In[5]:


def Graph(data1,column=None,directory=None):
    """
    A function that returns box plots and histograms for numerical variables and bar plot for categorical variables. 
    Input parameters:Graph(data,column=None,directory=None).
    column:Specify column labels in a list.
    directory:Specify directory in which plots needs to be downloaded.
    If column labels are not specified,it plots for all columns.
    If directory is not specified,it outputs the plots in the current directory.
    """
    import csv
    import os
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    
    if directory==None:
        directory=os.getcwd()                    #Getting the current directory if directory is not specified.
    else:
        orig_dir=os.getcwd()
    
    plt.ioff()                                    #Turn interactive ploting off.
    plt.rcParams['figure.figsize'] = (8,6)
    
    if os.path.exists(directory):
        os.chdir(directory)
    else:
        print('The given directory does not exists and saving the graphs in the current directory ',os.getcwd())
        directory=os.getcwd()
    if column==None:
        column=data1.columns                     #Getting all the columns if columns are not specified.
        df=data1
    elif set(column).issubset(data1.columns.tolist()):
            df=data1.loc[:,column]
    else:
        diff=np.setdiff1d(column,data1.columns.tolist())       #subsetting the values which are incorrect.
        column=np.setdiff1d(column,diff)
        print(diff,"is the list of column labels not present in dataset given.")
        print("*"*50)
        print("Although,we will provide you with graphs for correct column labels")
        if len(column)==0:
            column=data1.columns                 #Getting all the column labels 
        df=data1.loc[:,column]
    df_dtype=pd.DataFrame(df.dtypes)             
    for i in column:
        if (df_dtype.loc[i,][0]=='object'):      #categorical values.
            fig=plt.figure()
            df[i].value_counts().plot(kind='barh')  #plotting bar graph.
            plt.title('Bar graph of '+str(i))    
            plt.ylabel(str(i))
            plt.xlabel('Count')
            plt.savefig("Bar graph of "+ str(i) +'.png')
            plt.close(fig)
        else:                                        #for all numerical variables.
            fig = plt.figure()
            plt.boxplot(x=df.loc[:,i])              #plotting boxplot.
            plt.title("Box plot of " + str(i))
            plt.ylabel(str(i))
            plt.savefig("BoxPlot of "+str(i) +'.png')
            plt.close(fig)
            
            fig = plt.figure()
            plt.hist(x=df.loc[:,i],color='black',edgecolor='yellow')    #plotting histogram.
            plt.ylabel("Frequency")
            plt.xlabel(str(i))
            plt.title("Histogram of " + str(i))
            plt.savefig("Histogram "+str(i)+'.png')  
            plt.close(fig)
    os.chdir(orig_dir)                               #changing my directory to original directory.


# #### Improvisation 1: 
#    - Plotting bar plots for most frequent unique values upto 25.

# In[6]:


def Graph1(data1,column=None,directory=None):
    """
    A function that returns box plots and histograms for numerical variables and bar plot for categorical variables.
    It will return 25 most frequent unique values and will plot bar graph for integer variables less than equal to 
    25 unique values.
    Input parameters:Graph(data,column=None,directory=None).
    column:Specify column labels in a list.
    directory:Specify directory in which plots needs to be downloaded.
    If column labels are not specified,it plots for all columns.
    If directory is not specified,it outputs the plots in the current directory.  
    """
    import csv
    import os
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    
    if directory==None:
        directory=os.getcwd()                    #Getting the current directory if directory is not specified.
    else:
        orig_dir=os.getcwd()
    plt.ioff()
    plt.rcParams['figure.figsize'] = (8,6)
    
    if os.path.exists(directory):
        os.chdir(directory)
    else:
        print('The given directory does not exists and saving the graphs in the current directory ',os.getcwd())
        directory=os.getcwd()
    if column==None:
        column=data1.columns
        df=data1
    elif set(column).issubset(data1.columns.tolist()):
            df=data1.loc[:,column]
    else:
        diff=np.setdiff1d(column,data1.columns.tolist())     #subsetting the values which are incorrect.
        column=np.setdiff1d(column,diff)
        print(diff,"is the list of column labels not present in dataset given.")
        print("*"*50)
        print("Although,we will provide you with graphs for correct column labels")
        if len(column)==0:
            column=data1.columns                    #Getting all the column labels if all the specified column labels are wrong.
        df=data1.loc[:,column]
    
    df_dtype=pd.DataFrame(df.dtypes)
    for i in column:
        if (df_dtype.loc[i,][0]=='object'):             #categorical values
            fig=plt.figure()
            df[i].value_counts()[:25].plot(kind='barh')  #plotting top 25 unique values only
            plt.title('Bar graph of'+str(i))
            plt.ylabel(str(i))
            plt.xlabel('Count')
            plt.tight_layout()
            plt.savefig("Bar graph of "+ str(i) +'.png')
            plt.close(fig)
        elif (df_dtype.loc[i,][0]=='int64') and len((df[i].unique()))<=25: #numerical variables having less than equal 25 unique values
            fig=plt.figure()
            df[i].value_counts()[:25].plot(kind='barh')      #plotting bar graph
            plt.title('Bar graph of'+str(i))
            plt.ylabel(str(i))
            plt.xlabel('Count')
            plt.tight_layout()
            plt.savefig("Bar graph of "+ str(i) +'.png')
            plt.close(fig)
        else:
            fig = plt.figure()
            plt.boxplot(x=df.loc[:,i],notch=True)            #plotting boxplot
            plt.title("Box plot of " + str(i))
            plt.ylabel(str(i))
            plt.tight_layout()
            plt.savefig("BoxPlot of "+str(i) +'.png')
            plt.close(fig)
            
            fig = plt.figure()
            plt.hist(x=df.loc[:,i],color='black',edgecolor='yellow')    #plotting histogram
            plt.ylabel("Frequency")
            plt.xlabel(str(i))
            plt.title("Histogram of " + str(i))
            plt.tight_layout()
            plt.savefig("Histogram "+str(i)+'.png')
            plt.close(fig)
    os.chdir(orig_dir)


# #### Improvisation 2:
#    - Plotting bar plots if the user enters index values/label names for columns.
#    - Giving summary of the data in a csv file which includes number of missing values.
#    - Ploting the graph of boxplot and histogram side by side for a column label.
#    - Creating a local module UnivariateAnalysis which can be used to import these functions.

# In[7]:


def Graph2(data1,column=None,directory=None):
    """
    A function that returns box plots and histograms for numerical variables and bar plot for categorical variables.
    It will return 25 most frequent unique values and will plot bar graph for integer variables less than equal to 
    25 unique values.
    It will return plots for both indexes and label names specified in column parameter.
    It plots the histogram and boxplot in the same graph(side by side) for numerical variables.
    It will give summary with missing values for the columns specified.
    Input parameters:Graph(data,column=None,directory=None).
    column:Specify column labels in a list.
    directory:Specify directory in which plots needs to be downloaded.
    If column labels are not specified,it plots for all columns.
    If directory is not specified,it outputs the plots in the current directory.  
    """
    import csv
    import os
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    
    if directory==None:
        directory=os.getcwd()                         #Getting the current directory if directory is not specified
    else:
        orig_dir=os.getcwd()
    
    plt.style.use("ggplot")
    plt.ioff()
    plt.rcParams['figure.figsize'] = (8,6)
    if column!=None:
        num_l=[x for x in column if str(x).isdigit()]  #Extracting numeric index for column labels
        num_diff=[z for z in num_l if z>data1.shape[1]] #Extracting wrong column indexes.
        num_l=np.setdiff1d(num_l,num_diff).tolist()
        str_c=[y for y in column if str(y).isalpha()]
        column=str_c
    if os.path.exists(directory):
        os.chdir(directory)
    else:
        print('The given directory does not exists and saving the graphs in the current directory ',os.getcwd())
        directory=os.getcwd()
    if column==None:
        column=data1.columns
        df=data1
    elif set(column).issubset(data1.columns.tolist()):
            df=data1.loc[:,column]
    else:
        diff=np.setdiff1d(column,data1.columns.tolist())    #subsetting the values which are incorrect.
        column=np.setdiff1d(column,diff)
        print(diff.tolist()+num_diff,"is the list of column labels/indexes not present in dataset given.")
        print("*"*50)
        print("Although,we will provide you with graphs for correct column labels")
        if len(column)==0:
            column=data1.columns
        col_ind=data1.columns.get_indexer(column).tolist()
        col_indl=list(set(col_ind+num_l))
        df=data1.iloc[:,col_indl]
        column=data1.columns[col_indl].tolist()
    
    df_dtype=pd.DataFrame(df.dtypes)
    for i in column:
        if (df_dtype.loc[i,][0]=='object'):
            fig=plt.figure()
            df[i].value_counts()[:25].plot(kind='barh')  #plotting top 25 unique values only
            plt.title('Bar graph of'+str(i))
            plt.ylabel(str(i))
            plt.xlabel('Count')
            plt.tight_layout()
            plt.savefig("Bar graph of "+ str(i) +'.png')
            plt.close(fig)
        elif (df_dtype.loc[i,][0]=='int64') and len((df[i].unique()))<=25: #numerical variables having less than equal 25 unique values
            fig=plt.figure()
            df[i].value_counts()[:25].plot(kind='barh')   #plotting bar graph
            plt.title('Bar graph of'+str(i))
            plt.ylabel(str(i))
            plt.xlabel('Count')
            plt.tight_layout()
            plt.savefig("Bar graph of "+ str(i) +'.png')
            plt.close(fig)
        else:
            fig, (ax1,ax2) = plt.subplots(ncols= 2, figsize = (12,6)) 
            ax1.hist(x = df.loc[:,i],color='black',edgecolor='yellow') #creating histogram in the same graph
            ax1.set_title("Histogram of " + str(i))
            ax1.set_xlabel(str(i))
            ax1.set_ylabel("Frequency")
            ax2.boxplot(x=df.loc[:,i],notch=True) #creating boxplot in same graph
            ax2.set_title("Box plot of " + str(i))
            ax2.set_ylabel(str(i))
            plt.tight_layout()
            plt.savefig("Histogram & BoxPlot of "+str(i)+'.png')
            plt.close(fig)
    df.describe(include='all').to_csv('Summary.csv')  #creating a file summary
    row=['Missing Values']
    for l in column:       #appending missing values for each column
        row.append(df[l].isnull().sum())
    with open('Summary.csv','a') as csvf:
        write= csv.writer(csvf)
        write.writerow(row)
    
    csvf.close()
    os.chdir(orig_dir)  #returning to original directory

