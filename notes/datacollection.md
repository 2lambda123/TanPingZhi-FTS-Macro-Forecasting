# Goal
Collect **long term daily** data. Try not to accept anything less than 15 years.

## Rationale 
Though there are some interesting monthly data such as morgage yield, their release dates are inconsistent. 
Extrapolating monthly data to daily data will induce garbage data as the model will know the data even before the data is even released.

## Procudure
1. Create your own branch and checkout the branch
2. Make sure you're on the branch ```git status``` and convert the unclean data to numpy while in that branch
    - data format: 2 columns (date, data value)
3. Chart the data and some fast data visualisation (For sanity checks in the future)
4. In the folder for cleaned numpy data, create a data info txt file if there isnt one.
    - Include
      - name of data collected
      - data range YYYYMMDD-YYYYMMDD
      - data dimension
      - number of invalid values
5. add, commit, push changes into **your own branch**
6. Bring your work into the main folder - checkout main and add selected files (data, data info etc)
    - ```git checkout main```
    - ```git checkout your-new-branchname <path>/filename.filetype```
