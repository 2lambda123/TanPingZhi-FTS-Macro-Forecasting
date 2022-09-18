# Goal
Collect **long term daily** data. Do not accept anything less than 15 years.

## Rationale 
Though there are some interesting monthly data such as morgage yield, their release dates are inconsistent. 
Extrapolating monthly data to daily data will induce garbage data.

## Procudure
1. Create your own branch and checkout the branch
2. Make sure you're on the branch ```git status``` and convert the unclean data to numpy while in that branch
    - data format: 2 columns (date, data value)
3. Chart the data
4. In the folder for cleaned data, create a data info txt file if there isnt one.
    - Include
      - name of data collected
      - data range YYYYMMDD-YYYYMMDD
      - data dimension
      - number of invalid values
